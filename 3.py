graph = {}
graph["start"] = {}
graph["start"]["a"] = 6
graph["start"]["b"] = 2

graph["a"] = {}
graph["a"]["end"] = 1

graph["b"] = {}
graph["b"]["a"] = 3
graph["b"]["end"] = 5
graph["end"] = {}


infinity = float("inf")
costs = {}
costs["a"] = 6
costs["b"] = 2
costs["end"] = infinity


parents = {}
parents["a"] = "start"
parents["b"] = "start"
parents["end"] = None


processed = []



def find_lowest_cost_node(costs):

    lowest_cost = infinity
    lowest_cost_node = None

    for node in costs:

        if not node in processed:

            if costs[node] < lowest_cost:
                lowest_cost = costs[node]
                lowest_cost_node = node
    return lowest_cost_node



def find_shortest_path():
    node = "end"
    shortest_path = ["end"]
    while parents[node] != "start":
        shortest_path.append(parents[node])
        node = parents[node]
    shortest_path.append("start")
    return shortest_path



def dijkstra():
    node = find_lowest_cost_node(costs)
    while node is not None:
        cost = costs[node]
        neighbors = graph[node]
        for n in neighbors.keys():
            new_cost = cost + neighbors[n]
            if new_cost < costs[n]:
                costs[n] = new_cost
                parents[n] = node
        processed.append(node)
        node = find_lowest_cost_node(costs)
    shortest_path = find_shortest_path()
    shortest_path.reverse()
    print(shortest_path)
