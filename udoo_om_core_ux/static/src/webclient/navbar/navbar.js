/** @odoo-module **/

import { patch } from '@web/core/utils/patch';
import { NavBar } from '@web/webclient/navbar/navbar';
import { computeAppsAndMenuItems } from '@web/webclient/menus/menu_helpers';
import { useState, useExternalListener } from '@odoo/owl';


patch(NavBar.prototype, {
    setup() {
        super.setup();

        const apps = computeAppsAndMenuItems(this.menuService.getMenuAsTree('root')).apps;
        this.apps = useState(apps);
        this.state = useState({
            ueuopen: false,
            focusix: null,
        });

        useExternalListener(window, 'click', this.onWindowClicked, { capture: true });
    },

    onWindowClicked(ev) {
        // Return if already closed
        if (!this.state.ueuopen) {
            return;
        }

        // TODO
    },

    _isCurrentApp(app) {
        if (this.currentApp && app) {
            return this.currentApp.id === app.id
        }
        return false;
    },
});