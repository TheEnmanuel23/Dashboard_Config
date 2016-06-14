ConfigDashboard.Collections.ProjectsCollection = Backbone.Collection.extend({
	model: ConfigDashboard.Models.ProjectModel,
	url: '/get_all_projects'
});

ConfigDashboard.Collections.LayersCollections = Backbone.Collection.extend({
	Model: ConfigDashboard.Models.LayersModel,
	// url: '/get_layers/project/' + this.idProject
});