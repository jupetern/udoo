# -*- coding: utf-8 -*-
# Copyright 2024 Jupetern

from odoo.http import request
from odoo.addons.website_sale.controllers.main import WebsiteSale


class MultiWebsiteSale(WebsiteSale):
    def _get_additional_shop_values(self, values):
        vals = super()._get_additional_shop_values(values)
        website = request.env['website'].get_current_website()
        vals.update(
            {
                'categories': values['categories'].filtered(
                    lambda o: not o.public_website_ids or website in o.public_website_ids
                )
            }
        )
        return vals
