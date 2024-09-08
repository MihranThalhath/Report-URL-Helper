/** @odoo-module **/


import ActionMenus from "web.ActionMenus";
import session from "web.session";
import rpc from "web.rpc";
import { patch } from 'web.utils';

patch(ActionMenus.prototype, "report_url_helper.ActionMenus", {
    setup() {
        this._super();
        this.printURLButtonStrings = {
            title: this.env._t("Print URL"),
            hotkey: this.env._t("Printing options"),
        };
    },
    async willStart() {
        const _super = this._super.bind(this, ...arguments);
        this.printURLItems = await this._setPrintURLItems(this.props);
        return _super();
    },
    async willUpdateProps(nextProps) {
        const _super = this._super.bind(this, ...arguments);
        this.printURLItems = await this._setPrintURLItems(nextProps);
        return _super(nextProps);
    },
    async _setPrintItems(props) {
        if (session.is_show_print_url_cog_menu && session.is_hide_default_print_cog_menu) {
            return [];
        }
        const printActions = props.items.print || [];
        const printItems = printActions.map(
            action => ({ action, description: action.name, key: action.id })
        );
        return printItems;
    },
    async _setPrintURLItems(props) {
        if (!session.is_show_print_url_cog_menu) {
            return [];
        }
        if (session.is_hide_default_print_cog_menu) {
            this.printURLButtonStrings.title = this.env._t("Print");
        }
        const printActions = props.items.print || [];
        const printItems = printActions.map(
            action => ({ action, description: action.name, key: action.id, printURL: true })
        );
        return printItems;
    },
    async _onItemSelected(ev) {
        ev.stopPropagation();
        const { item } = ev.detail;
        if (item.printURL) {
            const reportURL = await rpc.query({
                model: "ir.actions.report",
                method: "get_report_url",
                args: [item.key],
            });
            if (!reportURL || !this.props.activeIds) {
                return;
            }
            // open url in new tab
            window.open(`${reportURL}${this.props.activeIds[0]}`, "_blank");
        } else if (item.callback) {
            item.callback([item]);
        } else if (item.action) {
            this._executeAction(item.action);
        } else if (item.url) {
            // Event has been prevented at its source: we need to redirect manually.
            this.env.services.navigate(item.url);
        }
    },
});
