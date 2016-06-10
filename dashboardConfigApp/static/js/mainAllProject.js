$(document).ready(function(){
	window.collections.allProjectsCollection = new ConfigDashboard.Collections.ProjectsCollection();
	window.views.projectViews = new ConfigDashboard.Views.ProjectsView({
		model: window.collections.allProjectsCollection
	});
	window.collections.allProjectsCollection.fetch();

	// window.routers.routerConfigDashboard = new ConfigDashboard.Routers.RoutersConfigDashboard();
	/*window.routers.routerConfigDashboard.on("route:configProject", function(){

	});*/
});