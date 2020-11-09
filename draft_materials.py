from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

Learning_APIs = 221418877483
PreCal_B = 213918693516
PreCal_A = 213918693436

Computer_Science_A_AP = 126645602070
Computer_Science_Principles_AP = 126645602060

# If modifying these scopes, delete the file token.pickle.
SCOPES = ["https://www.googleapis.com/auth/classroom.courseworkmaterials"]


def material(service, course, day, name):
    course_material = (
        service.courses()
        .courseWorkMaterials()
        .create(courseId=course, body=day)
        .execute()
    )
    print(
        "Assignement created with Title {%s}" % course_material.get("title")
        + " for the class of "
        + name
    )


def main():
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists("token_material.pickle"):
        with open("token_material.pickle", "rb") as token_material:
            creds = pickle.load(token_material)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file("credentials.json", SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open("token_material.pickle", "wb") as token_material:
            pickle.dump(creds, token_material)

    service = build("classroom", "v1", credentials=creds)

    # Call the Classroom API

    date = "2020-11-09T14:00:23Z"

    tuesday = {
        "title": "Tuesday:",
        "description": """Template for this """,
        "materials": [{"link": {"url": "http://codehs.com/"}}],
        "scheduledTime": date,
        "state": "DRAFT",
    }

    material(service, Learning_APIs, tuesday, "Learning APIs")

    thursday = {
        "title": "Thursday:",
        "description": """Template for this """,
        "materials": [{"link": {"url": "http://codehs.com/"}}],
        "scheduledTime": date,
        "state": "DRAFT",
    }

    material(service, Learning_APIs, thursday, "Learning APIs")


if __name__ == "__main__":
    main()
