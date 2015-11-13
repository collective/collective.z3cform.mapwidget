from zope.interface import implementer
from zope.schema import Text
from zope.schema.interfaces import IText


class IWKT(IText):
    pass


@implementer(IWKT)
class WKT(Text):
    pass
