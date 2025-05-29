{
    'name': 'University Core',
    'version': '17.0.0.1.0',
    'author': 'Shahad',
    'category': 'Education',
    'depends': ['base'],
    'data': [
            'security/ir.model.access.csv',
            'views/base_menu.xml',
            'views/college.department_view.xml',
            'views/university.student_view.xml',
            'views/university.college_view.xml',
            'views/student.academic.level_view.xml',
            'views/university.course_view.xml',
            ],

    'assets':{
        'web.assets_backend':['university_core\static\src\style.css']
    },                
            
    'application': True,
}