# -*- coding: utf-8 -*-
# Copyright 2024 Jupetern

{
    'name': 'Multiple Website Product',
    'category': 'Website/Website',
    'summary': 'add multiple websites per product in odoo multi website, odoo multi website, multi website select, add product into multiple website, website select in bulk, bulk website select, bulk website assign, bulk website, multi websites per product, multiple websites, product in multi website, multi websites per category, add category into multiple website, add multiple websites per category in odoo multi website, bulk website select in product category, multi website odoo',
    'version': '1.0',
    'license': 'AGPL-3',
    'author': 'Jupetern',
    'website': 'https://github.com/jupetern',
    'images': ['static/description/banner.png'],
    'depends': [
        'website_sale',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/product_views.xml',
        'wizard/multi_website_setter.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'udoo_product_multi_website/static/scss/*.scss',
        ],
    },
}
