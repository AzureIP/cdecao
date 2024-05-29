from classes.course import Course
from classes.node import Node
from classes.participant import Participant
from classes.restriction import Restriction
from classes.room import Room


class TreeWalker:

    def __init__(self, participants: list[Participant], courses: list[Course], rooms: list[Room]):
        self.participants = participants
        self.courses = courses
        self.sorted_rooms = rooms
        self.sorted_rooms.sort(key=lambda room: room.size, reverse=True)
        self.solved_nodes = 0
        self.best_node = None

    def start_walk(self):
        self._walk_deep([])

    def _walk_deep(self, restrictions: list[Restriction]):

        print("new node --------------")

        for restriction in restrictions:
            print(f"restricting course {restriction.courseId} to {restriction.max_participants} participants")

        node = Node(self.participants, self.courses, restrictions)
        node.solve()
        self.solved_nodes += 1
        print(self.solved_nodes)

        everyone_assigned = self.check_everyone_assigned(node)
        new_restrictions = self.restrict_courses(node, self.sorted_rooms)
        further_restriction_needed = len(new_restrictions) != 0

        if everyone_assigned and not further_restriction_needed:
            print(f"found a solution with score {node.cost}")

        if everyone_assigned and not further_restriction_needed and (self.best_node == None or node.cost < self.best_node.cost):
            print("found new best solution")
            self.best_node = node

        if further_restriction_needed and everyone_assigned:

            for restriction in new_restrictions:
                self._walk_deep(restrictions + [restriction])

    def restrict_courses(self, node: Node, sorted_rooms: list[Room]) -> list[Restriction]:

        # calculate course sizes
        flow = node.flow

        courses_with_size = []

        for course in self.courses:
            if course.index + 1000 in flow:
                number_instructors = len(course.instructor_ids)
                size = flow[course.index + 1000][2000] + number_instructors
                courses_with_size.append({
                    "size": size,
                    "index": course.index,
                    "instructors": number_instructors
                })

        courses_with_size.sort(key=lambda x: x["size"], reverse=True)

        new_restrictions = []

        # check if every course has a large enough room
        counter = 0
        for i, room in enumerate(sorted_rooms):
            if i > len(courses_with_size) - 1:
                break

            if room.size < courses_with_size[i]["size"]:
                # this course is too large
                print(f"adding option to shrink course {courses_with_size[i]["index"]} with size {courses_with_size[i]["size"]}")
                new_restrictions.append(
                    Restriction(courses_with_size[i]["index"], room.size - courses_with_size[i]["instructors"])
                )
                counter += 1

        if counter == 0 and len(courses_with_size) > len(sorted_rooms):
            for i in range(-3, 0):
                print(f"adding option to cancel course {courses_with_size[i]["index"]} with size {courses_with_size[i]["size"]}")
                new_restrictions.append(Restriction(courses_with_size[i]["index"], 0))

        return new_restrictions

    def check_everyone_assigned(self, node):

        flow = node.flow

        for participant in self.participants:

            if participant.index in node.instructos_which_courses_take_place:
                continue

            sum = 0
            for key, value in flow[participant.index].items():
                sum += value
            if sum == 0:
                print(participant.name + " was not assigned to a course")
                return False

        return True
