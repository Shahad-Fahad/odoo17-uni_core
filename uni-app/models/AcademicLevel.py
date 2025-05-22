from odoo import models, fields

class AcademicLevel(models.Model):
    _name = 'academic_level'
    _rec_name = 'levels'


    levels = fields.Char('Academic Level')

      






