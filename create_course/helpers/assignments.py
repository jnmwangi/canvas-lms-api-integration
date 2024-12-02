import requests
import os

BASE_URL=os.environ.get("CANVAS_LMS_BASE_URL")
ACCESS_TOKEN=os.environ.get("CANVAS_LMS_ACCESS_TOKEN")

headers = {
	"Content-Type":"application/json",
	"Authorization": f"Bearer {ACCESS_TOKEN}"
}

def create(course_id:int, assignment:dict):
    endpoint = f"/courses/{course_id}/assignments"
    data = { "assignment":assignment}
    response = requests.post(f"{BASE_URL}/{endpoint}", headers=headers, json=data)
    return response.json()