import networkx as nx

from classes.course import Course
from classes.participant import Participant


def generateGraph(participants: list[Participant], courses: list[Course]):

    required_payload_nodes = len(participants) + len(courses)

    start_node = required_payload_nodes + 1
    sink_node = 2000

    edge_list = []

    for participant in participants:
        edge_list.append(
            [start_node, participant.index, {"capacity": 1}]
        )

        for choice, weight in zip(participant.choices, [0, 1, 2]):
            edge_list.append(
                (participant.index, choice + 1000, {"capacity": 1, "weight": weight})
            )

    for course in courses:
        edge_list.append(
            (course.index + 1000, sink_node, {"capacity": course.max_participants})
        )

    G = nx.DiGraph()
    G.add_edges_from(edge_list)

    return G, start_node, sink_node





