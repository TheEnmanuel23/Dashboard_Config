ConfigDashboard.Models.ProjectModel = Backbone.Model.extend({
	url: '/get_all_projects/'
});

ConfigDashboard.Models.LayersModel = Backbone.Model.extend({
	defaults: function(){
		return {
			idCapa: '0',
			descripcion: 'None'
		}
	}
});