from odoo import models, fields, api

class PatientAppoitment(models.Model):
    _name = 'patient.appointment'
    _description = 'Create Patient Appointments'
    _inherit = ['mail.thread','mail.activity.mixin']
    _rec_name = 'patient_id'

    patient_id = fields.Many2one('hospital.patient', string='Patient Name', required=True, tracking=True) #many2one fields must always have a name that end with _id and have a comodel[source of data]
    appointment_date = fields.Date('Appointment Date', required=True, tracking=True)
    note = fields.Text('Notes', tracking=True)
    state = fields.Selection([('draft', 'Draft'), ('confirm', 'Confirmed'), ('ongoing', 'Ongoing'), ('complete', 'Complete'),('cancel', 'Cancelled')], default='draft', tracking=True)

    def action_confirm(self):
        for record in self:
            record.state = 'confirm'
    
    def action_ongoing(self):
        for record in self:
            record.state = 'ongoing'
    
    def action_complete(self):
        for record in self:
            record.state = 'complete'
    
    def action_cancel(self):
        for record in self:
            record.state = 'cancel'