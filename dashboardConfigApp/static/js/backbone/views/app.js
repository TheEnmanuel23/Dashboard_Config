ConfigDashboard.Views.App = Backbone.View.extend({
	el: $('body'),
	events: {
		'change #btnOpenFile': 'loadImageIntoContainer',
	 	'click .containerImageSaved path': 'clickLayerToAdd',
	},
	initialize: function($el){
		this.$el = $el;
	},
	loadImageIntoContainer:  function(e){
		var workSpace = Snap("#containerImage");		
		if($('#btnOpenFile').val() != '') {
			$("#containerImage").empty();
			var url = URL.createObjectURL(e.target.files[0]);
			Snap.load(url, function ( data ) {
			   	workSpace.append(data);
			});
		}
	},
	clickLayerToAdd: function(sender){
		var $path= $(sender.currentTarget);
		var idRegion = $path.attr('id');
		$('#txtCodigoCapa').val(idRegion)
	}
});