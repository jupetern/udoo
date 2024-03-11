# -*- coding: utf-8 -*-

from odoo import models, _


class FilterReportWizard(models.AbstractModel):
    _name = 'filter.report.wizard'
    _description = 'Report Option Wizard'

    def _data_filtered_fields(self):
        return []

    def _wizard_filtered_fields(self):
        return []

    def _gen_filtered(self, tail):
        tmp = tail
        for f in self._data_filtered_fields():
            if f in tail and tail[f]:
                tmp['default' + f] = tail[f]

        for f in self._wizard_filtered_fields():
            if f in self and self[f]:
                if isinstance(self[f], models.BaseModel):
                    tmp['default_' + f] = self[f].ids
                else:
                    tmp['default_' + f] = self[f]
        return tmp
