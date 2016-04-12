# -*- coding: utf-8 -*-

# Product imports
from Products.CMFCore.utils import getToolByName
from Products.Five.browser import BrowserView
from zope.component import getUtility
from plone.i18n.normalizer.interfaces import IIDNormalizer
from plone.memoize.instance import memoize
from zope.component import getMultiAdapter
from zope.site.hooks import getSite
from Products.CMFPlone.utils import _createObjectByType
from DateTime import DateTime
from openpyxl import load_workbook
import fpformat


class EstatisticasPublicasSinespForm(BrowserView):
    """
    """

    def __init__(self, context, request):
        self.context = context
        self.request = request
        self.errors = {}

        self.portal_state = getMultiAdapter((self.context, self.request), name=u'plone_portal_state')
        self.tools = getMultiAdapter((self.context, self.request), name=u'plone_tools')
        self.utils = getToolByName(self.context, 'plone_utils')
        self.catalog = getToolByName(self.context, 'portal_catalog')

        self.url_cancel = self.site_url() + '/import_sinesp'
        self.url_sucess = self.site_url() + '/import_sinesp'

        self.dados = []
        self.anos = []
        self.uf = []

        if 'tipo' in request.form:
            tipo = request.form['tipo']
            request.set('tipo', tipo)
            self.tipo = tipo
        else:
            request.set('tipo', None)
            self.tipo = None

    def __call__(self):

        if 'form.execute' in self.request.form:
            if self.validateForm():
                self.getInfo()

        if 'form.cancel' in self.request.form:
            msg = 'A operação de importação foi cancelada.'
            self.utils.addPortalMessage(msg, type='info')
            return self.request.response.redirect(self.url_cancel)

        return self.index()

    @memoize
    def getTipo(self):
        """
        """
        index = self.catalog._catalog.indexes['tipo']
        return index.uniqueValues()    

    @memoize
    def getAnos(self):
        """
        """
        index = self.catalog._catalog.indexes['ano']
        self.anos = [i for i in index.uniqueValues()]
        pass

    @memoize
    def getUF(self):
        """
        """
        index = self.catalog._catalog.indexes['uf']
        self.uf = index.uniqueValues()
        pass

    @memoize
    def getInfo(self):
        """
        """
        results = self.catalog(portal_type="sinesp",
                               tipo=self.tipo,
                               sort_on='uf',
                               sort_order='ascending')
        anos = self.getAnos()
        uf = self.getUF()
        
        if results:
            for i in results:
                dic = {
                    'tipo': i.tipo,
                    'uf': i.uf,
                    'ano': i.ano,
                    'qtd_ocorrencias': i.qtd_ocorrencias,
                    'taxa': '',
                    'universo': i.universo
                }
                try:
                    valor = float(i.taxa)
                    dic['taxa'] = fpformat.fix(valor, 2)
                except:
                    dic['taxa'] = i.taxa
                self.dados.append(dic)
        pass
                
    @memoize
    def getTotal(self, ano):
        """
        """
        if self.dados:
            total_universo = 0
            total_registro = 0
            total_taxa = 0
            for i in self.dados:
                if i['ano'] == ano:
                    try:
                        total_universo += int(i['universo'])
                        total_registro += int(i['qtd_ocorrencias'])
                    except:
                        pass
            if total_universo and total_registro:
                total_taxa = ((total_registro + .0) / (total_universo + .0)) * 100000
                total_taxa = fpformat.fix(total_taxa, 2)
            return {'total_registro': total_registro, 'total_taxa': total_taxa}
        else:
            return {}

    @memoize
    def getTaxas(self):
        """
        """
        taxas = []
        if self.dados:
            for ano in self.anos:
                total = self.getTotal(ano)
                taxas.append(float(total['total_taxa']))
        return taxas

    @memoize
    def getItem(self, uf, ano):
        """
        """
        for i in self.dados:
            if (i['uf'] == uf) and (i['ano'] == ano):
                return i
        
    @memoize
    def validateForm(self):
        """
        """
        if (self.tipo == '') or (self.tipo == None):
            self.errors['tipo'] = "O campo é obrigatório."
        # Check for errors
        if self.errors:
            self.utils.addPortalMessage("Corrija os erros.", type='error')
            return False
        else:
            return True
        
    @memoize
    def site_url(self):
        portal_state = getMultiAdapter((self.context, self.request), name=u'plone_portal_state')
        site_url = portal_state.portal_url()
        return site_url
