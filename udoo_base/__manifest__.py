# -*- coding: utf-8 -*-
# Copyright 2024 Jupetern
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl)

{
    'name': 'Udoo Base',
    'category': 'Hidden',
    'version': '1.0',
    'license': 'LGPL-3',
    'author': 'Jupetern',
    'website': 'https://github.com/jupetern',
    'images': ['static/description/banner.png'],
    'depends': [
        'base_setup',
        'mail',
    ],
    'data': [
        'views/ir_views.xml',
        'views/ir_module_module_views.xml',
        'views/webclient_templates.xml',
    ],
    'assets': {
        'web._assets_primary_variables': {
            (
                'before',
                'web/static/src/scss/primary_variables.scss',
                'udoo_base/static/src/scss/primary_variables.scss',
            ),
        },
        'web.assets_backend': [
            (
                'after',
                'web/static/src/scss/fontawesome_overridden.scss',
                'udoo_base/static/src/scss/overridden_icons.scss',
            ),
            'udoo_base/static/src/**/*',
        ],
        'web.assets_frontend': [
            (
                'after',
                'web/static/src/scss/fontawesome_overridden.scss',
                'udoo_base/static/src/scss/overridden_icons.scss',
            ),
        ],
    },
}
