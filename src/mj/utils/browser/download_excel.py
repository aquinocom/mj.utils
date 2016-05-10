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
import xlsxwriter
import os
from tempfile import NamedTemporaryFile


class EXCELExportView(BrowserView):
    """
    """

    def __call__(self):
        ""
        ""
        filename = 'teste.xlxs'
        output = StringIO()
        workbook = xlsxwriter.Workbook(output)
        worksheet = workbook.add_worksheet('crime')
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
        merge_format_4.set_text_wrap()

        worksheet.merge_range('A10:J10', 'SECRETARIA NACIONAL DE SEGURANÇA PÚBLICA', merge_format)
        worksheet.merge_range('A11:J11', 'SISTEMA NACIONAL DE INFORMAÇÕES DE SEGURANÇA PÚBLICA – SINESP', merge_format)
        worksheet.merge_range('A13:J13', 'Número de registros de ocorrências de estupros e taxa por 100 mil habitantes referente aos anos de 2011 a 2014.', merge_format_1)

        anos = [2011,2012,2013,2014]
        len_anos = (len(anos)*2) + 1

        worksheet.merge_range(14, 2, 14, len_anos, 'Ano', merge_format_2)

        start_col_ano = 2
        start_row_ano = 15

        for i in anos:
            if anos.index(i) == 0:
                worksheet.merge_range(start_row_ano, start_col_ano, start_row_ano, start_col_ano + 1, i, merge_format_3)
            else:
                start_col_ano += 2
                worksheet.merge_range(start_row_ano, start_col_ano, start_row_ano, start_col_ano + 1, i, merge_format_3)

        worksheet.set_column('A:J', 20)
        worksheet.write('A17', 'Tipo de Crime', merge_format_2)
        worksheet.write('B17', 'Unidade da Federação', merge_format_2)

        start_col_reg_tx = 2
        start_row_reg_tx = 16
        for i in anos:
            if anos.index(i) == 0:
                worksheet.write(start_row_reg_tx, start_col_reg_tx, 'Registros de Ocorrências', merge_format_4)
                worksheet.write(start_row_reg_tx, start_col_reg_tx + 1, 'Taxa', merge_format_4)
            else:
                start_col_reg_tx += 2
                worksheet.write(start_row_reg_tx, start_col_reg_tx, 'Registros de Ocorrências', merge_format_4)
                worksheet.write(start_row_reg_tx, start_col_reg_tx + 1, 'Taxa', merge_format_4)


        workbook.close()

        xlsx_data = output.getvalue()

        self.request.response.setHeader('Content-Type', 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet; charset=utf-8')
        self.request.response.setHeader('Content-Disposition', 'attachment; filename="%s"' % filename)
        return xlsx_data
