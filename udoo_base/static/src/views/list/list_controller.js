/** @odoo-module */

import { patch } from '@web/core/utils/patch';
import { ListController } from '@web/views/list/list_controller';

patch(ListController.prototype, {
    expandFoldGroups() {
        this.model.root.groups.forEach(group => {
            group.toggle();
        });
    },
});
