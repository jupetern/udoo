/** @odoo-module **/

import { _t } from '@web/core/l10n/translation';
import { patch } from '@web/core/utils/patch';
import { FormStatusIndicator } from '@web/views/form/form_status_indicator/form_status_indicator';
import { onWillRender, useState, reactive } from '@odoo/owl';

export const formIndicatorStore = reactive({});
export function useFormStatusIndicatorState() {
    return useState(formIndicatorStore);
}

function passFormStatusIndicator(getProps) {
    const formSdiState = useFormStatusIndicatorState({});

    onWillRender(() => {
        Object.assign(formSdiState, getProps() || {});
    });
}

patch(FormStatusIndicator.prototype, {

    setup() {
        super.setup();

        passFormStatusIndicator(() => {
            if (!this.props.model.root.isNew) {
                return {
                    discard: async () => this.discard(),
                    indicatorMode: () => this.indicatorMode,
                    displayButtons: () => this.displayButtons,
                };
            }
        });
    }
});