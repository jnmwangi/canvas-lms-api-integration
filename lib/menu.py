from lib.helpers import courses
from tabulate import tabulate

course_options = lambda:print(f"""{tabulate([[c["id"], c["name"]] for c in courses.get_all()], headers=["Id", "Name"])}
\nEnter course id from the list above""")

module_options = lambda:print(f"""{tabulate([[c["id"], c["name"]] for c in courses.get_modules()], headers=["Id", "Name"])}
\nEnter course id from the list above""")

menu = [
    {
        "name": "Manage Courses",
        "actions": [
            {
                "name":"List Courses",
                "action": lambda: print(tabulate([[i+1, c["name"]] for i, c in enumerate(courses.get_all())], headers=["#", "Course Name"])),
                "display_as": "list"
            },
            {
                "name":"Create Course",
                "instructions":"Enter the following info:-",
                "fields":[
                    {"name":"Course Name", "field":"name"},
                    {"name":"Course Code", "field":"course_code"}
                ],
                "action": courses.create
            }
        ]
    },
    
    {
        "name": "Manage Modules",
        "actions": [
            {
                "name":"Create Module",
                "instructions":"Enter the following info:-",
                "fields":[
                    {"name":"Course", "field":"course_id", "action":course_options},
                    {"name":"Module Name", "field":"name"},
                    {"name":"Unlock At(YYYY-MM-DD)(optional)", "field":"unlock_at"},
                    {"name":"Require Sequential Progress", "field":"require_sequential_progress"},
                ],
                "action": lambda a: print("Cool")
            },
            
            {
                "name": "Add Module Item",
                "instructions":"Enter assignemnt information",
                "fields":[
                    {"name":"Course", "field":"course_id", "action":course_options},
                    {"name":"Module", "field":"course_id", "action":module_options},
                    {"name":"Title", "field":"title"},
                    {"name":"Type", "field":"type", "options":lambda:print("Select Either: Assignment, Quiz")},
                ]
            }
        ]
    }
]