# -*- coding: utf-8 -*-

{
    'name': 'Stock Account',
    'category': 'Inventory',
    'images': ['static/description/banner.png'],
    'version': '1.0',
    'license': 'AGPL-3',
    'author': 'Jupetern',
    'website': 'https://github.com/jupetern/udoo',
    'depends': [
        'udoo_excel',
        'udoo_filter_binding',
        'stock_account',
    ],
    'data': [
        'security/ir.model.access.csv',
        'report/stock_account/report_stock_account.xml',
    ],
}
