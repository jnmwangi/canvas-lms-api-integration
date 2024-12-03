# Canvas LMS API Integration
This repository contains code for integrating Canvas LMS API
The `lib` module is used to create and manage "Foundation of Data Analysis" course

## Set Up
### Prerequisite
To run the code, you need to have the following installed:-
- Python 3
- venv (for managing virtual environment)
- include .env file with the following environment variables
```
CANVAS_LMS_BASE_URL=https://<canvas_domain>/api/v1
CANVAS_LMS_ACCESS_TOKEN = your-access-token
```

#### Package installations
```
pip install -r requirements.txt
```
## Running module
```
python -m create_course
```