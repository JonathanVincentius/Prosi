{
    'name': 'Prosi Kedokteran',
    'version': '19.0.1.0.0', 
    'category': 'Medical',
    'summary': 'Modul untuk manajemen sistem kedokteran',
    'depends': ['base'],     
    'data': [
        #'security/ir.model.access.csv',
        'views/welcome.xml',
        'views/register.xml',
        'views/login.xml',
    ],
    'installable': True,
    'application': True,     
}