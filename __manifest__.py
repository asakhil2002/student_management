{
    "name": "Student Management_akhil",
    "version": "1.0",
    "summary": "Student Management",
    "description": """to know student details""",
    "depends": ["base", "sale"],
    "installable": True,
    "auto_install": False,
    "application": True,
    "data": [
        "security/security.xml",
        "security/ir.model.access.csv",
        "report/student_report.xml",
        "report/student_template.xml",
        "views/students_management.xml",
        "views/parent_views.xml",
        "views/school_view.xml",
        "views/data.xml",
        "views/sale_view.xml",
        "wizard/wizard.xml",
        "views/menu.xml",
    ]

}
