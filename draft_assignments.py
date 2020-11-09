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
SCOPES = ["https://www.googleapis.com/auth/classroom.coursework.students"]


def assignment(service, course, day, name):
    course_work = (
        service.courses().courseWork().create(courseId=course, body=day).execute()
    )
    print(
        "Assignement draft scheduled with Title {%s}" % course_work.get("title")
        + " for the class of "
        + name
    )


def main():
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists("token_assignment.pickle"):
        with open("token_assignment.pickle", "rb") as token_assignment:
            creds = pickle.load(token_assignment)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file("credentials.json", SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open("token_assignment.pickle", "wb") as token_assignment:
            pickle.dump(creds, token_assignment)

    service = build("classroom", "v1", credentials=creds)

    # Call the Classroom API

    date = "2020-11-16T14:00:23Z"

    monday_cs = {
        "title": "Monday:",
        "description": """Template for this """,
        "materials": [{"link": {"url": "http://codehs.com"}}],
        "workType": "ASSIGNMENT",
        "scheduledTime": date,
        "state": "DRAFT",
    }

    assignment(
        service,
        computer_science_principles_ap,
        monday_cs,
        "Computer Science Principles",
    )
    assignment(service, computer_science_a_ap, monday_cs, "Computer Science A")

    wednesday_cs = {
        "title": "Wednesday: Finish CodeHS",
        "description": """ Will be in google meets during class time if you need help. Finish codehs chapters reviewed on Tuesday""",
        "materials": [{"link": {"url": "http://codehs.com"}}],
        "workType": "ASSIGNMENT",
        "scheduledTime": date,
        "state": "DRAFT",
    }

    assignment(
        service,
        computer_science_principles_ap,
        wednesday_cs,
        "Computer Science Principles",
    )
    assignment(service, computer_science_a_ap, wednesday_cs, "Computer Science A")

    friday_cs = {
        "title": "Friday: Review Assignment",
        "description": """Assignment will posted on Thursday. Share the program with CodeHS.""",
        "materials": [{"link": {"url": "http://codehs.com"}}],
        "workType": "ASSIGNMENT",
        "scheduledTime": date,
        "state": "DRAFT",
    }

    assignment(
        service,
        computer_science_principles_ap,
        friday_cs,
        "Computer Science Principles",
    )
    assignment(service, computer_science_a_ap, friday_cs, "Computer Science A")


if __name__ == "__main__":
    main()
