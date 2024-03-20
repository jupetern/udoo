/** @odoo-module **/

import { _t } from '@web/core/l10n/translation';
import { patch } from '@web/core/utils/patch';
import { useDebounced } from '@web/core/utils/timing';
import { useService } from '@web/core/utils/hooks';

import { ControlPanel } from '@web/search/control_panel/control_panel';
import { ConfirmationDialog } from '@web/core/confirmation_dialog/confirmation_dialog';

import { useFormStatusIndicatorState } from '../webclient/form_status/indicator';

const RFS_KEY_FRAMES = [
    { opacity: 0.9 },
    { transform: 'translateY(27px)', opacity: 0 },
    { opacity: 1 },
];

patch(ControlPanel.prototype, {

    setup() {
        super.setup();
        this.dialogService = useService('dialog');

        this.formIndicatorState = useFormStatusIndicatorState();
        this.doRefresh = useDebounced(this.doRefresh, 200);
    },

    async doRefresh() {
        const { config, searchModel, services } = this.env;
        const { pagerProps, formIndicatorState } = this;

        if (formIndicatorState && typeof formIndicatorState.displayButtons === 'function') {
            const hasDataUnsaved = !!(formIndicatorState.displayButtons());
            if (hasDataUnsaved) {
                this.dialogService.add(ConfirmationDialog, {
                    body: _t('There is unsaved data. Do you want to discard the changes and proceed?'),
                    confirm: async () => {
                        await formIndicatorState.discard();
                        return this._doRefresh();
                    },
                    cancel: () => { },
                });
                return;
            }
        }
        return this._doRefresh();
    },

    async _doRefresh() {
        const { pagerProps, searchModel } = this;

        // Refresh effect
        document.querySelector('.o_content').animate(RFS_KEY_FRAMES, {
            duration: 500,
            easing: 'ease-out',
        });

        // If has pager try it first
        if (pagerProps && typeof pagerProps.onUpdate === 'function') {
            console.log('pager');
            const { limit, offset } = pagerProps;
            await pagerProps.onUpdate({ offset, limit });
        }

        // Other case (setting form, ...)
        if (searchModel && typeof searchModel.search === 'function') {
            console.log('model');
            searchModel.search();
        }
    },

    get canRefresh() {
        const { searchModel } = this.env;
        const { pagerProps } = this.props;

        const hasSearchModel = searchModel && searchModel.search;
        return Boolean(hasSearchModel || (pagerProps && pagerProps.onUpdate));
    }
});
