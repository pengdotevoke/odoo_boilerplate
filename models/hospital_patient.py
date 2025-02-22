from odoo import models, fields, api

class HospitalPatient(models.Model):
    _name = 'hospital.patient'
    _description = 'Patient Information'

    #Add fields here for patient details, such as name, age, gender, and date of birth.
    name = fields.Char('Name', required=True)
    age = fields.Integer('Age')
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other')
    ], string='Gender', default='male')
    dob = fields.Date('Date of Birth')