# -*- coding: utf-8 -*-

# Product imports
from Products.CMFCore.utils import getToolByName
from Products.Five.browser import BrowserView
from zope.component import getMultiAdapter
from mj.utils.interfaces.interfaces import IPDFExportCapable
from mj.utils.interfaces.interfaces import IPDFConverter
import xhtml2pdf.pisa as pisa
from StringIO import StringIO
from zope.component import getUtility


class PDFExportView(BrowserView):
    """
    """

    def __init__(self, context, request):
        self.context = context
        self.request = request
        self.errors = {}

        self.portal_state = getMultiAdapter((self.context, self.request), name=u'plone_portal_state')
        self.tools = getMultiAdapter((self.context, self.request), name=u'plone_tools')
        self.utils = getToolByName(self.context, 'plone_utils')

    def __call__(self):

        converter = getUtility(IPDFConverter)
        view = self.request.get('pdf-view', None)
        result = converter.convert(self.context, view=view)
        out = result.getvalue()
        self.request.response.setHeader('Content-Type', 'application/pdf')
        if not self.request.get('pdf-noattach', False):
            self.request.response.setHeader('Content-Disposition',
                'attachment; filename=%s.pdf' % self.context.getId())
        self.request.response.setHeader('Content-Length', len(out))
        return out