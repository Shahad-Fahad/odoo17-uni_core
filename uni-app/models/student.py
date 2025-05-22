from odoo import models, fields, api

class Student(models.Model):
    _name = 'student'

    name = fields.Char(required=True)
    student_id = fields.Char('Student ID',required=True,size=10)
    phone = fields.Char(required=True,size=10)
    email = fields.Char(required=True)
    enrollment_date = fields.Date()
    gender = fields.Selection([
    	('female','Female'),
    	('male','Male'),
    ])
    college_id = fields.Many2one('college')
    department_id = fields.Many2one('department')
    academiclevel_id = fields.Many2one('academic_level', string='Academic Level')
    course_ids = fields.Many2many('course')

    _sql_constraints = [
        ('unique_student_id', 'unique(student_id)', 'This Student ID is already exists.'),
        ('unique_phone', 'unique(phone)', 'This Phone Number is already exists.'),
        ('unique_email', 'unique(email)', 'This Email is already exists.')
    ]