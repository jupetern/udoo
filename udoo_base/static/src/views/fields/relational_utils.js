/** @odoo-module **/

import { patch } from '@web/core/utils/patch';
import { Dialog } from '@web/core/dialog/dialog';
import { X2ManyFieldDialog } from '@web/views/fields/relational_utils';


patch(X2ManyFieldDialog.prototype, {

    setup() {
        super.setup();
        this.dialogSize = this.props.record.context.dialog_size || Dialog.defaultProps.size;
    },
});