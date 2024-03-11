/** @odoo-module */

import { patch } from '@web/core/utils/patch';
import { useService } from '@web/core/utils/hooks';
import { ListController } from '@web/views/list/list_controller';

patch(ListController.prototype, {
    setup() {
        super.setup();
        this.notification = useService('notification');
    },

    async openExtraOptions() {
        const action_wizard = this.props.context.uslot_action;
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
            additionalContext: this.props.context.filter,
        });
    },
});
