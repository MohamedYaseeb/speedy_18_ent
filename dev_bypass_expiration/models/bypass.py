from odoo import models, api, fields
from datetime import datetime

class PublisherWarrantyContract(models.AbstractModel):
    _inherit = 'publisher_warranty.contract'

    def update_notification(self, cron_mode=True):
        # Stop Odoo from calling home to check the license
        return True

class IrHttp(models.AbstractModel):
    _inherit = 'ir.http'

    def session_info(self):
        res = super(IrHttp, self).session_info()
        # Override the session expiration date so the UI banner disappears
        res['expiration_date'] = "2099-12-31 23:59:59"
        res['expiration_reason'] = False
        res['warning'] = False
        return res

class IrConfigParameter(models.Model):
    _inherit = 'ir.config_parameter'

    @api.model
    def set_param(self, key, value):
        # Prevent Odoo from overwriting the expiration date back to a real one
        if key == 'database.expiration_date':
            value = "2099-12-31 23:59:59"
        return super(IrConfigParameter, self).set_param(key, value)