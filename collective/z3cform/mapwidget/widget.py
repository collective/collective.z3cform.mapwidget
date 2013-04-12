# import Acquisition
import zope.interface
import zope.schema.interfaces
from zope.component import getMultiAdapter

# from zope.app.component.hooks import getSite

import z3c.form.interfaces
import z3c.form.browser.textarea
import z3c.form.widget
from z3c.form.interfaces import DISPLAY_MODE
from collective.geo.mapwidget.interfaces import IMaps, IMapView


class IMapWidget(z3c.form.interfaces.ITextAreaWidget, IMapView):
    pass


class MapWidget(z3c.form.browser.textarea.TextAreaWidget):
    zope.interface.implementsOnly(IMapWidget)

    klass = u'map-widget'
    mapfields = ['geoshapemap']

    @property
    def map_id(self):
        return "%s-map" % self.name.replace('.', '-')

    # def cgmap(self):
    #     mapwidget = getMultiAdapter(
    #         (self, self.request, self.context),
    #         IMaps
    #     )[0]
    #     mapwidget.mapid = self.map_id
    #     return mapwidget


@zope.component.adapter(zope.schema.interfaces.IField,
                        z3c.form.interfaces.IFormLayer)
@zope.interface.implementer(z3c.form.interfaces.IFieldWidget)
def MapFieldWidget(field, request):
    """IFieldWidget factory for MapWidget."""
    return z3c.form.widget.FieldWidget(field, MapWidget(request))
