/** @odoo-module **/

import { CogMenu } from "@web/search/cog_menu/cog_menu";
import { patch } from "@web/core/utils/patch";
import { session } from '@web/session';
import { useService } from "@web/core/utils/hooks";

patch(CogMenu.prototype, {
    setup() {
        super.setup();
        this.orm = useService("orm");
    },
    get defaultPrintVisibility() {
        return session.is_hide_default_print_cog_menu;
    },
    get printUrlVisibility() {
        return session.is_show_print_url_cog_menu;
    },
    async onPrintUrlSelected(item) {
        if (!item || !item.key) {
            return;
        }

        const activeIds = this.props.getActiveIds();
        if (!activeIds || !activeIds.length) {
            return;
        }
        const reportUrl = await this.orm.call("ir.actions.report", "get_report_url", [item.key]);
        if (!reportUrl) {
            return;
        }
        // open url in new tab
        window.open(`${reportUrl}${activeIds[0]}`, "_blank");
    }
});
