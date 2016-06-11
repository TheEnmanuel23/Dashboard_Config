$(document).ready(function(){
	window.collections.layersCollections = new ConfigDashboard.Collections.LayersCollections();
	window.views.layersViews = new ConfigDashboard.Views.LayersView({
		model: window.collections.layersCollections
	});
	window.collections.layersCollections.fetch();
});