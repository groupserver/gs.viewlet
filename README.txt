==============
``gs.viewlet``
==============
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Viewlet support for GroupServer
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Author: `Michael JasonSmith`_
:Contact: Michael JasonSmith <mpj17@onlinegroups.net>
:Date: 2013-07-25
:Organization: `GroupServer.org`_
:Copyright: This document is licensed under a
  `Creative Commons Attribution-Share Alike 3.0 New Zealand License`_
  by `OnlineGroups.Net`_.

Introduction
============

Viewlets [#viewlets]_ are heavily used in GroupServer_ to decompose complex
pages. This product provides three classes that make viewlets more useful
in GroupServer:

#. The SiteContentProvider_ provides the base code.
#. The SiteViewlet_ provides the viewlet.
#. The WeightOrderedViewletManager_ provides a useful class for organising
   viewlet.

``SiteContentProvider``
=======================

The class ``gs.viewlet.SiteContentProvider`` provides an abstract base
class for content providers [#contentprovider]_ on GroupServer. It defines
two attributes: ``siteInfo`` and ``loggedInUser``. The ``update`` and
``render`` methods must be provided by the concrete classes. The
SiteViewlet_ is one such concrete class.


``SiteViewlet``
===============

The class ``gs.viewlet.SiteViewlet`` provides a useful base-class for
viewlets in GroupServer. This class defines the ``siteInfo`` and
``loggedInUser``. Unlike the content provider, the viewlet is a concrete
class::

  <browser:viewlet 
    name="gs-site-change-base-adminstuff-adminlinks"
    manager=".interfaces.ISiteAdminStuff"
    template="browser/templates/adminlinks.pt"
    class="gs.viewlet.SiteViewlet"
    permission="zope2.ManageProperties"
    weight="1"
    title="Links" />

``WeightOrderedViewletManager``
===============================

The ``gs.viewlet.WeightOrderedViewletManager`` class is a backport of the
weighted order viewlet manager to allow it to work under Zope2::

  <browser:viewletManager
    name="groupserver.SiteHomeMetadata"
    for="Products.GSContent.interfaces.IGSSiteFolder"
    provides=".interfaces.ISiteHomeMetadata"
    class="gs.viewlet.manager.WeightOrderedViewletManager"
    template="browser/templates/simplemanager.pt" 
    permission="zope2.View" />
  
It is often used in conjunction with a simple page-template that renders
each of the viewlets and provides no additional markup::

  <tal:block repeat="viewlet options/viewlets">
    <tal:block content="structure viewlet/render">Script Content</tal:block>
  </tal:block>


Resources
=========

- Code repository: https://source.iopen.net/groupserver/gs.viewlet/
- Questions and comments to http://groupserver.org/groups/development/
- Report bugs at https://redmine.iopen.net/projects/groupserver/

.. _GroupServer: http://groupserver.org/
.. _GroupServer.org: http://groupserver.org/
.. _OnlineGroups.Net: https://onlinegroups.net/
.. _Michael JasonSmith: http://groupserver.org/p/mpj17/
.. _Creative Commons Attribution-Share Alike 3.0 New Zealand License:
   http://creativecommons.org/licenses/by-sa/3.0/nz/

.. [#viewlets] For more information on viewlets see
               <http://docs.zope.org/zope.viewlet/>

.. [#contentprovider] For more information on content providers see
                      <http://docs.zope.org/zope.contentprovider/>

..  LocalWords:  Viewlets viewlets groupserver http SiteContentProvider
..  LocalWords:  SiteViewlet WieghtOrderdviewletManager siteInfo
..  LocalWords:  WeightOrderedViewletManager loggedInUser
