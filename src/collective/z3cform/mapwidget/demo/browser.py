import logging
from collective.z3cform.mapwidget import WKT
from plone.z3cform.layout import wrap_form
from z3c.form import form, field, button
from zope.interface import Interface

logger = logging.getLogger(__name__)

_POLYGON = u"""
POLYGON((-74.00631186393909 40.71412240911994,
    -74.00408026603894 40.713130276463545,
    -74.00473472503782 40.712544748613674,
    -74.00558230308663 40.712186923504554,
    -74.00652644065993 40.711894156075694,
    -74.00757786659322 40.71167457965925,
    -74.00787827400312 40.71172337448104,
    -74.00796410469125 40.71181283156121,
    -74.00808212188849 40.71199174536168,
    -74.00722381500333 40.713032688846255,
    -74.00631186393909 40.71412240911994))
"""


class IForm(Interface):

    coordinates = WKT(
        title=u"Coordinates",
        required=False,
        default=u"POINT(7.686856499999999 45.070312)"
    )

    coordinates2 = WKT(
        title=u"Coordinates 2",
        required=False,
        default=_POLYGON
    )


class Form(form.Form):
    ignoreContext = True
    fields = field.Fields(IForm)

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
