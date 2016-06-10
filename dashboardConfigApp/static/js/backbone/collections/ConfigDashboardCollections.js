ConfigDashboard.Collections.ProjectsCollection = Backbone.Collection.extend({
	model: ConfigDashboard.Models.ProjectModel,
	url: '/get_all_projects'
});

ConfigDashboard.Collections.CapasCollection = Backbone.Collection.extend({
	Model: ConfigDashboard.Models.CapasModel
});