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
        $('#container-image-to-map').empty();
        $('#container_data_layer_no-save').empty();
		this.fillArrayPath();
		this.setAllLayers();
	},
	setAllLayers:function(){
		var idImage = $('#txtIdImageLoaded').val();
        $('#container_data_layer_loaded').empty();
		window.arrayPathToAdd = []
		window.collections.layersLoaded = new ConfigDashboard.Collections.LayersLoaded();
		window.views.layersOfImageLoaded = new ConfigDashboard.Views.LayersViewLoaded({
			model: window.collections.layersLoaded
		});
		var layersLoaded = window.collections.layersLoaded.fetch({
			data : {
				image: idImage,
				format: 'json'
			}
		});
		layersLoaded.then(this.configLayersNoSaved);
	},
	configLayersNoSaved: function(){
		var arrayPathToAdd = [];
		for(i = 0; i < window.arrayPath.length; i++){
			path = window.arrayPath[i];
			layer = window.collections.layersLoaded.find({idCapa : path});
			if(layer == null){
				arrayPathToAdd.push(path);
			}
		}
		window.collections.layerNoSaved = new ConfigDashboard.Collections.LayersNoSaved();
		window.views.layerNoSaved = new ConfigDashboard.Views.LayersViewNoSaved({
			model : window.collections.layerNoSaved
		});
		for(i = 0; i < arrayPathToAdd.length; i++){
			path = arrayPathToAdd[i];
			var count = parseInt($('#container_data_layer_no-save').children().length);
			window.collections.layerNoSaved.add([{
				id : count,
				path : path,
				descripcion : ''
			}]);
			$('#id_capa_set-TOTAL_FORMS').attr('value', count + 1);
		}
	},
	fillArrayPath: function(){
	  	var workSpace = Snap("#container-image-to-map");
		var url = $('#txtUrlImage').val();
		window.arrayPath = [];

		Snap.load(url, function ( data ) {
			workSpace.append( data );
			$("#container-image-to-map path").each(function(){
				path = $(this).attr('id');
				arrayPath.push(path);
			});
		});
	},
});