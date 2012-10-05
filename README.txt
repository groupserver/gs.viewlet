===============
Viewlet Support
===============

Viewlets are heavily used in GroupServer to decompose the complexity of a
page. This product provides three classes related to viewlets to make them
easy to use with GroupServer.

``SiteContentProvider``
=======================

The class ``gs.viewlet.contentprovider.SiteContentProvider`` provides an
abstract base class for content providers on GroupServer. It defines two
attributes: ``siteInfo`` and ``loggedInUser``. The ``update`` and
``render`` methods must be provided by the concrete classes.


``SiteViewlet``
===============

The class ``gs.viewlet.SiteViewlet`` provides a useful base-class for
viewlets in GroupServer. This class defines the ``siteInfo`` and
``loggedInUser``. Unlike the content provider, the viewlet is a concrete
class.

``WeightOrderedViewletManager``
===============================

The ``gs.viewlet.WeightOrderedViewletManager`` class is a backport of the
weighted order viewlet manager to allow it to work under Five.
