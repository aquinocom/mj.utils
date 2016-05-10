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


class EstatisticasPublicasSinespTipoForm(BrowserView):
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

        self.dados = []
        self.anos = []
        self.uf = []

        id_content = self.context.id
        if id_content == 'estupro':
            self.tipo = "Estupro"
        if id_content == 'furto-de-veiculo':
            self.tipo = "Furto de Veiculo"
        if id_content == 'homicidio-doloso':
            self.tipo = "Homicidio Doloso"
        if id_content == 'lesao-corporal-seguida-de-morte':
            self.tipo = "Lesão Corporal Seguida de Morte"
        if id_content == 'roubo-seguido-de-morte-latrocinio':
            self.tipo = "Roubo Seguido de Morte (Latrocinio)"
        if id_content == 'roubo-de-veiculo':
            self.tipo = "Roubo de Veículo"

    def __call__(self):

        self.getInfo()

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
            return {'total_registro': total_registro, 'total_taxa': total_taxa, 'total_universo': total_universo}
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
    def grafico(self):
        lista = []
        if self.anos:
            for ano in self.anos:
                total = self.getTotal(ano)
                lista.append([int(ano), float(total['total_taxa'])])
        return lista

    @memoize
    def getItem(self, uf, ano):
        """
        """
        for i in self.dados:
            if (i['uf'] == uf) and (i['ano'] == ano):
                return i

    @memoize
    def getNumOcorrencia(self):
        """
        """
        estados = {
            'AC': 'ACRE',
            'AL': 'ALAGOAS',
            'AM': 'AMAZONAS',
            'AP': 'AMAPÁ',
            'BA': 'BAHIA',
            'CE': 'CEARÁ',
            'DF': 'DISTRITO FEDERAL',
            'ES': 'ESPÍRITO SANTO',
            'GO': 'GOIÁS',
            'MA': 'MARANHÃO',
            'MG': 'MINAS GERAIS',
            'MS': 'MATO GROSSO DO SUL',
            'MT': 'MATO GROSSO',
            'PA': 'PARÁ',
            'PB': 'PARAÍBA',
            'PE': 'PERNAMBUCO',
            'PI': 'PIAUÍ',
            'PR': 'PARANÁ',
            'RJ': 'RIO DE JANEIRO',
            'RN': 'RIO GRANDE DO NORTE',
            'RO': 'RONDÔNIA',
            'RR': 'RORAIMA',
            'RS': 'RIO GRANDE DO SUL',
            'SC': 'SANTA CATARINA',
            'SE': 'SERGIPE',
            'SP': 'SÃO PAULO',
            'TO': 'TOCANTINS',
        }
        items = []
        if self.dados:
            anos = self.anos
            if anos:
                ano = anos[-1]
                for i in self.dados:
                    if i['ano'] == ano:
                        i['uf'] = estados[i['uf']]
                        items.append(i)
        return items

    @memoize
    def getDadosMapa(self):
        """
        """
        estados = {
            'AC': 'ACRE',
            'AL': 'ALAGOAS',
            'AM': 'AMAZONAS',
            'AP': 'AMAPÁ',
            'BA': 'BAHIA',
            'CE': 'CEARÁ',
            'DF': 'DISTRITO FEDERAL',
            'ES': 'ESPÍRITO SANTO',
            'GO': 'GOIÁS',
            'MA': 'MARANHÃO',
            'MG': 'MINAS GERAIS',
            'MS': 'MATO GROSSO DO SUL',
            'MT': 'MATO GROSSO',
            'PA': 'PARÁ',
            'PB': 'PARAÍBA',
            'PE': 'PERNAMBUCO',
            'PI': 'PIAUÍ',
            'PR': 'PARANÁ',
            'RJ': 'RIO DE JANEIRO',
            'RN': 'RIO GRANDE DO NORTE',
            'RO': 'RONDÔNIA',
            'RR': 'RORAIMA',
            'RS': 'RIO GRANDE DO SUL',
            'SC': 'SANTA CATARINA',
            'SE': 'SERGIPE',
            'SP': 'SÃO PAULO',
            'TO': 'TOCANTINS',
        }
        items = ''
        if self.dados:
            anos = self.anos
            if anos:
                ano = anos[-1]
                items += '['
                for i in self.dados:
                    if i['ano'] == ano:
                        if i['taxa'] == 'NI':
                            taxa = '0'
                        else:
                            taxa = i['taxa']
                        items += '{uf: "' + str(i['uf']) + \
                                 '", texto: "' + str(estados[i['uf']]) + \
                                 '", qtd_ocorrencias: "' + str(i['qtd_ocorrencias']) + \
                                 '", universo: "' + str(i['universo']) + \
                                 '", taxa:' + str(taxa) + '},'
                items += ']'
        items.replace("},]", "}]")

        return items

    @memoize
    def getEscalaMapa(self):
        """
        """
        items = []
        if self.dados:
            anos = self.anos
            if anos:
                ano = anos[-1]
                for i in self.dados:
                    if i['ano'] == ano:
                        if i['taxa'] == 'NI':
                            items.append(float(0))
                        else:
                            items.append(float(i['taxa']))
        if items:
            items.sort()
            intervalo = '[' + str(items[0]) + ',' + str(items[-1]) + ']'
            return intervalo
        return items


    @memoize
    def site_url(self):
        portal_state = getMultiAdapter((self.context, self.request), name=u'plone_portal_state')
        site_url = portal_state.portal_url()
        return site_url
