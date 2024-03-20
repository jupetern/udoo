# -*- coding: utf-8 -*-

from odoo import tools, _
from odoo.addons.auth_signup.controllers.main import AuthSignupHome


class UdooHome(AuthSignupHome):
    def get_auth_signup_config(self):
        d = super().get_auth_signup_config()
        d.update(
            {
                'brand_name': tools.config.get('brand_name', _('Odoo')),
                'brand_url': tools.config.get(
                    'brand_url', 'https://www.odoo.com?utm_source=db&amp;utm_medium=auth'
                ),
            }
        )
        return d
