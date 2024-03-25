/** @odoo-module **/

import { patch } from '@web/core/utils/patch';
import { ActionMenus } from '@web/search/action_menus/action_menus';

patch(ActionMenus.prototype, {

    get printItems() {
        const items = super.printItems;
        for (const idx in items) {
            const el = items[idx];
            el.icon = this.getActReportIcon(el.action?.report_type);
        }
        return items;
    },

    getActReportIcon(type) {
        let map = {
            'excel': 'text-success ri-file-excel-2-line',
            'html': 'text-warning ri-html5-line',
            'pdf': 'text-danger ri-file-pdf-2-line',
            'text': 'text-info ri-file-text-line',
        }
        for (const key in map) {
            if (type instanceof String && type.includes(key)) {
                return map[key];
            }
        }
        return 'text-info ri-file-info-line';
    }
});