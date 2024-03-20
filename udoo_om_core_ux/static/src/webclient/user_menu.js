/** @odoo-module **/

import { _t } from '@web/core/l10n/translation';
import { UserMenu } from '@web/webclient/user_menu/user_menu';
import { patch } from '@web/core/utils/patch';
import { browser } from '@web/core/browser/browser';
import { registry } from '@web/core/registry';
import { session } from '@web/session';

const userMenuRegistry = registry.category('user_menuitems');

function documentationItem(env) {
    const documentationURL = session.documentation_url
    return {
        type: 'item',
        id: 'documentation',
        description: _t('Documentation'),
        href: documentationURL,
        callback: () => {
            browser.open(documentationURL, '_blank');
        },
        sequence: 10,
    };
}

function saasAccountItem(env) {
    const saasAccountURL = session.saas_account_url
    return {
        type: 'item',
        id: 'account',
        description: _t('My Online Account'),
        callback: () => {
            browser.open(saasAccountURL, '_blank');
        },
        sequence: 60,
    };
}

function separatorMode() {
    return {
        type: 'separator',
        sequence: 31,
    };
}

patch(UserMenu.prototype, {
    setup() {
        super.setup();
        if (session.documentation_url)
            userMenuRegistry.add('documentation', documentationItem, { 'force': true });
        if (session.saas_account_url)
            userMenuRegistry.add('odoo_account', saasAccountItem, { 'force': true });
    },
});
