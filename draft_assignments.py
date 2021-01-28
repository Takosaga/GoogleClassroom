from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

learning_APIs = 221418877483

preCal_b = 213918693516
preCal_a = 213918693436

preCal = 258128831252

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
        + " for "
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

    # Setting times

    date = "2021-2-1T14:00:23Z"

    # This is the Sunday after for CST
    due = {
        "year": 2021,
        "month": 2,
        "day": 6
    }

    time = {
        "hours": 5,
        "minutes": 59,
        "seconds": 59,
        "nanos": 0
    }

    # Call the Classroom API
    # Create drafts for CS Classes

    monday_cs = {
        "title": "Monday 2/1: Catch Up/Codehs Quiz",
        "description": "This day is to catch up/ quiz over last weeks material.",
        "materials": [{"link": {"url": "http://codehs.com"}}],
        "workType": "ASSIGNMENT",
        "scheduledTime": date,
        "dueDate": due,
        "dueTime": time,
        "maxPoints": 100,
        "state": "DRAFT",
    }

    assignment(
        service,
        computer_science_principles_ap,
        monday_cs,
        "Computer Science Principles",
    )
    assignment(service, computer_science_a_ap, monday_cs, "Computer Science # A")

    wednesday_cs = {
        "title": "Wednesday 2/3: Finish CodeHS",
        "description": """ Will be in google meets during class time if you need help. Finish codehs chapters reviewed on Tuesday""",
        "materials": [{"link": {"url": "http://codehs.com"}}],
        "workType": "ASSIGNMENT",
        "scheduledTime": date,
        "dueDate": due,
        "dueTime": time,
        "maxPoints": 100,
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
        "title": "Friday 2/5: Review Assignment",
        "description": """Assignment will posted on Thursday. Share the program with CodeHS.""",
        "materials": [{"link": {"url": "http://codehs.com"}}],
        "workType": "ASSIGNMENT",
        "scheduledTime": date,
        "dueDate": due,
        "dueTime": time,
        "maxPoints": 100,
        "state": "DRAFT",
    }

    assignment(
        service,
        computer_science_principles_ap,
        friday_cs,
        "Computer Science Principles",
    )
    assignment(service, computer_science_a_ap, friday_cs, "Computer Science A")

    # Create drafts for Pre-Cal Class

    monday_cal = {
        "title": "Monday 2/1: Notes + Exit Ticket",
        "description": "Watch the video below, follow notes and do the exit ticket for your attendance for today or show up to google meets during class period",
        "materials": [
            {"link": {"url": "https://www.desmos.com/scientific"}},
            {"link": {"url": "https://api.socrative.com/rc/JrwgQn"}},
        ],
        "workType": "ASSIGNMENT",
        "scheduledTime": date,
        "dueDate": due,
        "dueTime": time,
        "maxPoints": 100,
        "state": "DRAFT",
    }

    tuesday_cal = {
        "title": "Tuesday 2/2: Assignment",
        "description": "Will be up by Tuesday 8 am. I will be in google meets for one on one questions",
        "materials": [
            {"link": {"url": "https://www.desmos.com/scientific"}},
            {"link": {"url": "https://api.socrative.com/rc/PLV8sA"}},
        ],
        "workType": "ASSIGNMENT",
        "scheduledTime": date,
        "dueDate": due,
        "dueTime": time,
        "maxPoints": 100,
        "state": "DRAFT",
    }

    wednesday_cal = {
        "title": "Wednesday 2/3: Notes + Exit Ticket",
        "description": "Watch the video below, follow notes and do the exit ticket for your attendance for today or show up to google meets during class period",
        "materials": [
            {"link": {"url": "https://www.desmos.com/scientific"}},
            {"link": {"url": "https://api.socrative.com/rc/tkaACc"}},
        ],
        "workType": "ASSIGNMENT",
        "scheduledTime": date,
        "dueDate": due,
        "dueTime": time,
        "maxPoints": 100,
        "state": "DRAFT",
    }

    thursday_cal = {
        "title": "Thursday 2/4: Assignment",
        "description": "Will be up by Thursday 8am. I will be in google meets for one on one questions",
        "materials": [
            {"link": {"url": "https://www.desmos.com/scientific"}},
            {"link": {"url": "https://api.socrative.com/rc/ZSyhHx"}},
        ],
        "workType": "ASSIGNMENT",
        "scheduledTime": date,
        "dueDate": due,
        "dueTime": time,
        "maxPoints": 100,
        "state": "DRAFT",
    }

    friday_cal = {
        "title": "Friday 2/5: Review/Quiz over the week",
        "description": "This day is to review / quiz assignment over this weeks material. I will be in google meets for one on one questions",
        "materials": [
            {"link": {"url": "https://www.desmos.com/scientific"}},
            {"link": {"url": "https://api.socrative.com/rc/EYHpzL"}},
        ],
        "workType": "ASSIGNMENT",
        "scheduledTime": date,
        "dueDate": due,
        "dueTime": time,
        "maxPoints": 100,
        "state": "DRAFT",
    }

    assignment(service, preCal, monday_cal, "Pre-Cal")
    assignment(service, preCal, tuesday_cal, "Pre-Cal")
    assignment(service, preCal, wednesday_cal, "Pre-Cal")
    assignment(service, preCal, thursday_cal, "Pre-Cal")
    assignment(service, preCal, friday_cal, "Pre-Cal")

    # Create drafts for Pre-Cal A & B Classes
    """
    last_assign_calB = {
        "title": "Monday 1/11: Habits/Quiz",
        "description": "Will be up Thursday",
        "materials": [
            {"link": {"url": "https://www.desmos.com/scientific"}},
            {"link": {"url": "https://api.socrative.com/rc/tkaACc"}},
        ],
        "workType": "ASSIGNMENT",
        "scheduledTime": date,
        "dueDate": due,
        "dueTime": time,
        "maxPoints": 100,
        "state": "DRAFT",
    }

    # assignment(service, preCal_a, last_assign_calA, "Pre-Cal A")
    # assignment(service, preCal_b, last_assign_calB, "Pre-Cal B")

    first_assign_calA = {
        "title": "Tuesday 1/19: Assignment",
        "description": "Will be up by Tuesday",
        "materials": [
            {"link": {"url": "https://www.desmos.com/scientific"}},
            {"link": {"url": "https://api.socrative.com/rc/PLV8sA"}},
        ],
        "workType": "ASSIGNMENT",
        "scheduledTime": date,
        "dueDate": due,
        "dueTime": time,
        "maxPoints": 100,
        "state": "DRAFT",
    }

    first_assign_calB = {
        "title": "Wednesday 1/20: Assignment",
        "description": "Will be up on Tuesday",
        "materials": [
            {"link": {"url": "https://www.desmos.com/scientific"}},
            {"link": {"url": "https://api.socrative.com/rc/PLV8sA"}},
        ],
        "workType": "ASSIGNMENT",
        "scheduledTime": date,
        "dueDate": due,
        "dueTime": time,
        "maxPoints": 100,
        "state": "DRAFT",
    }

    # assignment(service, preCal_a, first_assign_calA, "Pre-Cal A")
    # assignment(service, preCal_b, first_assign_calB, "Pre-Cal B")

    second_assign_calA = {
        "title": "Thursday 1/21: Assignment",
        "description": "Will be up Thursday",
        "materials": [
            {"link": {"url": "https://www.desmos.com/scientific"}},
            {"link": {"url": "https://api.socrative.com/rc/TJhXMW"}},
        ],
        "workType": "ASSIGNMENT",
        "scheduledTime": date,
        "dueDate": due,
        "dueTime": time,
        "maxPoints": 100,
        "state": "DRAFT",
    }

    second_assign_calB = {
        "title": "Friday 1/22: Assignment",
        "description": "Will be up Thursday",
        "materials": [
            {"link": {"url": "https://www.desmos.com/scientific"}},
            {"link": {"url": "https://api.socrative.com/rc/TJhXMW"}},
        ],
        "workType": "ASSIGNMENT",
        "scheduledTime": date,
        "dueDate": due,
        "dueTime": time,
        "maxPoints": 100,
        "state": "DRAFT",
    }

    assignment(service, preCal_a, second_assign_calA, "Pre-Cal A")
    assignment(service, preCal_b, second_assign_calB, "Pre-Cal B")

    last_assign_calA = {
        "title": "Friday 1/22: Habits/Quiz",
        "description": "Will be up Thursday",
        "materials": [
            {"link": {"url": "https://www.desmos.com/scientific"}},
            {"link": {"url": "https://api.socrative.com/rc/tkaACc"}},
        ],
        "workType": "ASSIGNMENT",
        "scheduledTime": date,
        "dueDate": due,
        "dueTime": time,
        "maxPoints": 100,
        "state": "DRAFT",
    }
    """

    #Here for testing stuff

    """ testing =  {
        "title": "Monday B/ Friday A: Habits/Quiz",
        "description": "Will be up Thursday",
        "materials": [
            {"link": {"url": "https://www.desmos.com/scientific"}},
            {"link": {"url": "https://api.socrative.com/rc/tkaACc"}},
        ],
        "workType": "ASSIGNMENT",
        "scheduledTime": date,
        "dueDate": due,
        "dueTime": time,
        "maxPoints": 100,
        "state": "DRAFT",
    }

    assignment(service, learning_APIs, testing, "Learning APIs") """


if __name__ == "__main__":
    main()
