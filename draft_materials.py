from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

learning_APIs = 221418877483
preCal_b = 213918693516
preCal_a = 213918693436

computer_science_a_ap = 126645602070
computer_science_principles_ap = 126645602060

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
        "Assignement draft scheduled with Title {%s}" % course_material.get("title")
        + " for "
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

    date = "2020-11-16T14:00:23Z"



    # Create drafts for CS Classes




    tuesday_cs = {
        "title": "Tuesday: CodeHS",
        "description": """Watch the video below and make sure to fill out the form for attendance . Will be in google meets during class time if you need help.""",
        "materials": [{"link": {"url": "https://codehs.com"}}],
        "scheduledTime": date,
        "state": "DRAFT",
    }

    material(
        service,
        computer_science_principles_ap,
        tuesday_cs,
        "Computer Science Principles",
    )
    material(service, computer_science_a_ap, tuesday_cs, "Computer Science A")

    thursday_cs = {
        "title": "Thursday: CodeHS Review",
        "description": """Watch the video below and make sure to fill out the form for attendance . Will be in google meets during class time if you need help.""",
        "materials": [{"link": {"url": "https://codehs.com"}}],
        "scheduledTime": date,
        "state": "DRAFT",
    }

    material(
        service,
        computer_science_principles_ap,
        thursday_cs,
        "Computer Science Principles",
    )
    material(service, computer_science_a_ap, thursday_cs, "Computer Science A")



    # Create drafts for Pre-Cal Classes



    first_note_cal = {
        "title": "Monday A/Tuesday B: Notes",
        "description": """Watch the video below, follow notes and fill out form for your attendance for today or show up in google meets for live teaching""",
        "materials": [{"link": {"url": "https://www.desmos.com/scientific"}}],
        "scheduledTime": date,
        "state": "DRAFT",
    }

    material(service, preCal_a, first_note_cal, "Pre-Cal A")
    material(service, preCal_a, first_note_cal, "Pre-Cal B")

    second_note_cal = {
        "title": "Wednesday A/Thursday B: Notes",
        "description": """Watch the video below, follow notes and fill out form for your attendance for today or show up in google meets for live teaching""",
        "materials": [{"link": {"url": "https://www.desmos.com/scientific"}}],
        "scheduledTime": date,
        "state": "DRAFT",
    }

    material(service, preCal_a, second_note_cal, "Pre-Cal A")
    material(service, preCal_a, second_note_cal, "Pre-Cal B")


if __name__ == "__main__":
    main()
