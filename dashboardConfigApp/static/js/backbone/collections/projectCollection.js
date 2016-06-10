ConfigDashboard.Collections.ProjectsCollection = Backbone.Collection.extend({
	model: ConfigDashboard.Models.ProjectModel,
	url: '/get_all_projects'
});