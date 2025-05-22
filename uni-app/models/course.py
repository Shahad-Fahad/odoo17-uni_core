from odoo import models, fields

class Course(models.Model):
    _name = 'course'

    name = fields.Char()
    code = fields.Char()