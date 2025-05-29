from odoo import models, fields

class College(models.Model):
    _description = 'College'
    _name = 'university.college'
    name = fields.Char()
    name_ar = fields.Char(string='الاسم بالعربي')
    code = fields.Char()
    department_ids = fields.One2many('college.department','college_id')
