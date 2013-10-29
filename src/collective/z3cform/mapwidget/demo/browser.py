import logging
from zope import schema

from zope.interface import Interface

from z3c.form import form, field, button
from plone.z3cform.layout import wrap_form

from ..widget import MapFieldWidget

logger = logging.getLogger(__name__)


class IForm(Interface):

    coordinates = schema.Text(
        title=u"Coordinates",
        required=False,
    )

    coordinates2 = schema.Text(
        title=u"Coordinates 2",
        required=False,
    )


class Form(form.Form):
    ignoreContext = True
    fields = field.Fields(IForm)
    fields['coordinates'].widgetFactory = MapFieldWidget
    fields['coordinates2'].widgetFactory = MapFieldWidget

    def __init__(self, context, request):
        super(Form, self).__init__(context, request)
        self.request.set('disable_border', True)

    @button.buttonAndHandler(u'Send')
    def handleSend(self, action):  # pylint: disable=W0613

        data, errors = self.extractData()
        if errors:
            self.status = self.formErrorsMessage
            return

        logger.info(data)


DemoForm = wrap_form(Form)
