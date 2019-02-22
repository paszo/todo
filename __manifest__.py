{
    'name': 'To-Do Application',
    'description': 'Manage personal to-do tasks.',
    'author': 'Daniel Reis',
    'depends': ['base'],
    'application': True,
    'data': [
             'security/ir.model.access.csv',
             'views/todo_menu.xml',
             'views/todo_view.xml',
    ],
}
