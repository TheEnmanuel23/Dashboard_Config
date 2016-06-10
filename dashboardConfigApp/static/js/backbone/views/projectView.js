ConfigDashboard.Views.ProjectView = Backbone.View.extend({
	initialize: function(){
		this.model.on('add', this.render);
		self = this;
	},
	template: _.template($('#allProjectTemplate').html()),
	render: function(){
		$('#allProject_table_tbody').empty();
		var data = self.model.toJSON();
		data.forEach(function(item){
			var html = self.template(item);
			self.setElement(html);
			self.$el.appendTo('#allProject_table_tbody');
		})
	},
});