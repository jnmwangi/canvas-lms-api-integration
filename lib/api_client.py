import os
import requests
from helpers import get_user

user = get_user()

class APIClient:
    
    __request_headers = {
            "Content-Type":"applicaiton/json",
            "Authorization":f"Bearer {ACCESS_TOKEN}"
        }

    def __init__(self):
        print("***Getting account information***")
        account_endpoint=f"{BASE_URL}/course_creation_accounts"
        response = requests.get(account_endpoint, headers=self.__request_headers)
        accounts = response.json()
        self.account_id = accounts[0]["id"]
    
    def createCourse(self, course: dict):
        endpoint = f"{BASE_URL}/accounts/{self.account_id}/courses"
        endpoint += "?enroll_me=true&course[sync_enrollments_from_homeroom]=false&"
        body = []
        for k, v in course.items():
            body.append(f"{k}={v}")
        
        endpoint += "&".join(body)
        response = requests.post(
            endpoint,
            headers=self.__request_headers
        )
        
        response_data = response.json()
        print(response_data)
        
        # response = requests.get(f"{BASE_URL}/")