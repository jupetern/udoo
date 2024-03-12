# -*- coding: utf-8 -*-
# Copyright 2024 Jupetern

from odoo import models, tools, _
from odoo.exceptions import MissingError
from odoo.tools import frozendict
from collections import defaultdict


class IrHttp(models.AbstractModel):
    _inherit = 'ir.actions.actions'

    @tools.ormcache('model_name', 'self.env.lang')
    def _get_bindings(self, model_name):
        cr = self.env.cr

        # discard unauthorized actions, and read action definitions
        result = defaultdict(list)

        self.env.flush_all()
        cr.execute(
            """
            SELECT a.id, a.type, a.binding_type
              FROM ir_actions a
              JOIN ir_model m ON a.binding_model_id = m.id
             WHERE m.model = %s
          ORDER BY a.id
        """,
            [model_name],
        )
        for action_id, action_model, binding_type in cr.fetchall():
            try:
                action = self.env[action_model].sudo().browse(action_id)
                fields = ['name', 'binding_view_types']
                for field in ('groups_id', 'res_model', 'sequence', 'report_type'): # Just add 'report_type' here
                    if field in action._fields:
                        fields.append(field)
                action = action.read(fields)[0]
                if action.get('groups_id'):
                    groups = self.env['res.groups'].browse(action['groups_id'])
                    action['groups_id'] = ','.join(
                        ext_id for ext_id in groups._ensure_xml_id().values()
                    )
                result[binding_type].append(frozendict(action))
            except MissingError:
                continue

        # sort actions by their sequence if sequence available
        if result.get('action'):
            result['action'] = tuple(
                sorted(result['action'], key=lambda vals: vals.get('sequence', 0))
            )
        return frozendict(result)
