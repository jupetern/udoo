# -*- coding: utf-8 -*-
# Copyright 2024 Jupetern

from odoo import api, models


class BaseModelExtend(models.AbstractModel):
    _inherit = 'base'

    @api.model
    def mat_line(self, attr, txt):
        if self[attr]:
            prefix = self[attr] + '\n'
        else:
            prefix = ''
        self[attr] = prefix + txt
