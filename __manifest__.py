{
    'name': 'Hope Hospital',
    'version': '1.0',
    'category': 'Accounting',
    'summary': 'Custom module for a hospital management system',
    'author': 'James Oginga',
    'depends': ['base', 'mail'],  
    'data': [
        'security/ir.model.access.csv', 
        'views/hospital_patient_view.xml', 
        'views/hospital_staff_view.xml',    
        'views/patient_appointment_view.xml', 
        'views/menu.xml',
    ],
    'installable': True,
    'application': True,
}
