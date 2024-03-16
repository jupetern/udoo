/** @odoo-module */

import { patch } from '@web/core/utils/patch';
import { useService } from '@web/core/utils/hooks';
import { PivotRenderer } from '@web/views/pivot/pivot_renderer';

patch(PivotRenderer.prototype, {

    setup() {
        super.setup();
        this.notification = useService('notification');
        this.search_ctx = this.env.searchModel._context;
    },

    async openExtraOptions() {
        const action_wizard = this.search_ctx.uslot_action;
        if (!action_wizard) {
            this.notification.add(
                this.env._t('This functionality is not yet implemented.'),
                {
                    title: this.env._t('Warning'),
                    type: 'warning',
                }
            );
            return;
        }
        this.actionService.doAction(action_wizard, {
            additionalContext: this.search_ctx.filter,
        });
    },
});