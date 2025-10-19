import sys

start_node=sys.argv[1]
end_node=sys.argv[2]

distances = {
    "A": {"B": {"distance": 0.5, "pheromone": 0},
          "C": {"distance": 0.5, "pheromone": 0}},
    "B": {"A": {"distance": 0.5, "pheromone": 0}},
    "C": {"A": {"distance": 0.5, "pheromone": 0}}
}

pheromone_trail = 0.5
evaporation_rate = 0.1

def evaporation(pheromone):
    return pheromone * (1 - evaporation_rate)


def ant_strategy(current_node, graph, visited):
    shortest_distance = float('inf')
    closest_neighbor = None
    
    for neighbor, data in graph[current_node].items():
        if neighbor in visited:
            continue
        distance_to_neighbor = data["distance"] + evaporation(data["pheromone"]) / 2
        if distance_to_neighbor < shortest_distance:
            shortest_distance = distance_to_neighbor
            closest_neighbor = neighbor
    graph[current_node][closest_neighbor]["pheromone"] += pheromone_trail
    return closest_neighbor


def process_search_path(start_node, end_node, graph):
    current_node = start_node
    path = [current_node]
    visited = set(start_node)

    for i in range(100):
        next_node = ant_strategy(current_node, graph, visited)
        if not next_node:  
            print("Aucun chemin trouvé !")
            break
        current_node = next_node
        path.append(current_node)
        visited.add(current_node)

        if current_node == end_node:
            print("End node found. Shortest path is:")
            return " - ".join(path)
    
    return "Aucun chemin trouvé."

print(process_search_path(start_node, end_node, distances))