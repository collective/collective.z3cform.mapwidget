from collective.geo.mapwidget.browser.widget import MapWidget
from collective.geo.mapwidget.maplayers import MapLayer
from collective.geo.mapwidget.browser.widget import MapWidgets \
                                                as BaseMapWidgets


class MapWidgets(BaseMapWidgets):
    mapid = 'default-cgmap'
    klass = 'widget-cgmap'

class ShapeMapDisplayWidget(MapWidget):

    klass = 'widget-cgmap'
    mapid = 'geoshapedisplaymap'
    _layers = ['shapedisplay']

    @property
    def js(self):
        layer_name = '%s - %s' % (self.context.Title(),
                                  self.view.label)
        return """
    (function($) {

    $(window).bind("load", function() {
       var map = cgmap.config['%(mapid)s'].map;
       var layers = map.getLayersByName("%(layer_name)s");
       if (layers && layers[0].features) {
           map.zoomToExtent(layers[0].getDataExtent());
       }
    });

    })(jQuery);
    """ % dict(mapid=self.mapid, layer_name=layer_name)

class ShapeMapWidget(MapWidget):

    klass = 'widget-cgmap'
    mapid = 'geoshapemap'
    _layers = ['shapeedit']

    @property
    def js(self):
        return """
    (function($) {

    $(window).bind("load", function() {
       var map = cgmap.config['%(mapid)s'].map;
       var layer = map.getLayersByName('Edit')[0];
       var elctl = new OpenLayers.Control.WKTEditingToolbar(layer, {wktid: '%(wktid)s'});
       map.addControl(elctl);
       elctl.activate();
    });

    })(jQuery);
    """ % dict(mapid=self.mapid, wktid=self.view.id)

class ShapeDisplayLayer(MapLayer):

    name = 'shapedisplay'

    @property
    def jsfactory(self):
        layer_name = '%s - %s' % (self.context.Title(),
                                  self.widget.view.label)
        js = """
    function() { return (function(cgmap) {
        cg_default_options = cgmap.createDefaultOptions();
        var wkt = new OpenLayers.Format.WKT({
            internalProjection: cg_default_options.projection,
            externalProjection: cg_default_options.displayProjection
        });

        var features = wkt.read('%(coords)s') || [];
        wkt.destroy();
        if(features.constructor != Array) {
            features = [features];
        }

        var layer = new OpenLayers.Layer.Vector('%(layer_name)s');
        layer.addFeatures(features);
        return layer;
    })(cgmap);
    }
             """ % dict(coords=self.widget.view.value,
                        layer_name=layer_name
                       )
        return js


class ShapeEditLayer(MapLayer):

    name = 'shapeedit'

    jsfactory = """
    function(){return new OpenLayers.Layer.Vector('Edit');}
    """
