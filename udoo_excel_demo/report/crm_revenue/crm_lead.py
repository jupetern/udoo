# -*- coding: utf-8 -*-
# Copyright 2019 Ecosoft Co., Ltd (http://ecosoft.co.th/)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html)

from odoo import fields, models, _


class ReportCRMLead(models.TransientModel):
    _name = 'report.crm.lead'
    _description = 'Wizard for report.crm.lead'
    _inherit = 'xlsx.report'

    # Search Criteria
    team_id = fields.Many2one('crm.team', string='Sales Team')
    # Report Result, crm.lead
    results = fields.Many2many(
        'crm.lead',
        compute='_compute_results',
    )
    revenue_by_country = fields.Many2many(
        'crm.lead',
        compute='_compute_revenue_by_country',
    )
    revenue_by_team = fields.Many2many(
        'crm.lead',
        compute='_compute_revenue_by_team',
    )

    def _compute_results(self):
        self.ensure_one()
        domain = []
        if self.team_id:
            domain += [('team_id', '=', self.team_id.id)]
        self.results = self.env['crm.lead'].search(domain)

    def _compute_revenue_by_country(self):
        self.ensure_one()
        domain = []
        if self.team_id:
            domain += [('team_id', '=', self.team_id.id)]
        results = self.env['crm.lead'].read_group(
            domain,
            ['country_id', 'expected_revenue'],
            ['country_id'],
            orderby='country_id',
        )
        for row in results:
            self.revenue_by_country += self.env['crm.lead'].new(
                {
                    'country_id': row['country_id'],
                    'expected_revenue': row['expected_revenue'],
                }
            )

    def _compute_revenue_by_team(self):
        self.ensure_one()
        domain = []
        if self.team_id:
            domain += [('team_id', '=', self.team_id.id)]
        results = self.env['crm.lead'].read_group(
            domain, ['team_id', 'expected_revenue'], ['team_id'], orderby='team_id'
        )
        for row in results:
            self.revenue_by_team += self.env['crm.lead'].new(
                {'team_id': row['team_id'], 'expected_revenue': row['expected_revenue']}
            )

    def _o_export_engine(self):
        DEF_SF = '${"%s"}#{format=text}'
        DEF_TF = '${"%s"}#{format=text;rspan=1}'

        # Inject dynamic instructions through context with the following key format: export_{file name}.{sheet name}
        return self.env['xlsx.export'].with_context(
            {
                'export_crm_lead.crm_lead': {
                    '_NAME_': _('CRM Leads'),
                    '_HEAD_': {
                        'A2': DEF_SF % _('All Leads'),
                        'A3': DEF_SF % _('Opportunity'),
                        'B3': DEF_SF % _('Customer'),
                        'C3': DEF_SF % _('Country'),
                        'D3': DEF_SF % _('Next Activity Deadline'),
                        'E3': DEF_SF % _('Next Activity Summary'),
                        'F3': DEF_SF % _('Stage'),
                        'G3': DEF_SF % _('Expected Revenue'),
                        'H3': DEF_SF % _('Sales Team'),
                    },
                    'results': {
                        'A4': 'name',
                        'B4': 'partner_id.name',
                        'C4': 'country_id.name',
                        'D4': 'activity_date_deadline${value or ""}#{format=date}',
                        'E4': 'activity_summary',
                        'F4': 'stage_id.name',
                        'G4': 'expected_revenue${value or 0}#{format=number}',
                        'H4': 'team_id.name',
                    },
                },
                'export_crm_lead.revenue_by_country': {
                    '_NAME_': _('Revenue by Country'),
                    '_HEAD_': {
                        'A1': DEF_TF % _('Revenue by Country'),
                        'A2': DEF_SF % _('Country'),
                        'B2': DEF_SF % _('Expected Revenue'),
                    },
                    'revenue_by_country': {
                        'A3': 'country_id.name',
                        'B3': 'expected_revenue${value or 0}#{format=number}',
                    },
                },
                'export_crm_lead.revenue_by_team': {
                    '_NAME_': _('Revenue by Team'),
                    '_HEAD_': {
                        'A1': DEF_TF % _('Revenue by Team'),
                        'A2': DEF_SF % _('Team'),
                        'B2': DEF_SF % _('Expected Revenue'),
                    },
                    'revenue_by_team': {
                        'A3': 'team_id.name',
                        'B3': 'expected_revenue${value or 0}#{format=number}',
                    },
                },
            }
        )
