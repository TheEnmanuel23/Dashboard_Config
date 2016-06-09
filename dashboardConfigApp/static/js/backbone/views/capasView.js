ConfigDashboard.Views.CapasView = Backbone.View.extend({
	el: "body",
	initialize: function(){
		this.model.on("add", this.render)
	},
	render: function(){
		var $tbody = $('#layers-description-table-body');
		$tbody.empty();
		
	},
	events: {
		"click #readImageLoaded" : 'readImageData'
	},
	readImageData: function(){
		var getAllPathElement = $("svg").find("path");
		getAllPathElement.each(function(){
			window.collections.capasCollections.add({
				id: $(this).attr("id"),
				descripcion: ''
			});
		});
	},
});