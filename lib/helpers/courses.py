import requests
import os
from .user import get_user

BASE_URL=os.environ.get("CANVAS_LMS_BASE_URL")
ACCESS_TOKEN=os.environ.get("CANVAS_LMS_ACCESS_TOKEN")

headers = {
	"Content-Type":"application/json",
	"Authorization": f"Bearer {ACCESS_TOKEN}"
}

def create(course:dict):
    accounts = get_user()
    account = accounts[0]
    
    endpoint = f"{BASE_URL}/accounts/{account['id']}/courses"
    endpoint += "?enroll_me=true&course[sync_enrollments_from_homeroom]=false&"
    body = []
    for k, v in course.items():
        body.append(f"course[{k}]={v}")
    
    endpoint += "&".join(body)
    response = requests.post(
        endpoint,
        headers=headers
    )
    
    return response.json()

def get_all():
    endpoint = f"{BASE_URL}/courses"
    response = requests.get(
        endpoint,
        headers=headers
    )
    
    return response.json()

def get_modules(course_id:int):
    endpoint = f"{BASE_URL}/courses/{course_id}/modules"
    response = requests.get(
        endpoint,
        headers=headers
    )
    
    return response.json()