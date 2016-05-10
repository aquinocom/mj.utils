# -*- coding: utf-8 -*-
from mj.utils.interfaces.interfaces import IPDFConverter, IPDFHTMLProvider
import os
from StringIO import StringIO
import pdfkit
from base64 import b64encode
from pdfkit.pdfkit import PDFKit
from zope.interface import implements

_orig_command = PDFKit.command


def command(self, path=None):
    args = _orig_command(self, path)
    auth = os.environ.get('WKHTMLTOPDF_HTTPAUTH', None)
    if auth:
        username, password = auth.strip().split(':', 1)
        args.insert(1, 'Basic %s' % b64encode(auth.strip()))
        args.insert(1, 'Authorization')
        args.insert(1, '--custom-header')
    return args

PDFKit.command = command


class PDFKitPDFConverter(object):
    implements(IPDFConverter)

    def __init__(self):
        path = os.environ.get('WKHTMLTOPDF_PATH', None)
        if path:
            config = pdfkit.configuration(wkhtmltopdf=path)
        else:
            config = pdfkit.configuration()
        self.config = config

    def _options(self):
        #import pdb; pdb.set_trace()
        opts = {
            '--print-media-type': None,
            '--disable-javascript': None,
            '--quiet': None,
            '--page-size': 'A4',
            '--margin-left': '10mm',
            '--margin-right': '10mm',
            '--margin-top': '10mm',
            '--header-spacing': '20',
            '--proxy': 'http://proxy.tse.jus.br:8080',
        }

        return opts

    def convert(self, content, view=None):
        item = IPDFHTMLProvider(content)
        html = item.pdf_html(view=view)
        try:
            css = os.path.dirname(os.path.abspath(__file__)) + '/browser/css/pdf.css'

            out = pdfkit.from_string(
                html,
                False,
                options=self._options(),
                configuration=self.config,
                css=css,
            )
        except IOError:
            # pt = getToolByName(content, 'portal_transforms')
            # texto = content.getText()
            # texto_puro = pt.convertTo('text/plain', texto, mimetype='text/html').getData().strip()
            html = '<!DOCTYPE html>' \
                   '<html xmlns="http://www.w3.org/1999/xhtml" lang="pt-br">' \
                   '    <head>' \
                   '        <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />' \
                   '    </head>' \
                   '    <body>' \
                   '        <h1>Erro ao gerar o PDF.</h1>' \
                   '        <p>Existe conteúdo externo na página.</p>' \
                   '    </body>' \
                   '</html>'
            out = pdfkit.from_string(html,
                False,
                options=self._options(),
                configuration=self.config
            )
        return StringIO(out)
