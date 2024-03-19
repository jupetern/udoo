# -*- coding: utf-8 -*-
# Copyright 2024 Jupetern

{
    'name': 'Om Graph Palette',
    'category': 'Tools',
    'summary': 'Refined Odoo Graph View with the best color palettes for data visualization, color palette, customize bar color, changing colors in graph, different colors, graph color, bar chart color, line chart, better charts, material chart, dynamic theme color, enterprise color theme, enterprise theme',
    'version': '1.0',
    'license': 'AGPL-3',
    'author': 'Jupetern',
    'website': 'https://github.com/jupetern/udoo',
    'images': [
        'static/description/banner.png',
    ],
    'assets': {
        'web.assets_backend': [
            (
                'before',
                'web/static/src/webclient/**/*',
                'udoo_om_chart/static/src/views/**/*',
            ),
        ],
        'web._assets_core': [
            (
                'replace',
                'web/static/src/core/colors/colors.js',
                'udoo_om_chart/static/src/core/colors.js',
            ),
        ],
    },
}
