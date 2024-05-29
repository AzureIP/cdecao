import random
from random import sample, randint

from classes.course import Course
from classes.participant import Participant


def generateTestData():
    number_of_courses = random.randint(18, 25)
    number_participants = 270

    courseNumberList = [i for i in range(1, number_of_courses + 1)]

    participants = []

    for i in range(1, number_participants + 1):
        participants.append(
            Participant(i, i, f"Participant {i}", sample(courseNumberList, 3))
        )

    courses = []

    for courseID in courseNumberList:
        courses.append(
            Course(courseID, courses, f"course {courseID}", randint(6, 20), randint(4, 5))
        )

    sum = 0
    for course in courses:
        sum += course.max_participants

    print(f"number_participants {number_participants}")
    print(f"number_of_courses {number_of_courses}")
    print(f"places in courses {sum}")

    return participants, courses
