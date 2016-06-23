ConfigDashboard.Views.App = Backbone.View.extend({
	el: $('body'),
	events: {
		'change #btnOpenFile': 'loadImageIntoContainer',
	 	'click .containerImageSaved path': 'clickLayerToAdd',
		'click #btnLoadDataOfImage': 'btnClickLoadDataOfImage',
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
	},
	btnClickLoadDataOfImage: function(){
		var idProject = $('#txtIdProject').val();
		var idImage = $('#txtIdImageLoaded').val();
        $('#container_data_layer_loaded').empty();
		window.collections.layersLoaded = new ConfigDashboard.Collections.LayersLoaded();
		window.views.layersOfImageLoaded = new ConfigDashboard.Views.LayersViewLoaded({
				model: window.collections.layersLoaded
			});
		window.collections.layersLoaded.fetch({
			data : {
				image: idImage
			}
		});
	}
});