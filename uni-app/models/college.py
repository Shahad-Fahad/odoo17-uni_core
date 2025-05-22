from odoo import models, fields

class College(models.Model):
    _name = 'college'

    name = fields.Char()
    code = fields.Char()
    department_ids = fields.One2many('department','college_id')
