from odoo import models, fields, api

class HospitalStaff(models.Model):
    _name = 'hospital.staff'
    _description = 'Staff Information'
    _inherit = ['mail.thread', 'mail.activity.mixin'] # Adds tracking and activity functionality to the model.


    name = fields.Char('Name', required=True, tracking=True)
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other')
    ], string='Gender', default='male', tracking=True)
    dob = fields.Date('Date of Birth', tracking=True)
    role = fields.Selection([
        ('doctor', 'Doctor'),
        ('nurse', 'Nurse'),
        ('labtech', 'Laboratory Technician'),
        ('receptionist', 'Receptionist'),
        ('other', 'Other')
    ], string='Role', default='doctor', tracking=True)