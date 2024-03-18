# -*- coding: utf-8 -*-
# Copyright 2019 Ecosoft Co., Ltd (http://ecosoft.co.th)
# Copyright 2024 Jupetern
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl)

{
    'name': 'Dynamic Excel Engine',
    'category': 'Tools',
    'summary': 'Dynamic Excel import export report generation engine.',
    'version': '1.1',
    'license': 'AGPL-3',
    'author': 'Jupetern,Ecosoft,Odoo Community Association (OCA)',
    'website': 'https://github.com/jupetern/udoo',
    'images': ['static/description/banner.png'],
    'depends': ['web'],
    'external_dependencies': {'python': ['openpyxl']},
    'data': [
        'security/ir.model.access.csv',
        'wizard/export_xlsx_wizard.xml',
        'wizard/import_xlsx_wizard.xml',
        'wizard/report_xlsx_wizard.xml',
        'views/xlsx_template_view.xml',
        'views/xlsx_report.xml',
    ],
    'assets': {
        'web.assets_backend': [
            '/udoo_excel/static/src/js/report/action_manager_report.esm.js',
        ],
    },
}
