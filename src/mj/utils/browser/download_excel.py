# -*- coding: utf-8 -*-

# Product imports
from Products.CMFCore.utils import getToolByName
from Products.Five.browser import BrowserView
from zope.component import getMultiAdapter
from StringIO import StringIO
from zope.component import getUtility
import xlsxwriter
import os
import fpformat
from plone.memoize.instance import memoize
from plone.i18n.normalizer.interfaces import IIDNormalizer


class EXCELExportView(BrowserView):
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

        if 'tipo' in request.form:
            tipo = request.form['tipo']
            if tipo in self.getTipo():
                request.set('tipo', tipo)
                self.tipo = tipo
            else:
                request.set('tipo', None)
                self.tipo = None
        else:
            request.set('tipo', None)
            self.tipo = None

    def __call__(self):
        """
        """
        if self.tipo:
            return self.createFile()
        else:
            pass

    @memoize
    def createFile(self):
        """
        """
        self.getAnos()
        self.getInfo()
        self.getUF()

        normalizer = getUtility(IIDNormalizer)
        tipo_id = normalizer.normalize(self.tipo)
        filename = tipo_id + '.xlxs'
        output = StringIO()
        workbook = xlsxwriter.Workbook(output)
        worksheet = workbook.add_worksheet(self.tipo[:30])
        worksheet.hide_gridlines(2)
        img = os.path.dirname(os.path.abspath(__file__)) + '/img/brasao-mj.png'

        # Insert an image.
        worksheet.insert_image('E1', img)

        # Create a format to use in the merged range.
        merge_format = workbook.add_format({
            'bold': 0,
            'border': 0,
            'align': 'center',
            'valign': 'vcenter',})

        merge_format_1 = workbook.add_format({
            'bold': 1,
            'border': 0,
            'align': 'center',
            'valign': 'vcenter',
            'fg_color': '#CCCCCC'})

        merge_format_2 = workbook.add_format({
            'bold': 0,
            'border': 1,
            'align': 'center',
            'valign': 'vcenter',
            'fg_color': 'yellow'})

        merge_format_3 = workbook.add_format({
            'bold': 0,
            'border': 1,
            'align': 'center',
            'valign': 'vcenter',})

        merge_format_4 = workbook.add_format({
            'bold': 0,
            'border': 1,
            'align': 'center',
            'valign': 'vcenter',
            'fg_color': '#DDD'})

        merge_format_5 = workbook.add_format({
            'bold': 0,
            'border': 1,
            'align': 'right',
            'valign': 'vcenter',})

        merge_format_6 = workbook.add_format({
            'bold': 0,
            'border': 1,
            'align': 'left',
            'valign': 'vcenter',})

        merge_format_7 = workbook.add_format({
            'bold': 1,
            'border': 1,
            'align': 'right',
            'valign': 'vcenter',
            'fg_color': '#CCCCCC'})

        merge_format_4.set_text_wrap()
        merge_format_3.set_text_wrap()

        worksheet.merge_range('A10:J10', 'SECRETARIA NACIONAL DE SEGURANÇA PÚBLICA', merge_format)
        worksheet.merge_range('A11:J11', 'SISTEMA NACIONAL DE INFORMAÇÕES DE SEGURANÇA PÚBLICA – SINESP', merge_format)

        frotas = ['Furto de Veiculo', 'Roubo de Veículo']
        if self.tipo in frotas:
            texto = 'Número de registros de ocorrências de ' + self.tipo.lower() + ' e taxa por 100 mil veículos referente aos anos de ' + str(self.anos[0]) + ' a ' + str(self.anos[-1]) + '.'
        else:
            texto = 'Número de registros de ocorrências de ' + self.tipo.lower() + ' e taxa por 100 mil habitantes referente aos anos de ' + str(self.anos[0]) + ' a ' + str(self.anos[-1]) + '.'

        worksheet.merge_range('A13:J13', texto, merge_format_1)

        len_anos = (len(self.anos)*2) + 1

        worksheet.merge_range(14, 2, 14, len_anos, 'Ano', merge_format_2)

        start_col_ano = 2
        start_row_ano = 15

        start_col_reg_tx = 2
        start_row_reg_tx = 16

        start_row_total = 44

        for i in self.anos:
            total = self.getTotal(i)
            total_ocorrencia = total['total_registro']
            total_taxa = total['total_taxa']
            if self.anos.index(i) == 0:
                #
                worksheet.merge_range(start_row_ano, start_col_ano, start_row_ano, start_col_ano + 1, i, merge_format_3)
                #
                worksheet.write(start_row_reg_tx, start_col_reg_tx, 'Registros de Ocorrências', merge_format_4)
                worksheet.write(start_row_reg_tx, start_col_reg_tx + 1, 'Taxa', merge_format_4)
                #
                worksheet.write(start_row_total, start_col_reg_tx, total_ocorrencia, merge_format_7)
                worksheet.write(start_row_total, start_col_reg_tx + 1, total_taxa, merge_format_7)
            else:
                #
                start_col_ano += 2
                worksheet.merge_range(start_row_ano, start_col_ano, start_row_ano, start_col_ano + 1, i, merge_format_3)
                #
                start_col_reg_tx += 2
                worksheet.write(start_row_reg_tx, start_col_reg_tx, 'Registros de Ocorrências', merge_format_4)
                worksheet.write(start_row_reg_tx, start_col_reg_tx + 1, 'Taxa', merge_format_4)
                #
                worksheet.write(start_row_total, start_col_reg_tx, total_ocorrencia, merge_format_7)
                worksheet.write(start_row_total, start_col_reg_tx + 1, total_taxa, merge_format_7)

        worksheet.set_column('A:J', 20)
        worksheet.write('A17', 'Tipo de Crime', merge_format_2)
        worksheet.write('B17', 'Unidade da Federação', merge_format_2)

        worksheet.merge_range(17, 0, 43, 0, self.tipo, merge_format_3)

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

        start_col_uf = 1
        start_row_uf = 17

        for uf in self.uf:
            item = estados[uf]
            worksheet.write(start_row_uf, start_col_uf, item, merge_format_6)
            start_row_uf += 1


        dados = {}
        for uf in self.uf:
            dados[uf] = []
            for ano in self.anos:
                item = self.getItem(uf, ano)
                dados[uf].append(item['qtd_ocorrencias'])
                dados[uf].append(item['taxa'])

        start_col_val_reg_tx = 2
        start_row_val_reg_tx = 17

        for uf in self.uf:
            item = dados[uf]
            worksheet.write_row(start_row_val_reg_tx, start_col_val_reg_tx, item, merge_format_5)
            start_row_val_reg_tx += 1

        worksheet.merge_range(44, 0, 44, 1, 'Totalizadores para este crime →', merge_format_7)


        workbook.close()

        xlsx_data = output.getvalue()

        self.request.response.setHeader('Content-Type', 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet; charset=utf-8')
        self.request.response.setHeader('Content-Disposition', 'attachment; filename="%s"' % filename)
        return xlsx_data

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
    def getItem(self, uf, ano):
        """
        """
        for i in self.dados:
            if (i['uf'] == uf) and (i['ano'] == ano):
                return i