# coding=utf-8
from zope.component import getAdapters
try:
    from zope.contentprovider.interfaces import BeforeUpdateEvent
except ImportError, e:
    zope213 = False
else:
    zope213 = True    
from zope.event import notify
from zope.location.interfaces import ILocation
from zope.viewlet import interfaces
from Products.Five.viewlet.manager import ViewletManagerBase

class aWeightOrderedViewletManager(ViewletManagerBase):
    def filter_out_no_shows(self, viewlets):
        # filter for permission
        allowed = [v for v in self.filter(viewlets)]
        retval = []
        # we show a viewlet if the show attribute allows us, or if it
        # doesn't have one
        for viewlet in allowed:
            try:
                if viewlet.show:
                    retval.append(viewlet)
            except AttributeError:
                retval.append(viewlet)
        
        return retval

    def update(self):
        """See zope.contentprovider.interfaces.IContentProvider"""
        #--=mpj17=-- Stolen from zope.viewlet.manager
        self.__updated = True
        # Find all content providers for the region
        viewlets = getAdapters(
            (self.context, self.request, self.__parent__, self),
            interfaces.IViewlet)
        viewlets = self.filter_out_no_shows(viewlets)
        
        # --=mpj17=-- This is the main change to the standard viewlet 
        #       manager: the viewlets are sorted according to the
        #       "weight" attribute
        viewlets.sort(key=lambda v: int(v[1].weight))

        self.viewlets=[]
        for name, viewlet in viewlets:
            if ILocation.providedBy(viewlet):
                viewlet.__name__ = name
            self.viewlets.append(viewlet)
            # --=mpj17=-- Don't call _updateViewlets, because it does
            #       not exist in Zope 2.10
            if zope213:
                notify(BeforeUpdateEvent(viewlet, self.request))
            viewlet.update()

WeightOrderedViewletManager = aWeightOrderedViewletManager

