import requests
import os

BASE_URL=os.environ.get("CANVAS_LMS_BASE_URL")
ACCESS_TOKEN=os.environ.get("CANVAS_LMS_ACCESS_TOKEN")

headers = {
	"Content-Type":"application/json",
	"Authorization": f"Bearer {ACCESS_TOKEN}"
}

def get_user():
    account_endpoint=f"{BASE_URL}/course_creation_accounts"
    response = requests.get(
        account_endpoint, 
        headers=headers
    )
    
    return response.json()