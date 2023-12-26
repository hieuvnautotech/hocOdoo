# -*- coding: utf-8 -*-
from odoo import models, fields


class stdModel(models.Model):
    _name = 'stdmodel'
    _description = 'Standard Model'

    code = fields.Char('Model #', required=True)
    name = fields.Char('Description', required=False)
    remark = fields.Char('Remark', required=False)

    # product_ids = fields.One2many('standard.product', 'model_id', 'Products')

    # display_text = fields.Char(string = 'Display Text', store = False)

    # def open_popup(self):
    #     return {
	# 		'type': 'ir.actions.act_window',
	# 		'name': 'Popup Basic',
	# 		'view_type': 'form',
	# 		'view_mode': 'form',
	# 		'res_model': self._name,
	# 		'res_id': self.id,   
    #         'view_id': self.env.ref('crud_basic.popup_basic').id,
	# 		'target': 'new',
    #         'context': {
    #             'default_display_text':'TEXT DEMO'
    #         }
    #     }maindddddd