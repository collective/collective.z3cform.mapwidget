from zope.component import adapter
from zope.interface import implementer
from zope.interface import implementsOnly
from zope.schema.interfaces import IField

import z3c.form.interfaces
from z3c.form.interfaces import IFormLayer
from z3c.form.interfaces import IFieldWidget
from z3c.form.interfaces import ITextAreaWidget

from z3c.form.browser.textarea import TextAreaWidget
from z3c.form.widget import FieldWidget
from z3c.form.interfaces import DISPLAY_MODE

from collective.geo.mapwidget.browser import widget


class MapWidget(widget.MapWidget):
    js = None

    @property
    def mapid(self):
        return "%s-map" % self.view.name.replace('.', '-')

    def coords(self):
        return self.view.value


class MapDisplayWidget(MapWidget):
    _layers = ['shapedisplay']


class IFormMapWidget(ITextAreaWidget):
    """Interface for z3c.form map widget"""
    pass


class FormMapWidget(TextAreaWidget):
    implementsOnly(IFormMapWidget)

    @property
    def cgmap(self):
        if self.mode == DISPLAY_MODE:
            return MapDisplayWidget(self, self.request, self.context)
        return MapWidget(self, self.request, self.context)


@adapter(IField, IFormLayer)
@implementer(IFieldWidget)
def MapFieldWidget(field, request):
    """IFieldWidget factory for FormMapWidget."""
    return FieldWidget(field, FormMapWidget(request))
