# -*- coding: utf-8 -*-
# Copyright 2015 ABF OSIELL <https://osiell.com>
# Copyright 2024 Jupetern
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl)

{
    'name': 'Audit Logs',
    'category': 'Tools',
    'version': '2.2',
    'license': 'AGPL-3',
    'author': 'Jupetern,Ecosoft,Odoo Community Association (OCA)',
    'website': 'https://github.com/jupetern/udoo/wiki/Audit-Logs',
    'images': ['static/description/banner.png'],
    'depends': ['web'],
    'data': [
        'security/res_groups.xml',
        'security/ir.model.access.csv',
        'data/ir_cron.xml',
        'views/auditlog_view.xml',
        'views/http_session_view.xml',
        'views/http_request_view.xml',
    ],
}
