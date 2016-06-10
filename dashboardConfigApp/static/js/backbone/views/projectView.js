ConfigDashboard.Views.ProjectsView = Backbone.View.extend({
	initialize: function(){
		this.model.on('add', this.addSingle);
	},
	addSingle: function(project){
		if(project.view == null)
			project.view = new ConfigDashboard.Views.ProjectViewSingle({model: project});
		project.view.render();
		project.view.$el.appendTo('#allProject_table_tbody');
	}
});

ConfigDashboard.Views.ProjectViewSingle = Backbone.View.extend({
	initialize: function(){
	},
	events: {
		"click .goToConfig": "goToConfig_click"
	},
	render: function(){
		var template = _.template($('#allProjectTemplate').html());
		json = this.model.toJSON();
		html = template(json);
		this.setElement(html);
		return this;
	},
	goToConfig_click: function(){
		json = this.model.toJSON();
		idProject = json['pk'];
	}
});