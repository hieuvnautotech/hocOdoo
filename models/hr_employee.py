from odoo import models, fields, api


class Staff(models.Model):
    _inherit = 'hr.employee'


    code = fields.Char(string='Employee Code', required=True)