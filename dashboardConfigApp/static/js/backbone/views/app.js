ConfigDashboard.Views.App = Backbone.View.extend({
	el: $('body'),
	events: {
		'change #btnOpenFile': 'loadImageIntoContainer',
		'click .add-book': 'addLayer',
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
		var html = template({ id : count });
		$('#layersForm tbody').append(html);
		$('#id_capa_set-TOTAL_FORMS').attr('value', count+1);
	}
});