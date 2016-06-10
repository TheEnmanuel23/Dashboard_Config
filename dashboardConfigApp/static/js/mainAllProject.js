$(document).ready(function(){
	window.collections.allProjectCollection = new ConfigDashboard.Collections.ProjectCollection();
	window.views.projectViews = new ConfigDashboard.Views.ProjectView({
		model: window.collections.allProjectCollection
	});
	window.collections.allProjectCollection.fetch();
});