ConfigDashboard.Views.ProjectView = Backbone.View.extend({	
	render: function(){
		var data = this.model.toJSON();
		var html = window.templates.allProject(data);
		this.setElement(html);
	}
});