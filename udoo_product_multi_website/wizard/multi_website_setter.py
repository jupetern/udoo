# -*- coding: utf-8 -*-
# Copyright 2024 Jupetern

from odoo import api, fields, models


class MultiWebsiteSetter(models.TransientModel):
    _name = 'multi.website.setter'
    _description = 'Multi Website Setter'

    product_ids = fields.Many2many('product.template')
    categories_ids = fields.Many2many('product.public.category')
    website_ids = fields.Many2many(
        'website',
        string='Websites',
        compute='_compute_website_ids',
        readonly=False,
        store=True,
    )

    @api.depends('product_ids', 'categories_ids')
    def _compute_website_ids(self):
        for rec in self:
            rec.website_ids |= rec.product_ids.public_website_ids
            rec.website_ids |= rec.categories_ids.public_website_ids

    def action_apply(self, websites=None):
        self.ensure_one()
        websites = websites if websites is not None else self.website_ids
        if self._context.get('set_product'):
            for rec in self.product_ids:
                rec.public_website_ids = websites
        elif self._context.get('set_category'):
            for rec in self.categories_ids:
                rec.public_website_ids = websites

    def action_apply_all(self):
        self.ensure_one()
        self.action_apply(self.env['website'].search([]))
