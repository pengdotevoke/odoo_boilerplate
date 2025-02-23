from odoo import models, fields, api

class PatientAppoitment(models.Model):
    _name = 'patient.appointment'
    _description = 'Create Patient Appointments'
    _inherit = ['mail.thread','mail.activity.mixin']

    patient_id = fields.Many2one('hospital.patient', string='Patient Name', required=True, tracking=True) #many2one fields must always have a name that end with _id and have a comodel[source of data]
    appointment_date = fields.Date('Appointment Date', required=True, tracking=True)
    note = fields.Text('Notes', tracking=True)
