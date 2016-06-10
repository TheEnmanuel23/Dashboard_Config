$(document).ready(function(){
	window.collections.allProjectCollection = new ConfigDashboard.Collections.ProjectCollection();
	window.collections.allProjectCollection.on('add', function(model){
		var view = new ConfigDashboard.Views.ProjectView({model:model});
		view.render();
		view.$el.appendTo('#allProject_table_tbody');
	});
	window.collections.allProjectCollection.fetch();
});