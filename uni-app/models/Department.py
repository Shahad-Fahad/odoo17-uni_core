from odoo import models, fields

class Department(models.Model):
    _name = 'department'


    name = fields.Char()
    code = fields.Char()
    college_id = fields.Many2one('college')

