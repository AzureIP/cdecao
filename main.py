import networkx as nx

from graph_generator import generateGraph
from testData import generateTestData

if __name__ == "__main__":


    participants, courses = generateTestData()

    graph, start_node, sink_node = generateGraph(participants, courses)

    flow = nx.max_flow_min_cost(graph, start_node, sink_node)

    cost = nx.cost_of_flow(graph, flow)



    for participant in participants:

        print(participant.name)
        print("choices: " + str(participant.choices))

        for key, value in flow[participant.index].items():
            if value == 1:
                print("is in course: " + str(key - 1000))
        print()

    for course in courses:
        print(course.name)
        print("max participants: " + str(course.max_participants))

        if sink_node in flow[course.index + 1000]:
            print("has participants: " + str(flow[course.index + 1000][sink_node]))
        else:
            print("empty")

        print()

    numbers = [course.max_participants for course in courses]
    print("total places was " + str(sum(numbers)))
    print("participants: " + str(len(participants)))
    print("cost: " + str(cost))












