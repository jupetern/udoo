# -*- coding: utf-8 -*-
# Copyright 2024 Jupetern

{
    'name': 'Wizard Filter Binding',
    'category': 'Hidden/Tools',
    'version': '1.0',
    'license': 'LGPL-3',
    'author': 'Jupetern',
    'website': 'https://github.com/jupetern',
    'images': ['static/description/banner.png'],
    'depends': ['web'],
    'data': [
        'security/ir.model.access.csv',
    ],
    'assets': {
        'web.assets_backend': [
            'udoo_filter_binding/static/src/**/*',
        ],
    },
}
