{
    'name': 'Odoo Boilerplate',
    'version': '1.0',
    'category': 'Accounting',
    'summary': 'Custom module that creates basic templates for odoo app development',
    'author': 'James Oginga',
    'depends': ['base', 'mail'],  
    'data': [
    'security/ir.model.access.csv', 
    'views/hospital_patient_view.xml',   
    'views/menu.xml',
    ],
    'installable': True,
    'application': True,
}
