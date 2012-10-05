# coding=utf-8
import os
from setuptools import setup, find_packages
from version import get_version

version = get_version()

setup(name='gs.viewlet',
    version=version,
    description="A bug-fixed viewlet manager.",
    long_description=open("README.txt").read() + "\n" +
                      open(os.path.join("docs", "HISTORY.txt")).read(),
    classifiers=[
      "Development Status :: 4 - Beta",
      "Environment :: Web Environment",
      "Framework :: Zope2",
      "Intended Audience :: Developers",
      "License :: Other/Proprietary License",
      "Natural Language :: English",
      "Operating System :: POSIX :: Linux"
      "Programming Language :: Python",
      "Topic :: Software Development :: Libraries :: Python Modules",
      ],
    keywords='group membership group groupserver',
    author='Michael JasonSmith',
    author_email='mpj17@onlinegroups.net',
    url='http://groupserver.org/',
    license='other',
    packages=find_packages(exclude=['ez_setup']),
    namespace_packages=['gs',],
    include_package_data=True,
    zip_safe=True,
    install_requires=[
        'setuptools',
        'zope.cachedescriptors',
        'zope.component',
        'zope.contentprovider',
        'zope.event',
        'zope.location',
        'zope.viewlet',
        'Products.GSContent',  # For the site info
        'Products.CustomUserFolder',  # For the logged in user
        # -*- Extra requirements: -*-
    ],
    entry_points="""
    # -*- Entry points: -*-
    """,)

