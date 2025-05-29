from odoo import models, fields

class Course(models.Model):
    _name = 'university.course'
    _description = 'Course'

    name = fields.Char()
    code = fields.Char()