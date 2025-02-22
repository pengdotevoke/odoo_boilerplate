{
    'name': 'Odoo Boilerplate',
    'version': '1.0',
    'category': 'Accounting',
    'summary': 'CCustom module that creates basic templates for odoo app development',
    'author': 'James Oginga',
    'depends': ['base'],  
    'data': [
        'security/ir.model.access.csv',
        'views/bank_reconciliation_views.xml',
    ],
    'installable': True,
    'application': True,
}
