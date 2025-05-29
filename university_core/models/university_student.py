from odoo import models, fields, api, _
import logging

_logger = logging.getLogger(__name__)


class Student(models.Model):
    _name = 'university.student'
    _description = 'Student'

    name = fields.Char(required=True)
    student_id = fields.Char('Student ID', required=True, size=10)
    phone = fields.Char(required=True, size=10)
    email = fields.Char(required=True)
    enrollment_date = fields.Date(string='Enrollment Date', default=lambda self:fields.Date.today())
    gender = fields.Selection([
        ('female', 'Female'),
        ('male', 'Male'),
    ])
    college_id = fields.Many2one('university.college')
    department_id = fields.Many2one('college.department')
    academiclevel_id = fields.Many2one('student.academic.level', string='Academic Level')
    course_ids = fields.Many2many('university.course', string='Courses')
    course_count = fields.Integer(string='Course Count', compute='_compute_course_count', store=True)

    _sql_constraints = [
        ('unique_student_id', 'unique(student_id)', 'This Student ID is already exists.'),
        ('unique_phone', 'unique(phone)', 'This Phone Number is already exists.'),
        ('unique_email', 'unique(email)', 'This Email is already exists.')
    ]

    @api.depends('course_ids')
    def _compute_course_count(self):
        for student in self:
            student.course_count = len(student.course_ids)

    def action_count_courses(self):
        for student in self:
             _logger.info("Student %s is enrolled in %s courses.", student.name, len(student.course_ids))
