from odoo import models, fields, api

class HospitalPatient(models.Model):
    _name = 'hospital.patient'
    _description = 'Patient Information'
    _inherit = ['mail.thread', 'mail.activity.mixin'] # Adds tracking and activity functionality to the model.

    #Add fields here for patient details, such as name, age, gender, and date of birth.
    name = fields.Char('Name', required=True, tracking=True)
    age = fields.Integer('Age', tracking=True)
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other')
    ], string='Gender', default='male', tracking=True)
    dob = fields.Date('Date of Birth', tracking=True)
    address = fields.Text('Address', tracking=True)