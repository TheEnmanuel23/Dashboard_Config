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
		this.loadLayerImageSaved();
		this.loadLayerImageNoSaved();
	},
	loadLayerImageSaved:function(){
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
	},
	loadLayerImageNoSaved: function(){
		window.collections.layerNoSaved = new ConfigDashboard.Collections.LayersNoSaved();
		window.views.layerNoSaved = new ConfigDashboard.Views.LayersViewNoSaved({
			model : window.collections.layerNoSaved
		});

        $('#container-image-to-map').empty();
        $('#container_data_layer_no-save').empty();
	  	var workSpace = Snap("#container-image-to-map");
		var url = $('#txtUrlImage').val();
		Snap.load(url, function ( data ) {
			workSpace.append( data );
			$("#container-image-to-map path").each(function(){
				path = $(this).attr('id');
			  	var count = parseInt($('#container_data_layer_no-save').children().length);
				window.collections.layerNoSaved.add({
					id : count,
					path : path,
					descripcion : ''
				});
                $('#id_capa_set-TOTAL_FORMS').attr('value', count + 1);
			});
		});
	}
});