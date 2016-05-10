# -*- coding: utf-8 -*-
from zope.interface import implements
from mj.utils.interfaces.interfaces import IPDFHTMLProvider


class DefaultPDF(object):
    implements(IPDFHTMLProvider)

    def __init__(self, context):
        """Constructor"""
        self.context = context

    def pdf_html(self, view=None):
        if view is None:
            return self.context()
        return self.context.restrictedTraverse(view)()