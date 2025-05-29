from odoo import models, fields

class Department(models.Model):
    _name = 'college.department'
    _description = 'Department'


    name = fields.Char()
    code = fields.Char()
    college_id = fields.Many2one('university.college')

