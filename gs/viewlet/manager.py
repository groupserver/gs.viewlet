# coding=utf-8
import zope.component
from zope.viewlet import interfaces
from zope.location.interfaces import ILocation
from Products.Five.viewlet.manager import ViewletManagerBase

class aWeightOrderedViewletManager(ViewletManagerBase):
    def update(self):
        """See zope.contentprovider.interfaces.IContentProvider"""
        #--=mpj17=-- Stolen from zope.viewlet.manager
        self.__updated = True
        # Find all content providers for the region
        viewlets = zope.component.getAdapters(
            (self.context, self.request, self.__parent__, self),
            interfaces.IViewlet)
        viewlets = self.filter(viewlets)
        viewlets = [v for v in viewlets if getattr(v[1], 'show', True)]
        
        # --=mpj17=-- This is the main change to the standard viewlet 
        #       manager: the viewlets are sorted according to the
        #       "weight" attribute
        viewlets.sort(key=lambda v: int(v[1].weight))

        # Just use the viewlets from now on
        self.viewlets=[]
        for name, viewlet in viewlets:
            if ILocation.providedBy(viewlet):
                viewlet.__name__ = name
            self.viewlets.append(viewlet)
        self._updateViewlets()

WeightOrderedViewletManager = aWeightOrderedViewletManager

