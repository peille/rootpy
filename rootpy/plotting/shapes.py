import ROOT
from ..core import camelCaseMethods
from .core import Plottable

@camelCaseMethods
class Ellipse(Plottable, ROOT.TEllipse):

    def __init__(self, *args, **kwargs):

        ROOT.TEllipse.__init__(self, *args)
        Plottable.__init__(self)
        self.decorate(**kwargs)
