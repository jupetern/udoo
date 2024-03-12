/** @odoo-module **/

import { patch } from '@web/core/utils/patch';
import { ActionMenus } from '@web/search/action_menus/action_menus';

patch(ActionMenus.prototype, {

    get printItems() {
        const printActions = this.props.items.print || [];
        return printActions.map((action) => ({
            action,
            description: action.name,
            key: action.id,
            icon: this.getReportIcon(action.report_type),
        }));
    },

    getReportIcon(type) {
        let map = {
            'excel': 'text-success ri-file-excel-2-line',
            'qweb-html': 'text-warning ri-html5-line',
            'qweb-pdf': 'text-danger ri-file-pdf-2-line',
            'qweb-text': 'text-info ri-file-text-line',
        }
        return map[type] || 'ri-file-info-line';
    }
});