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
        "Material draft scheduled with Title {%s}" % course_material.get("title")
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

    date = "2020-12-14T14:00:23Z"

    # Create drafts for CS Classes

    tuesday_cs = {
        "title": "Tuesday 12/15: CodeHS",
        "description": """Watch the videos on CodeHS and make sure to fill out the form for attendance . Will be in google meets during class time if you need help.""",
        "materials": [
            {"link": {"url": "https://codehs.com"}},
            {"link": {"url": "https://forms.gle/5JsyfTMrpAphMCwF7"}},
        ],
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
        "title": "Thursday 12/17: CodeHS Review",
        "description": """Watch the video below for review and make sure to fill out the form for attendance . Will be in google meets during class time if you need help.""",
        "materials": [
            {"link": {"url": "https://codehs.com"}},
            {"link": {"url": "https://forms.gle/zMx2NmsJGYjiu5sh9"}},
        ],
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

    first_note_calA = {
        "title": "Monday 12/14: Notes",
        "description": """Watch the video below, follow notes and fill out form for your attendance for today or show up in google meets for live teaching""",
        "materials": [
            {"link": {"url": "https://www.desmos.com/scientific"}},
            {"link": {"url": "https://forms.gle/8ioVmwDA7qJpT4Ra6"}}
        ],
        "scheduledTime": date,
        "state": "DRAFT",
    }

    first_note_calB = {
        "title": "Tuesday 12/15: Notes",
        "description": """Watch the video below, follow notes and fill out form for your attendance for today or show up in google meets for live teaching""",
        "materials": [
            {"link": {"url": "https://www.desmos.com/scientific"}},
            {"link": {"url": "https://forms.gle/5JsyfTMrpAphMCwF7"}}
        ],
        "scheduledTime": date,
        "state": "DRAFT",
    }

    material(service, preCal_a, first_note_calA, "Pre-Cal A")
    material(service, preCal_b, first_note_calB, "Pre-Cal B")

    second_note_calA = {
        "title": "Wednesday 12/16: Notes",
        "description": """Watch the video below, follow notes and fill out form for your attendance for today or show up in google meets for live teaching""",
        "materials": [
            {"link": {"url": "https://www.desmos.com/scientific"}},
            {"link": {"url": "https://forms.gle/4rsnGKpszQm4rhjU7"}}
        ],
        "scheduledTime": date,
        "state": "DRAFT",
    }

    second_note_calB = {
        "title": "Thursday 12/17: Notes",
        "description": """Watch the video below, follow notes and fill out form for your attendance for today or show up in google meets for live teaching""",
        "materials": [
            {"link": {"url": "https://www.desmos.com/scientific"}},
            {"link": {"url": "https://forms.gle/zMx2NmsJGYjiu5sh9"}}
        ],
        "scheduledTime": date,
        "state": "DRAFT",
    }

    material(service, preCal_a, second_note_calA, "Pre-Cal A")
    material(service, preCal_b, second_note_calB, "Pre-Cal B")


if __name__ == "__main__":
    main()
