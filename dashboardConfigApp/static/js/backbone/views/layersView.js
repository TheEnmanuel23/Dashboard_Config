ConfigDashboard.Views.LayersView = Backbone.View.extend({
    el: 'body',
    events: {
        'click .add-layer': 'addLayer_click',
    },
    initialize: function(){
        this.model.on('add', this.addLayerToCollection);
    },
    addLayer_click: function(ev){
        ev.preventDefault();
		jQuery.validator.messages.required = ""
		if($('#form-layer-selected').valid()) {
            if ($('#form-layer-selected').valid()) {
                var count = parseInt($('#layersForm tbody').children().length);
                var idCapa = $('#txtCodigoCapa').val()
                var descripcion = $('#txtDescripcionCapa').val()
                this.model.add({
                    id: count,
                    idCapa: idCapa,
                    descripcion: descripcion
                });
                $('#id_capa_set-TOTAL_FORMS').attr('value', count + 1);
                this.addClassLayerAdded(idCapa);
            }
        }
    },
	addClassLayerAdded: function(id){
		$('#' + id).addClass('added-layer');
	},
    render: function(){
        console.log("hola backbobe que hay de nuevo.");
    },
    addLayerToCollection: function (layer) {
        if(layer.view == null) {
            layer.view = new ConfigDashboard.Views.LayerViewSingle({
                model: layer
            });
        }
        layer.view.render();
        layer.view.$el.appendTo('#layersForm tbody');
    }
});

ConfigDashboard.Views.LayerViewSingle = Backbone.View.extend({
    render: function () {
        var template = _.template($('#layer-template').html());
        var html = template(this.model.toJSON());
        this.setElement(html);
        return this;
    }
});

ConfigDashboard.Views.LayersViewLoaded = Backbone.View.extend({
    initialize: function(){
        this.model.on('add', this.addLayer)
    },
    addLayer: function(layer){
        if(layer.view == null){
            layer.view = new ConfigDashboard.Views.LayerViewSingleLoaded({
                model: layer
            });
        }
        layer.view.render();
        layer.view.$el.appendTo('#container_data_layer_loaded');
    }
});

ConfigDashboard.Views.LayerViewSingleLoaded = Backbone.View.extend({
    render: function(){
        var template = _.template($('#layerLoadedTemplate').html());
        var html = template(this.model.toJSON());
        this.setElement(html);
        return this;
    }
});