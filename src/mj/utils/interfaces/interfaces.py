# -*- coding: utf-8 -*-
from zope.interface import Interface


class IPDFExportCapable(Interface):
    pass


class IPDFConverter(Interface):
    pass


class IPDFHTMLProvider(Interface):

    def pdf_html(view):
        """ get pdf html of current content """
