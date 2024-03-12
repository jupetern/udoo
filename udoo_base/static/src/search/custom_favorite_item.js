/** @odoo-module **/

import { patch } from '@web/core/utils/patch';
import { CustomFavoriteItem } from '@web/search/custom_favorite_item/custom_favorite_item';

patch(CustomFavoriteItem.prototype, {

    setup() {
        super.setup();
        this.description = _t('Save current search');
    },
});