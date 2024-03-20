/** @odoo-module **/

import { Component } from "@odoo/owl";

export class CommandPalette extends Component {
    openMainPalette() {
        this.env.services.command.openMainPalette({
            searchValue: '/',
            bypassEditableProtection: true,
            global: true,
        })
    }
}

CommandPalette.template = 'udoo_om_core_ux.CommandPalette';
