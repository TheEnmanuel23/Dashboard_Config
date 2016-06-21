ConfigDashboard.Views.App = Backbone.View.extend({
	el: $('body'),
	events: {
		'change #btnOpenFile': 'loadImageIntoContainer',
		'click .add-layer': 'addLayer',
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
	addLayer: function(ev){
		ev.preventDefault();
		var count = $('#layersForm tbody').children().length;
		var template = _.template($('#layer-template').html());
		jQuery.validator.messages.required = ""
		var idCapa = $('#txtCodigoCapa').val()
		var descripcion = $('#txtDescripcionCapa').val()
		var html = template({id: count, idCapa: idCapa, descripcion: descripcion});
		$('#layersForm tbody').append(html);
		$('#id_capa_set-TOTAL_FORMS').attr('value', count + 1);
		this.addClassLayerAdded(idCapa);
	},
	clickLayerToAdd: function(sender){
		var $path= $(sender.currentTarget);
		var idRegion = $path.attr('id');
		$('#txtCodigoCapa').val(idRegion)
	},
	addClassLayerAdded: function(id){
		$('#' + id).addClass('added-layer');
		$('#' + id).attr('disabled','disabled');
		$('#' + id).off('click');
	}
});