import requests
import os

BASE_URL=os.environ.get("CANVAS_LMS_BASE_URL")
ACCESS_TOKEN=os.environ.get("CANVAS_LMS_ACCESS_TOKEN")

headers = {
	"Content-Type":"application/json",
	"Authorization": f"Bearer {ACCESS_TOKEN}"
}

def create(course_id:int, module:dict, prerequisite_ids:list = []):
    endpoint = f"/courses/{course_id}/modules"
    for k, v in module.items(): module[k] = v
    
    # Add the previous module as a prerequisite
    if len(prerequisite_ids) > 0:
        module["prerequisite_module_ids"] = prerequisite_ids
        
    response = requests.post(f"{BASE_URL}/{endpoint}", headers=headers, json={"module": module})
    
    created_module = response.json()
    return created_module

def add_item(course_id:int, module_id:int, content_id:int):
    endpoint = f"/courses/{course_id}/modules/{module_id}/items"
    data = {
        "item":{
            "title": "Assignment 1",
            "type": "Assignment",
            "content_id": content_id,
            "completion_requirement": "must_submit"
        }
    }
    requests.post(f"{BASE_URL}/{endpoint}", headers=headers, json=data)