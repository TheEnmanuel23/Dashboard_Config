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

ConfigDashboard.Views.LayersViewNoSaved = Backbone.View.extend({
    initialize: function () {
        this.model.on('add', this.addRowLayerNoSaved);
    },
    addRowLayerNoSaved: function (layer) {
        if(layer.view == null){
            layer.view = new ConfigDashboard.Views.LayerViewSingleNoSaved({
                model: layer
            });
        }
        layer.view.render();
        layer.view.$el.appendTo('#container_data_layer_no-save');
    }
});
ConfigDashboard.Views.LayerViewSingleNoSaved = Backbone.View.extend({
    render: function(){
        var template = _.template($('#layerNoSavedTemplate').html());
        var html = template(this.model.toJSON());
        this.setElement(html);
        return this;
    }
});