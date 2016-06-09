$(document).ready(function(){
	window.models.capasModel = new ConfigDashboard.Models.CapasModel();
	window.collections.capasCollections = new ConfigDashboard.Collections.CapasCollection();
	window.views.capasView = new ConfigDashboard.Views.CapasView({
		model : window.collections.capasCollections
	});

	window.views.app = new ConfigDashboard.Views.App($('body'));
	window.routers.steps = new ConfigDashboard.Routers.StepsConfig();
	window.routers.steps.on("route:root", function(){
	});
	window.routers.steps.on("route:step", function(){
	});

	Backbone.history.start({
			root: '/',
			pushState: true
	});
});