ConfigDashboard.Routers.StepsConfig = Backbone.Router.extend({
	routes:{
		"new_project/": "rootProject",
		"new_project/:projectName": "step"
	},
	root: function(){
		window.app.state = 'root';
		window.app.indicadorRegion = null;
	},
	step: function(projectName){
		window.app.state = 'projectName';
		window.app.indicadorRegion = step;		
	}
});