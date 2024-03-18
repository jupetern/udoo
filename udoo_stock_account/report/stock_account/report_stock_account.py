# -*- coding: utf-8 -*-
# Copyright 2024 Jupetern

from odoo.tools import format_date
from odoo import models, api, fields, _


class ReportStockAccount(models.AbstractModel):
    _name = 'report.stock.account'
    _inherit = ['xlsx.report', 'filter.report.wizard']
    _description = 'Wizard for report.stock.account'

    def _get_company_domain(self):
        return [('company_id', '=', self.env.company.id)]

    def _mdf_date_from(self):
        return self.date_from or fields.Date.context_today(self).replace(day=1)

    def _mdf_date_to(self):
        return self.date_to or fields.Date.context_today(self)

    subtitle = fields.Char(
        'Report subtitle',
        compute='_compute_subtitle',
    )

    # Search Criteria
    date_from = fields.Date(
        string='Date From',
        default=_mdf_date_from,
    )
    date_to = fields.Date(
        string='Date To',
        default=_mdf_date_to,
    )
    view_by_location = fields.Boolean(
        string='View By Locations',
        help='Available if Storage Locations setting is enabled',
        default=lambda self: self.env.user.has_group('stock.group_stock_multi_locations'),
        readonly=True,
    )
    warehouse_ids = fields.Many2many(
        'stock.warehouse',
        string='Warehouses',
        domain=_get_company_domain,
    )
    existing_wh_ids = fields.Many2many(
        'stock.warehouse',
        compute='_compute_existing_wh_ids',
    )
    location_ids = fields.Many2many(
        'stock.location',
        string='Locations',
    )

    @property
    def _tz(self):
        return self.env.context.get('tz') or self.env.user.tz or 'UTC'

    def _data_filtered_fields(self):
        return ['_date_from', '_date_to']

    def _wizard_filtered_fields(self):
        return ['warehouse_ids', 'location_ids']

    def _build_params(self, tail={}):
        if self.existing_wh_ids:
            warehouse_ids = self.existing_wh_ids
        else:
            warehouse_ids = self.warehouse_ids.search(self._get_company_domain())
        if self.location_ids:
            location_ids = self.location_ids.ids
        else:
            location_ids = self.location_ids.search(
                [
                    '&',
                    ('warehouse_id', 'in', warehouse_ids.ids),
                    ('usage', '=', 'internal'),
                ]
            ).ids
        date_to = self._mdf_date_to()
        date_from = self._mdf_date_from()

        tail.update(
            {
                '_company_id': self.env.company.id,
                '_location_ids': location_ids,
                '_tz': self._tz,
                '_date_to': date_to,
                '_date_from': date_from,
                '_days': (date_to - date_from).days,
            }
        )
        return self._gen_filtered(tail)

    @api.onchange('warehouse_ids')
    def _onchange_warehouse_ids(self):
        self.location_ids = self.location_ids.filtered(
            lambda o: o.warehouse_id.id in self.existing_wh_ids.ids
        )

    @api.depends('warehouse_ids')
    def _compute_existing_wh_ids(self):
        for rec in self:
            if rec.warehouse_ids:
                rec.existing_wh_ids = rec.warehouse_ids
            else:
                rec.existing_wh_ids = rec.warehouse_ids.search(rec._get_company_domain())

    @api.depends('date_from', 'date_to')
    def _compute_subtitle(self):
        for rec in self:
            rec.subtitle = rec._get_subtitle()

    def _get_subtitle(self):
        return _('From date %s to date %s') % (
            format_date(self.env, self._mdf_date_from()),
            format_date(self.env, self._mdf_date_to()),
        )

    def _get_display_name(self, prefix=''):
        return (
            prefix
            + ': '
            + _('%s ~ %s')
            % (
                format_date(self.env, self._mdf_date_from()),
                format_date(self.env, self._mdf_date_to()),
            )
        )

    def _prepare_data(self, params):
        return

    def report_xlsx(self):
        params = self._build_params()
        self._prepare_data(params)

        # Call parent to start report
        return super().report_xlsx()
