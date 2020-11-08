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
SCOPES = ["https://www.googleapis.com/auth/classroom.coursework.students"]


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
    monday = {
        "title": "Wednesday:",
        "description": """Template for this """,
        "materials": [{"link": {"url": "https://api.socrative.com/rc/PLV8sA"}}],
        "workType": "ASSIGNMENT",
        "scheduledTime": "2020-11-09T14:00:23Z",
        "state": "DRAFT",
    }

    coursework = (
        service.courses()
        .courseWork()
        .create(courseId=Learning_APIs, body=monday)
        .execute()
    )
    print("Assignment created with Title {%s}" % coursework.get("title"))


if __name__ == "__main__":
    main()
