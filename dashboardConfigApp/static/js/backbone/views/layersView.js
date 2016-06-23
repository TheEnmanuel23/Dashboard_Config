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
        this.setElement(setTemplateRow(this, 'layerLoadedTemplate'));
        return this;
    }
});

ConfigDashboard.Views.LayersViewNoSaved = Backbone.View.extend({
    initialize: function () {
        this.model.on('add', this.addRowLayerNoSaved);
        this.model.on('remove', this.removeRowLayerNoSaved);
    },
    addRowLayerNoSaved: function (layer) {
        if(layer.view == null){
            layer.view = new ConfigDashboard.Views.LayerViewSingleNoSaved({
                model: layer
            });
        }
        layer.view.render();
        layer.view.$el.appendTo('#container_data_layer_no-save');
    },
    removeRowLayerNoSaved: function(layer){
        if(layer.view != null){
            layer.view.remove();
        }
        layer.clear();
    }
});
ConfigDashboard.Views.LayerViewSingleNoSaved = Backbone.View.extend({
    events: {
        'click #removePathRow': 'remove_path_click'
    },
    remove_path_click: function(e){
        e.preventDefault();
        this.model.collection.remove(this.model);
    },
    render: function(){
        this.setElement(setTemplateRow(this, 'layerNoSavedTemplate'))
        return this;
    }
});

function setTemplateRow(self, templatName){
  var template = _.template($('#' + templatName).html());
  var html = template(self.model.toJSON());
  return html;
}