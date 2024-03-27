# -*- coding: utf-8 -*-
# Copyright 2024 Jupetern

from . import controllers
from . import models

import logging
import re

from odoo import http
from odoo.tools import config

# -------------------------------------------------------------------------
# DATABASE FILTER INBOUND
# -------------------------------------------------------------------------

db_filter_outbound = http.db_filter


def dbfilter_2way(dbs, host=None):
    dbs = db_filter_outbound(dbs, host)
    env = http.request.httprequest.environ
    db_filter_inbound_regex = env.get('HTTP_X_ODOO_DBFILTER')
    if db_filter_inbound_regex:
        if host is None:
            host = env.get('HTTP_HOST', '')
        host = host.partition(':')[0]
        if host.startswith('www.'):
            host = host[4:]
        domain = host.partition('.')[0]
        dbfilter_re = re.compile(
            db_filter_inbound_regex.replace('%h', re.escape(host))
                                   .replace('%d', re.escape(domain)))
        dbs = [db for db in dbs if dbfilter_re.match(db)]

    return dbs


if config.get('proxy_mode') and config.get('dbfilter_inbound'):
    _logger = logging.getLogger(__name__)
    _logger.info('Using Two-way database filtering')
    http.db_filter = dbfilter_2way
