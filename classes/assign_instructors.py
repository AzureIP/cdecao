import random

from classes.course import Course
from classes.participant import Participant


def assign_instructors(participants: list[Participant], courses: list[Course]):

    participant_ids = [participant.index for participant in participants]
    random.shuffle(participant_ids)

    number_instructors_total = 0
    for course in courses:
        number_instructors = random.randint(1, 2)
        course.instructor_ids = participant_ids[0:number_instructors]
        participant_ids = participant_ids[number_instructors:]
        number_instructors_total += number_instructors

    print(f"instructors {number_instructors_total}")
    print()