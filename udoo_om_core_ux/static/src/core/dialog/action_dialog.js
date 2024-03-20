/** @odoo-module */

import { patch } from "@web/core/utils/patch";
import { Dialog } from "@web/core/dialog/dialog";
import { SelectCreateDialog } from "@web/views/view_dialogs/select_create_dialog";

patch(Dialog.prototype, {
    toggle_dialog_size() {
        const inbackfs = this.props.size != 'fs';
        if (inbackfs) {
            this.bkSize = this.props.size;
        }
        this.props.size = inbackfs ? 'fs' : this.bkSize;
        this.render();
    }
});

patch(SelectCreateDialog.prototype, {
    toggle_dialog_size() {
        const inbackfs = this.props.size != 'fs';
        if (inbackfs) {
            this.bkSize = this.props.size;
        }
        this.props.size = inbackfs ? 'fs' : this.bkSize;
        this.render();
    }
});
