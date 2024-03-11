# -*- coding: utf-8 -*-
# Copyright 2024 Jupetern

from odoo import api, fields, models, _
from odoo.http import request
from odoo.exceptions import ValidationError


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    public_website_ids = fields.Many2many(
        string='Websites',
        comodel_name='website',
        relation='product_template_public_website_rel',
        column1='product_id',
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

    @api.depends('is_published', 'website_id', 'public_website_ids')
    @api.depends_context('website_id')
    def _compute_website_published(self):
        current_website_id = self._context.get('website_id')
        for record in self.sudo():
            if current_website_id:
                restricts = record.public_website_ids | record.website_id
                record.website_published = record.is_published and (
                    not restricts or current_website_id in restricts.ids
                )
            else:
                record.website_published = record.is_published

    def can_access_from_current_website(self, website_id=False):
        can_access = True
        for product in self:
            restricts = product.public_website_ids | product.website_id
            if restricts:
                current_website_id = request.env['website'].get_current_website().id
                return not (current_website_id not in restricts.ids)
        return can_access

    def open_update_available_website(self):
        if any(not o.sale_ok for o in self):
            raise ValidationError(_("The selected products has not been set to 'Can be Sold'"))

        return {
            'name': _('Update Available Websites'),
            'res_model': 'multi.website.setter',
            'view_mode': 'form',
            'views': [[False, 'form']],
            'context': {
                'set_product': True,
                'default_product_ids': self.ids,
            },
            'target': 'new',
            'type': 'ir.actions.act_window',
        }
