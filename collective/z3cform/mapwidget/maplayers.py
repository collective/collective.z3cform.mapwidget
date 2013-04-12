from collective.geo.mapwidget.browser.widget import MapWidget
from collective.geo.mapwidget.maplayers import MapLayer


class ShapeMapDisplayWidget(MapWidget):

    klass = 'widget-cgmap'
    mapid = 'geoshapedisplaymap'
    _layers = ['shapedisplay']

    @property
    def js(self):
        layer_name = u'%s - %s' % (self.context.Title().decode('utf-8'),
                                   unicode(self.view.label))
        return """
    (function($) {

    $(window).bind("map-load", function(e, map) {
       var layers = map.getLayersByName("%(layer_name)s");
       if (layers && layers[0].features) {
           map.zoomToExtent(layers[0].getDataExtent());
       }
    });

    })(jQuery);
    """ % {
            'mapid': self.mapid,
            'layer_name': layer_name
        }


class ShapeDisplayLayer(MapLayer):

    name = 'shapedisplay'

    @property
    def jsfactory(self):
        layer_name = u'%s - %s' % (self.context.Title().decode('utf-8'),
                                   unicode(self.widget.view.label))
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
             """ % {
            'coords': self.widget.view.value,
            'layer_name': layer_name
        }
        return js
