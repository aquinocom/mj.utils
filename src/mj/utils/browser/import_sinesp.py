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


class ImportSinespForm(BrowserView):
    """
    """

    def __init__(self, context, request):
        self.context = context
        self.request = request
        self.errors = {}

        self.portal_state = getMultiAdapter((self.context, self.request), name=u'plone_portal_state')
        self.tools = getMultiAdapter((self.context, self.request), name=u'plone_tools')
        self.utils = getToolByName(self.context, 'plone_utils')

        self.url_cancel = self.site_url() + '/import_sinesp'
        self.url_sucess = self.site_url() + '/import_sinesp'

        self.dados = []

        if 'file' in request.form:
            file_conteudo = request.form['file']
            request.set('file', file_conteudo)
            self.file_conteudo = file_conteudo

    def __call__(self):

        if self.portal_state.anonymous():
            self.request.set('came_from', self.url_classificados)
            return getSite().restrictedTraverse('login')()

        if 'form.execute' in self.request.form:
            if self.validateForm():
                return self.Importacao()

        if 'form.cancel' in self.request.form:
            msg = 'A operação de importação foi cancelada.'
            self.utils.addPortalMessage(msg, type='info')
            return self.request.response.redirect(self.url_cancel)

        return self.index()
    
    @memoize
    def validateForm(self):
        """
        """
        if self.file_conteudo.filename == '':
            self.errors['file'] = "O campo é obrigatório."
        # Check for errors
        if self.errors:
            self.utils.addPortalMessage("Corrija os erros.", type='error')
            return False
        else:
            return True

    @memoize
    def Importacao(self):
        """
        """
        wb = load_workbook(filename=self.file_conteudo)
        sheet = wb['CONSOLIDADO']
        lista = [i for i in sheet.rows][3:]
        for row in lista:
            #tipo do crime
            tipo = row[0].value

            #sigla da uf
            uf = row[1].value[:2]

            #ano/periodo
            ano = int(row[2].value)

            #quantidade de ocorrencia no ano
            try:
                qtd_ocorrencias = int(row[3].value)
            except:
                qtd_ocorrencias = row[3].value

            #taxa no ano
            try:
                taxa = float(row[4].value)
            except:
                taxa = row[4].value

            #populacao ou frota
            universo = int(row[5].value)

            dic = {
                'tipo': tipo,
                'uf': uf,
                'ano': ano,
                'qtd_ocorrencias': qtd_ocorrencias,
                'taxa': taxa,
                'universo': universo
            }
            self.dados.append(dic)

        if not self.AddContents():
            msg = 'Ocorreu alguma falha na importação dos dados. Entre em contato com o Admnistrador do sistema.'
            self.utils.addPortalMessage(msg, type='error')
        else:
            msg = 'Dados importados com sucesso.'
            self.utils.addPortalMessage(msg, type='info')

        return self.request.response.redirect(self.url_sucess)

    @memoize
    def AddContents(self):
        """
        """
        normalizer = getUtility(IIDNormalizer)
        try:
            if self.dados:
                portal = getSite()
                #Create folder SINESP
                if not hasattr(portal, 'sinesp'):
                    _createObjectByType('Folder',
                                        portal,
                                        'sinesp',
                                        title='Sinesp')
                folder_sinesp = getattr(portal, 'sinesp')
                folder_sinesp.setLayout('estatisticas-publicas-sinesp')
                for i in self.dados:

                    #Create folder type
                    tipo = i['tipo']
                    tipo_id = normalizer.normalize(tipo)
                    if not hasattr(folder_sinesp, tipo_id):
                        _createObjectByType('Folder',
                                            folder_sinesp,
                                            tipo_id,
                                            title=tipo)
                    folder_tipo = getattr(folder_sinesp, tipo_id)


                    #Create folder year
                    ano = str(i['ano'])
                    if not hasattr(folder_tipo, ano):
                        _createObjectByType('Folder',
                                            folder_tipo,
                                            ano,
                                            title=ano)
                    folder_ano = getattr(folder_tipo, ano)

                    #Create folder UF
                    # uf = i['uf']
                    # if not hasattr(folder_tipo, uf):
                    #     _createObjectByType('Folder',
                    #                         folder_tipo,
                    #                         uf,
                    #                         title=uf)
                    # folder_uf = getattr(folder_tipo, uf)

                    #Create content
                    id = str(i['ano']) + '-' + i['tipo'] + '-' + i['uf']
                    object_id = normalizer.normalize(id)
                    if not hasattr(folder_ano, object_id):
                        titulo = i['uf'] + ': ' + i['tipo']
                        _createObjectByType('sinesp',
                                            folder_ano,
                                            object_id,
                                            title=titulo,
                                            tipo=i['tipo'],
                                            uf=i['uf'],
                                            ano=i['ano'],
                                            qtd_ocorrencias=i['qtd_ocorrencias'],
                                            taxa=i['taxa'],
                                            universo=i['universo'])
            return True
        except:
            return False

    @memoize
    def site_url(self):
        portal_state = getMultiAdapter((self.context, self.request), name=u'plone_portal_state')
        site_url = portal_state.portal_url()
        return site_url
