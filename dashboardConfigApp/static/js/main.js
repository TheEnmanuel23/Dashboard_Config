$(document).ready(function(){
	window.templates.allProject = _.template($('#allProjectTemplate').html())

	window.collections.capasCollections = new ConfigDashboard.Collections.CapasCollection();
	window.views.capasView = new ConfigDashboard.Views.CapasView({
		model : window.collections.capasCollections,
	});
	window.views.app = new ConfigDashboard.Views.App($('body'));
	Backbone.history.start({
			root: '/',
			pushState: true
	});

	window.collections.allProjectCollection = new ConfigDashboard.Collections.ProjectCollection();
	window.collections.allProjectCollection.on('add', function(model){
		var view = new ConfigDashboard.Views.ProjectView({model:model});
		view.render();
		view.$el.appendTo('#allProject_table_tbody');
	});
	window.collections.allProjectCollection.fetch();
});