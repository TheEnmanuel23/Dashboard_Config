ConfigDashboard.Views.App = Backbone.View.extend({
	el: $('body'),
	events: {
		'change #btnOpenFile': 'loadImageIntoContainer'
	},
	initialize: function($el){
		this.$el = $el;
	},
	loadImageIntoContainer:  function(e){
		var workSpace = Snap("#containerImage");		
		if($('#btnOpenFile').val() != '') {
			// $('#containerImage').empty();
			window.collections.capasCollections.reset();
			var url = URL.createObjectURL(e.target.files[0]);
			Snap.load(url, function ( data ) {
			   	workSpace.append(data);
			});
		}
	}
});