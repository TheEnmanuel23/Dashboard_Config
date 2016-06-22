$(document).ready(function(){
	window.views.app = new ConfigDashboard.Views.App($('body'));
    window.collections.layers = new ConfigDashboard.Collections.LayersCollections();
    window.views.layers = new ConfigDashboard.Views.LayersView({
        model: window.collections.layers
    });
});