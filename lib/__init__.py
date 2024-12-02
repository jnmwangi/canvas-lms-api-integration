from helpers import courses, modules, assignments, quizzes

# Create Course
created_course = courses.create({"name":"Foundation of Data Analysis"})

# Create Modules 
modules_data = [
	{ "name": "Introduction", "position": 1},
	{ 
        "name": "Module 2", 
        "position": 2,
        "unlock_at": "2024-12-09T00:00:00",
        "require_sequential_progress": "true"
    },
    # Module 3 starts a week after module 2
    { 
        "name": "Module 3", 
        "position": 3,
        "unlock_at": "2024-12-16T00:00:00",
        "require_sequential_progress": "true"
    },
]

created_modules = []
for m in modules_data:
    
    prerequisite_ids = []
    
    # Add the previous module as a prerequisite
    if len(created_modules) > 0:
        module = created_modules[-1]
        prerequisite_ids.append(module["id"])
    
    created_module = modules.create(created_course["id"], m, prerequisite_ids)
    created_modules.append(created_module)


# Create and add assignments
assignments_data = [{
        "title":"Assignment 1",
        "description":"&lt;p&gt;This would be a long html description&lt;/p&gt;",
        "submission_types":["online_url","online_upload"]
    },
    {
      "title": "Assignment 2",
      "description":"&lt;p&gt;This would be a long html description&lt;/p&gt;",
        "submission_types":["online_url","online_upload"]
      }
]

for i, assignment in enumerate(assignments_data):
    created_assignment = assignments.create(created_course['id'], assignment)
    # Add assignment to module at index i of the created modules
    module = created_modules[i]
    modules.add_item(created_course['id'], module['id'], created_assignment['id'])

# Create and add 2 quizzes for each module
for i in range(2):
    quiz = quizzes.create(
        created_course["id"],
        {
            "title": f"Quiz {i}",
            "description": f"This is the description of quiz {i}",
            "type": "assignment"
        }
    )

    # Add quize to module
    module = created_modules[i]
    modules.add_item(created_course["id"], module["id"], quiz["id"])
    
