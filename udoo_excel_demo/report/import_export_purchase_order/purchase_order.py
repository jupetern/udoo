# -*- coding: utf-8 -*-
# Copyright 2024 Jupetern
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl)

from odoo import models, _


class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    def _o_export_dict(self):
        return {
            'export_purchase_order.purchase': {
                '_HEAD_': {
                    'B1': 'partner_id.contact_address',
                    'F4': 'display_name',
                    'H4': 'date_order',
                    'B8': 'user_id.display_name',
                    'B10': 'company_id.name',
                    'B12': '${"%s, %s, %s" % (object.company_id.street, object.company_id.city, object.company_id.state_id.name)}',
                    'B15': 'company_id.phone',
                    'B17': 'company_id.email',
                    'E8': 'partner_id.name',
                    'E10': 'partner_id.parent_id.name',
                    'E15': 'partner_id.phone',
                    'E17': 'partner_id.email',
                    'H20': 'date_planned${value or ""}#{format=date}',
                    'I37': 'amount_untaxed#{format=number}',
                    'O38': 'amount_tax#{format=number}',
                    'I39': 'amount_total#{format=number}',
                },
                'order_line': {
                    'B22': 'product_id.default_code',
                    'C22': 'name',
                    'E22': 'product_qty${value or 0}#{format=number}',
                    'F22': 'product_uom.name',
                    'G22': 'price_unit${value or 0}#{format=number}',
                    'H22': 'taxes_id.name',
                },
            }
        }
