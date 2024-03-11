# -*- coding: utf-8 -*-
# Copyright 2024 Jupetern

from odoo import api, fields, models, _
from odoo.http import request


class ProductPublicCategory(models.Model):
    _inherit = "product.public.category"

    public_website_ids = fields.Many2many(
        string='Websites',
        comodel_name='website',
        relation='ecommerce_category_public_website_rel',
        column1='category_id',
        column2='website_id',
    )

    @api.model
    def _search_get_detail(self, website, order, options):
        res = super()._search_get_detail(website, order, options)
        res['base_domain'].append(
            [
                '|',
                ('public_website_ids', '=', False),
                ('public_website_ids', 'in', website.ids),
            ]
        )
        return res

    def can_access_from_current_website(self, website_id=False):
        can_access = True
        for product in self:
            restricts = product.public_website_ids | product.website_id
            if restricts:
                current_website_id = request.env['website'].get_current_website().id
                return not (current_website_id not in restricts.ids)
        return can_access

    def open_update_available_website(self):
        return {
            'name': _('Update Available Websites'),
            'res_model': 'multi.website.setter',
            'view_mode': 'form',
            'views': [[False, 'form']],
            'context': {
                'set_category': True,
                'default_categories_ids': self.ids,
            },
            'target': 'new',
            'type': 'ir.actions.act_window',
        }
