# -*- coding: utf-8 -*-
# Copyright 2019 Ecosoft Co., Ltd (http://ecosoft.co.th/)
# Copyright 2024 Jupetern
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl)

{
    'name': 'Dynamic Excel Engine Demo',
    'category': 'Tools',
    'version': '1.1',
    'license': 'AGPL-3',
    'author': 'Jupetern,Ecosoft,Odoo Community Association (OCA)',
    'website': 'https://github.com/jupetern',
    'images': ['static/description/banner.png'],
    'depends': [
        'udoo_excel',
        'sale_management',
        'purchase',
        'crm',
    ],
    'data': [
        'security/ir.model.access.csv',
        'report/sale_order/sale_order_form.xml',
        'report/sale_order/sale_orders_partner.xml',
        'report/crm_revenue/crm_lead.xml',
        'report/partner_list/partner_list.xml',
        'report/import_sale_orders/actions.xml',
        'report/import_sale_orders/templates.xml',
        'report/import_export_sale_order/actions.xml',
        'report/import_export_sale_order/templates.xml',
        'report/import_export_purchase_order/actions.xml',
        'report/import_export_purchase_order/templates.xml',
    ],
}
