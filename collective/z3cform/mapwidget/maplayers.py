from collective.geo.mapwidget.browser.widget import MapWidget
from collective.geo.mapwidget.maplayers import MapLayer
from collective.geo.mapwidget.browser.widget import MapWidgets \
                                                as BaseMapWidgets


class MapWidgets(BaseMapWidgets):
    mapid = 'default-cgmap'
    klass = 'widget-cgmap'


class ShapeMapWidget(MapWidget):

    klass = 'widget-cgmap'
    mapid = 'geoshapemap'
    _layers = ['shapeedit']

    @property
    def js(self):
        return """
  jq(function(){
    var map = cgmap.config['geoshapemap'].map;
    var layer = map.getLayersByName('Edit')[0];
    var elctl = new OpenLayers.Control.WKTEditingToolbar(layer, {wktid: '%s'});
    map.addControl(elctl);
    elctl.activate();
   });
        """ % self.view.id


class ShapeEditLayer(MapLayer):

    name = 'shapeedit'

    jsfactory = """
    function(){return new OpenLayers.Layer.Vector('Edit');}
    """
