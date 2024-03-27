# -*- coding: utf-8 -*-
# Copyright 2024 Jupetern

import configparser

from odoo import models
from odoo.http import request


class IrHttp(models.AbstractModel):
    _inherit = 'ir.http'

    def session_info(self):
        result = super(IrHttp, self).session_info()
        config_sudo = request.env['ir.config_parameter'].sudo()

        udoo_configs_param = config_sudo.get_param('udoo_configs')
        p = configparser.RawConfigParser()

        try:
            p.read_string(udoo_configs_param)
            result['udoo_configs'] = p._sections

            if support_url := p._sections['brand'].get('support_url'):
                result['support_url'] = support_url
            if documentation_url := p._sections['brand'].get('documentation_url'):
                result['documentation_url'] = documentation_url
            if saas_account_url := p._sections['brand'].get('saas_account_url'):
                result['saas_account_url'] = saas_account_url

        except Exception:
            result['udoo_configs'] = {}

        return result
