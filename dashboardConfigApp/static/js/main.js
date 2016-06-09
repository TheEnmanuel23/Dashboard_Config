$(document).ready(function(){
	window.collections.capasCollections = new ConfigDashboard.Collections.CapasCollection();
	window.views.capasView = new ConfigDashboard.Views.CapasView({
		model : window.collections.capasCollections,
	});
	window.views.app = new ConfigDashboard.Views.App($('body'));
	Backbone.history.start({
			root: '/',
			pushState: true
	});
});