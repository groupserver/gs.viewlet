# -*- coding: utf-8 -*-
from contentprovider import SiteContentProvider


class SiteViewlet(SiteContentProvider):
    def __init__(self, context, request, view, manager):
        SiteContentProvider.__init__(self, context, request, view)
        self.manager = manager
