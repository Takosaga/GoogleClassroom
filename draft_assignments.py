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

    date = "2021-5-10T12:00:23Z"

    # This is the Sunday after for CST
    due = {
        "year": 2021,
        "month": 5,
        "day": 16
    }

    dueAP = {
        "year": 2021,
        "month": 5,
        "day": 20
    }

    time = {
        "hours": 4,
        "minutes": 59,
        "seconds": 59,
        "nanos": 0
    }

    # Call the Classroom API
    # Create drafts for CS Classes

    monday_cs = {
        "title": "Monday 5/10: AP Create Task Day 11/14",
        "description": "Using this day to work on Create Task/ to review over AP Test.",
        "materials": [
            {"link": {"url": "https://myap.collegeboard.org/login"}},
            {"link": {"url": "https://www.youtube.com/watch?v=h51o7IqY4vQ"}},
            {"link": {"url": "https://drive.google.com/file/d/1CpQl4TYr6PYKuUM89IcGojcXb0yQGCQT/view?usp=drive_web&authuser=1"}},
            {"link": {"url": "https://drive.google.com/file/d/1tnEJwVStW5ld-m5DOE4CkcwQhEld1SN9/view?usp=drive_web&authuser=1"}},
            {"link": {"url": "https://classroom.google.com/c/MTI2NjQ1NjAyMDYw/m/MzI1ODMzMDk4ODc2/details"}},
        ],
        "workType": "ASSIGNMENT",
        "scheduledTime": date,
        "dueDate": dueAP,
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
    #assignment(service, computer_science_a_ap, monday_cs, "Computer Science A")

    tuesday_cs = {
        "title": "Tuesday 5/11: AP Create Task Day 12/14",
        "description": "Using this day to work on Create Task/ to review over AP Test.",
        "materials": [
            {"link": {"url": "https://myap.collegeboard.org/login"}},
            {"link": {"url": "https://www.youtube.com/watch?v=h51o7IqY4vQ"}},
            {"link": {"url": "https://drive.google.com/file/d/1CpQl4TYr6PYKuUM89IcGojcXb0yQGCQT/view?usp=drive_web&authuser=1"}},
            {"link": {"url": "https://drive.google.com/file/d/1tnEJwVStW5ld-m5DOE4CkcwQhEld1SN9/view?usp=drive_web&authuser=1"}},
            {"link": {"url": "https://classroom.google.com/c/MTI2NjQ1NjAyMDYw/m/MzI1ODMzMDk4ODc2/details"}},
        ],
        "workType": "ASSIGNMENT",
        "scheduledTime": date,
        "dueDate": dueAP,
        "dueTime": time,
        "maxPoints": 100,
        "state": "DRAFT",
    }

    assignment(
        service,
        computer_science_principles_ap,
        tuesday_cs,
        "Computer Science Principles",
    )

    wednesday_cs = {
        "title": "Wednesday 5/12: AP Create Task Day 13/14",
        "description": """ Using this day to work on Create Task/ to review over AP Test.""",
        "materials": [
            {"link": {"url": "https://myap.collegeboard.org/login"}},
            {"link": {"url": "https://www.youtube.com/watch?v=h51o7IqY4vQ"}},
            {"link": {"url": "https://drive.google.com/file/d/1CpQl4TYr6PYKuUM89IcGojcXb0yQGCQT/view?usp=drive_web&authuser=1"}},
            {"link": {"url": "https://drive.google.com/file/d/1tnEJwVStW5ld-m5DOE4CkcwQhEld1SN9/view?usp=drive_web&authuser=1"}},
            {"link": {"url": "https://classroom.google.com/c/MTI2NjQ1NjAyMDYw/m/MzI1ODMzMDk4ODc2/details"}},
        ],
        "workType": "ASSIGNMENT",
        "scheduledTime": date,
        "dueDate": dueAP,
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
    #assignment(service, computer_science_a_ap, wednesday_cs, "Computer Science A")

    thursday_cs = {
        "title": "Thursday 5/13: AP Practice EXAM",
        "description": """ Using this day to work on Create Task/ to review over AP Test.""",
        "materials": [
            {"link": {"url": "https://myap.collegeboard.org/login"}},
            {"link": {"url": "https://www.youtube.com/watch?v=h51o7IqY4vQ"}},
            {"link": {"url": "https://drive.google.com/file/d/1CpQl4TYr6PYKuUM89IcGojcXb0yQGCQT/view?usp=drive_web&authuser=1"}},
            {"link": {"url": "https://drive.google.com/file/d/1tnEJwVStW5ld-m5DOE4CkcwQhEld1SN9/view?usp=drive_web&authuser=1"}},
            {"link": {"url": "https://classroom.google.com/c/MTI2NjQ1NjAyMDYw/m/MzI1ODMzMDk4ODc2/details"}},
        ],
        "workType": "ASSIGNMENT",
        "scheduledTime": date,
        "dueDate": dueAP,
        "dueTime": time,
        "maxPoints": 100,
        "state": "DRAFT",
    }

    assignment(
        service,
        computer_science_principles_ap,
        thursday_cs,
        "Computer Science Principles",
    )

    friday_cs = {
        "title": "Friday 5/14: AP AP Practice EXAM",
        "description": """ Using this day to work on Create Task/ to review over AP Test.""",
        "materials": [
            {"link": {"url": "https://myap.collegeboard.org/login"}},
            {"link": {"url": "https://www.youtube.com/watch?v=h51o7IqY4vQ"}},
            {"link": {"url": "https://drive.google.com/file/d/1CpQl4TYr6PYKuUM89IcGojcXb0yQGCQT/view?usp=drive_web&authuser=1"}},
            {"link": {"url": "https://drive.google.com/file/d/1tnEJwVStW5ld-m5DOE4CkcwQhEld1SN9/view?usp=drive_web&authuser=1"}},
            {"link": {"url": "https://classroom.google.com/c/MTI2NjQ1NjAyMDYw/m/MzI1ODMzMDk4ODc2/details"}},
        ],
        "workType": "ASSIGNMENT",
        "scheduledTime": date,
        "dueDate": dueAP,
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
    #assignment(service, computer_science_a_ap, friday_cs, "Computer Science A")

    # Create drafts for Pre-Cal Class

    monday_cal = {
        "title": "Monday 5/10: Factoring Notes + Exit Ticket",
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
        "title": "Tuesday 5/11: Factoring Assignment",
        "description": "Will be up by Tuesday 8 am. I'm also AP testing",
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
        "title": "Wednesday 5/12: I'm AP testing",
        "description": "Work on what you need",
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
        "title": "Thursday 5/13: Campus Is STAAR testing",
        "description": "Work on what you need",
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
        "title": "Friday 5/14: Last week before finals, ask if you need me to reopen stuff",
        "description": "Work on what you need",
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
