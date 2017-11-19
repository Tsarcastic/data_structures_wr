"""Run Djikstra's algorithm to find shortest path on a graph."""


def djs_algorithm(start_pt, end_pt, node_list, edge_list):
    """Implement the algorithm."""
    nodelist = node_list  # ['s', 'a', 'b', 'c', 'd', 't']

    pred_list = {}
    for node in nodelist:
        pred_list[node] = ['', float('inf')]
    pred_list[start_pt] = ['', 0]  # {'s': ['', 0]}

    edges = edge_list
    # edges = {('s', 'a'): 2,
    #          ('s', 'b'): 1,
    #          ('a', 'c'): 8,
    #          ('a', 'b'): 4,
    #          ('b', 'a'): 2,
    #          ('b', 's'): 4,
    #          ('b', 'd'): 2,
    #          ('c', 'a'): 2,
    #          ('c', 'd'): 7,
    #          ('c', 't'): 4,
    #          ('d', 'b'): 1,
    #          ('d', 'c'): 11,
    #          ('t', 'c'): 3,
    #          ('t', 'd'): 5
    #          }
    for node in nodelist:

        for key in edges:
            if key[0] == node:
                tentative = edges[key] + pred_list[key[0]](1)
                if tentative < pred_list[key[1]](1):
                    pred_list[key[1]] = [key[0], tentative]
    dist = pred_list[end_pt](1)
    route = []
    cur = end_pt
    while cur:
        route.append(pred_list[cur](0))
        cur = pred_list[cur](0)

    return dist, route
