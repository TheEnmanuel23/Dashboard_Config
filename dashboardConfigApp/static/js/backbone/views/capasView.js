ConfigDashboard.Views.CapasView = Backbone.View.extend({
	el: 'body',
	events: {
		"click #readImageLoaded" : 'readImageData'
	},
	render: function(){
		self = this;
		var template = _.template($('#layers-description-template').html());
		var json = window.collections.capasCollections.toJSON();
		json.forEach(function(item){
			var html = template(item);
			self.$el.find('#layers-description-table-body').append(html);
		})
		return this;
	},
	readImageData: function(){
		var getAllPathElement = $("svg").find("path");
		getAllPathElement.each(function(){
			window.collections.capasCollections.add({
				'id': $(this).attr("id"),
				'descripcion': ''
			});
		});
		this.render();
	},
});