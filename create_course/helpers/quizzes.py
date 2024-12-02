import requests
import os

BASE_URL=os.environ.get("CANVAS_LMS_BASE_URL")
ACCESS_TOKEN=os.environ.get("CANVAS_LMS_ACCESS_TOKEN")

headers = {
	"Content-Type":"application/json",
	"Authorization": f"Bearer {ACCESS_TOKEN}"
}

def create(course_id:int, quiz:dict):
    endpoint = f"/courses/{course_id}/quizzes"
    response = requests.post(f"{BASE_URL}/{endpoint}", headers=headers, json={"quiz":quiz})
    created_quiz = response.json()
    
    # Add 4 questions to quiz
    for q in range(4):
        qEndpoint = f"/courses/{course_id}/quizzes/{created_quiz['id']}/questions"
        question = {
            "name": f"Quiz question {q}",
            "text": f"The test of question {q}",
            "type": "short_answer_question"
        }
        requests.post(f"{BASE_URL}/{qEndpoint}", headers=headers, json=question)
    
    return created_quiz