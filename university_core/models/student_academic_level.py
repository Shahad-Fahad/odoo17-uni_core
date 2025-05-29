from odoo import models, fields

class AcademicLevel(models.Model):
    _name = 'student.academic.level'
    _description = 'Academic Levels'
    _rec_name = 'levels'

    levels = fields.Char('Academic Levels')

      






