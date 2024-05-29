
import networkx as nx
# from networkx.algorithms.flow import maximum_flow

if __name__ == "__main__":



    G = nx.DiGraph()

    G.add_edges_from(
        [
            (1, 2, {"capacity": 12, "weight": 4}),
            (1, 3, {"capacity": 20, "weight": 6}),
            (2, 3, {"capacity": 6, "weight": -3}),
            (2, 6, {"capacity": 14, "weight": 1}),
            (3, 4, {"weight": 9}),
            (3, 5, {"capacity": 10, "weight": 5}),
            (4, 2, {"capacity": 19, "weight": 13}),
            (4, 5, {"capacity": 4, "weight": 0}),
            (5, 7, {"capacity": 28, "weight": 2}),
            (6, 5, {"capacity": 11, "weight": 1}),
            (6, 7, {"weight": 8}),
            (7, 4, {"capacity": 6, "weight": 6}),
        ]
    )

    max_flow_min_cost_result = nx.max_flow_min_cost(G, 1, 7)

    cost = nx.cost_of_flow(G, max_flow_min_cost_result)

    # maximalAchivedFlow = maximum_flow(G, 1, 7)[1]

    # var = nx.cost_of_flow(G, maximalAchivedFlow) >= minimalCostOfCalculatedFlow


    # mincostFlowValue = sum(max_flow_min_cost_result[u][7] for u in G.predecessors(7)) - sum(max_flow_min_cost_result[7][v] for v in G.successors(7))

    # var = mincostFlowValue == nx.maximum_flow_value(G, 1, 7)

    G2 = nx.DiGraph()

    G2.add_edges_from(
        [
            (1, 2, {"capacity": 1}),
            (1, 3, {"capacity": 1}),
            (1, 4, {"capacity": 1}),
            (1, 5, {"capacity": 1}),
            (1, 6, {"capacity": 1}),

            (2, 7, {"capacity": 1, "weight": 0}),
            (2, 8, {"capacity": 1, "weight": 1}),

            (3, 7, {"capacity": 1, "weight": 0}),
            (3, 8, {"capacity": 1, "weight": 1}),

            (4, 7, {"capacity": 1, "weight": 0}),
            (4, 8, {"capacity": 1, "weight": 1}),

            (5, 7, {"capacity": 1, "weight": 0}),
            (5, 8, {"capacity": 1, "weight": 1}),

            (6, 7, {"capacity": 1, "weight": 1}),
            (6, 8, {"capacity": 1, "weight": 0}),

            (7, 9, {"capacity": 2}),
            (8, 9, {"capacity": 3}),

        ]
    )

    flow = nx.max_flow_min_cost(G2, 1, 9)

    cost2 = nx.cost_of_flow(G2, flow)






    print("hi")