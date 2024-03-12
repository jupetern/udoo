# -*- coding: utf-8 -*-
# Copyright 2024 Jupetern

{
    'name': 'Multiple Website Product',
    'category': 'Website/Website',
    'summary': 'Managing products across multiple websites',
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
