# -*- coding: utf-8 -*-
# Copyright 2024 Jupetern

{
    'name': 'Om Backend Community Theme',
    'category': 'Themes/Backend',
    'summary': 'Refined Odoo UX with customizable app drawer, chatter box sizing, global search, sticky header, minimalist design, stunning graph view, group fold unfold, optimized multi-line, responsive mobile, sign up login design, split layout, user-friendly, flexible backend theme, fast backend theme, lightweight backend theme, animated backend theme, modern multipurpose theme, community color theme, community theme',
    'version': '1.2',
    'license': 'OPL-1',
    'author': 'Jupetern',
    'website': 'https://github.com/jupetern/udoo/wiki/Om-Backend-UX',
    'sequence': 7,
    'images': [
        'static/description/banner.png',
        'static/description/theme_screenshot.png',
    ],
    'depends': [
        'udoo_base',
        'auth_signup',
    ],
    'excludes': [
        'web_enterprise',
    ],
    'data': [
        'views/webclient_templates.xml',
    ],
    'assets': {
        'web._assets_primary_variables': {
            (
                'before',
                'web/static/src/scss/primary_variables.scss',
                'udoo_om_core_ux/static/src/scss/primary_variables.scss',
            ),
            (
                'after',
                'web/static/src/scss/primary_variables.scss',
                'udoo_om_core_ux/static/src/**/*.variables.scss',
            ),
        },
        'web._assets_secondary_variables': [
            (
                'before',
                'web/static/src/scss/secondary_variables.scss',
                'udoo_om_core_ux/static/src/scss/secondary_variables.scss',
            ),
        ],
        'web._assets_bootstrap': [
            'udoo_om_core_ux/static/src/scss/overridden_common.scss',
        ],
        'web._assets_backend_helpers': [
            (
                'before',
                'web/static/src/scss/bootstrap_overridden.scss',
                'udoo_om_core_ux/static/src/scss/bootstrap_backend_overridden.scss',
            ),
        ],
        'web.assets_backend': [
            'udoo_om_core_ux/static/src/scss/styles_backend.scss',
            (
                'replace',
                'web/static/src/webclient/navbar/navbar.scss',
                'udoo_om_core_ux/static/src/webclient/navbar/navbar.scss',
            ),
            (
                'after',
                'udoo_base/static/src/scss/overridden_icons.scss',
                'udoo_om_core_ux/static/src/scss/overridden_icons.scss',
            ),
            (
                'before',
                'web/static/src/webclient/**/*',
                'udoo_om_core_ux/static/src/views/**/*',
            ),
            'udoo_om_core_ux/static/src/core/**/*',
            'udoo_om_core_ux/static/src/search/**/*',
            'udoo_om_core_ux/static/src/webclient/**/*',
        ],
        'web.assets_frontend': [
            (
                'before',
                'web/static/lib/bootstrap/scss/_variables.scss',
                'udoo_om_core_ux/static/src/scss/bootstrap_frontend_variables.scss',
            ),
            (
                'after',
                'web/static/src/scss/fontawesome_overridden.scss',
                'udoo_om_core_ux/static/src/scss/overridden_icons.scss',
            ),
            (
                'replace',
                'web/static/src/webclient/navbar/navbar.scss',
                'udoo_om_core_ux/static/src/webclient/navbar/navbar.scss',
            ),
        ],
        'web._assets_core': [
            (
                'replace',
                'web/static/src/core/colors/colors.js',
                'udoo_om_core_ux/static/src/core/colors.js',
            ),
        ],
    },
}
