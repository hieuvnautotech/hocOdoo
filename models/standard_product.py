from odoo import models, fields


class StandardProduct(models.Model):
    _name = 'standard.product'
    _description = 'Standard Product'

    name = fields.Char(string = 'Name')
    code = fields.Char(string = 'Code')
    model_id = fields.Many2one('standardmodel', string = 'Model')

    def open_popup(self):
        return {
			'type': 'ir.actions.act_window',
			'name': 'Popup Basic',
			'view_type': 'form',
			'view_mode': 'form',
			'res_model': self._name,
			'res_id': self.id,
            # 'view_id': self.env.ref('crud_basic.popup_basic').id,
			'target': 'new',
        }