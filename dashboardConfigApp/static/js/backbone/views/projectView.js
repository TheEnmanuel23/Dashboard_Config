ConfigDashboard.Views.ProjectView = Backbone.View.extend({	
	render: function(){
		var data = this.model.toJSON();
		template = _.template($('#allProjectTemplate').html() )
		var html = template(data);
		this.setElement(html);
	}
});