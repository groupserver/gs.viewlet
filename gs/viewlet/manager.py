# coding=utf-8
from zope.component import getAdapters
from zope.contentprovider.interfaces import BeforeUpdateEvent
from zope.event import notify
from zope.location.interfaces import ILocation
from zope.viewlet import interfaces
from Products.Five.viewlet.manager import ViewletManagerBase

class aWeightOrderedViewletManager(ViewletManagerBase):
    def filter_out_no_shows(self, viewlets):
        # --=mpj17=-- The reason I do not call
        # viewlets = super(ViewletManagerBase, self).filter(viewlets)
        # is I get a "ForbiddenAttribute: ('render'" when I try. I can
        # call the "filter" method from the parent class, but not using 
        # "super."
        viewlets = [v for v in self.filter(viewlets) 
                    if getattr(v[1], 'show', True)]
        return viewlets

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
            notify(BeforeUpdateEvent(viewlet, self.request))
            viewlet.update()

WeightOrderedViewletManager = aWeightOrderedViewletManager

