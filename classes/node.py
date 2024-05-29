import networkx as nx

from classes.course import Course
from classes.participant import Participant
from classes.restriction import Restriction


class Node:


    def __init__(self, participants: list[Participant], courses: list[Course], course_restrictions: list[Restriction]):

        self.participants = participants
        self.courses = courses
        self.course_restrictions = course_restrictions
        self.cost = None
        self.flow = None
        self.instructos_which_courses_take_place = None


    def solve(self):
        graph, start_node, sink_node = self.generateGraph()

        self.flow = nx.max_flow_min_cost(graph, start_node, sink_node)
        self.cost = nx.cost_of_flow(graph, self.flow)

    def generateGraph(self):

        start_node = 4000
        sink_node = 2000

        course_size_dict = {}

        for restriction in self.course_restrictions:
            if restriction.courseId in course_size_dict:
                if course_size_dict[restriction.courseId] > restriction.max_participants:
                    course_size_dict[restriction.courseId] = restriction.max_participants
            else:
                course_size_dict[restriction.courseId] = restriction.max_participants

        course_ids_that_take_place = []

        for course in self.courses:
            if course.index in course_size_dict:
                if course.min_participants <= course_size_dict[course.index]:
                    course_ids_that_take_place.append(course.index)
            else:
                course_ids_that_take_place.append(course.index)

        self.instructos_which_courses_take_place = []

        for course in self.courses:
            if course.index in course_ids_that_take_place:
                self.instructos_which_courses_take_place.extend(course.instructor_ids)

        edge_list = []

        for participant in self.participants:

            if participant.index in self.instructos_which_courses_take_place:
                continue

            edge_list.append(
                [start_node, participant.index, {"capacity": 1}]
            )

            for choice, weight in zip(participant.choices, [0, 1, 2]):
                if choice in course_ids_that_take_place:

                    edge_list.append(
                        (participant.index, choice + 1000, {"capacity": 1, "weight": weight})
                    )

        for course in self.courses:
            if course.index not in course_ids_that_take_place:
                continue

            if course.index in course_size_dict:
                max_participants = course_size_dict[course.index]
            else:
                max_participants = course.max_participants

            edge_list.append(
                (course.index + 1000, sink_node, {"capacity": max_participants})
            )

        G = nx.DiGraph()
        G.add_edges_from(edge_list)

        return G, start_node, sink_node






