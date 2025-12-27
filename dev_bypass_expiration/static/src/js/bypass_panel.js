/** @odoo-module **/

import { patch } from "@web/core/utils/patch";
// In Odoo 17/18, we target the main WebClient or the specific panel if it exists
import { DatabaseExpirationPanel } from "@web/webclient/database_expiration_panel/database_expiration_panel";

patch(DatabaseExpirationPanel.prototype, {
    setup() {
        super.setup();
        // Force display to false on initialization
        if (this.state) {
            this.state.display = false;
        }
    },
    // Sometimes Odoo re-calculates visibility on specific events
    get display() {
        return false;
    }
});