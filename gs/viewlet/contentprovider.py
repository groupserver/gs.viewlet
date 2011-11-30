# coding=utf-8
from zope.cachedescriptors.property import Lazy
from zope.component import createObject
from AccessControl import getSecurityManager

class SiteContentProvider(object):
    def __init__(self, context, request, view):
        self.__parent__ = self.view = view
        self.__updated = False
        self.context = context
        self.request = request

    @Lazy
    def siteInfo(self):
        retval = createObject('groupserver.SiteInfo', self.context)
        return retval

    @Lazy
    def loggedInUser(self):
        retval = createObject('groupserver.LoggedInUser', self.context)
        return retval

