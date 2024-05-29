import sys

from classes.assign_instructors import assign_instructors
from classes.room import Room
from classes.tree_walker import TreeWalker
from testData import generateTestData

if __name__ == "__main__":

    participants, courses = generateTestData()

    assign_instructors(participants, courses)

    rooms = [
        Room(20),
        Room(19),
        Room(19),
        Room(19),
        Room(19),
        Room(19),
        Room(19),
        Room(15),
        Room(15),
        Room(15),
        Room(15),
        Room(15),
        Room(15),
        Room(15),
        Room(15),
        Room(10),
        Room(10),
        Room(10),
        Room(10),
        Room(10),
        Room(5),
    ]

    walker = TreeWalker(participants, courses, rooms)
    walker.start_walk()

    print()

    if not walker.best_node:
        print("it is not possible to assign everyone to a course")
        sys.exit(0)

    node = walker.best_node

    flow = node.flow
    cost = node.cost

    sink_node = 2000

    course_ids_that_take_place = []

    for course in courses:
        print(course.name)
        print("max participants: " + str(course.max_participants))

        course_flow_index = course.index + 1000

        if course_flow_index in flow and sink_node in flow[course_flow_index]:
            print("has participants: " + str(flow[course_flow_index][sink_node]))
            course_ids_that_take_place.append(course.index)
        else:
            print("empty")

        print()

    instructos_to_course = {}

    for course in courses:
        if course.index in course_ids_that_take_place:
            for instructor_id in course.instructor_ids:
                instructos_to_course[instructor_id] = course

    for participant in participants:

        print(participant.name)
        print("choices: " + str(participant.choices))

        if participant.index in instructos_to_course:
            print(f"participant is instructor for course: {instructos_to_course[participant.index].name}")
        else:
            for key, value in flow[participant.index].items():
                if value == 1:
                    assigned_course = key - 1000
                    print("is in course: " + str(assigned_course))

                    if assigned_course == participant.choices[2]:
                        print("this participant has only got the third choice")

        print()

    numbers = [course.max_participants for course in courses]
    print("total places was " + str(sum(numbers)))
    print("participants: " + str(len(participants)))
    print("cost: " + str(cost))
