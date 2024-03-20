/** @odoo-module **/

import { patch } from '@web/core/utils/patch';
import { useService } from '@web/core/utils/hooks';
import { registry } from '@web/core/registry';
import { session } from '@web/session';
import { CommandPalette } from './burger_menu/quick_search';
import { WebClient } from '@web/webclient/webclient';

const trayMenu = registry.category('systray');

patch(WebClient.prototype, {
    setup() {
        super.setup();
        this.user = useService('user');
        this.hotkey = useService('hotkey');
        this.action = useService('action');

        /* Set system name by config */
        const uconfigs = session.udoo_configs;
        if (uconfigs.brand) {
            this.title.setParts({ zopenerp: uconfigs.brand.zopenerp });
        }

        /* System tray */
        trayMenu.add('quick_search', { Component: CommandPalette }, { sequence: 50 });
    },
});
