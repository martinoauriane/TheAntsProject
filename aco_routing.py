# Aco_routing is a package to find the shortest path in a graph using the Ant Colony Optimization (ACO).
# The Ant colony Optimization algorithm is a probabilistic technique for solving computational problems such as finding the shortest path from node A to node I 
# in a graph. 

# aco_routing.Ant
# An Ant that traverses the graph.


from aco_routing import ACO
import networkx as nx

Graph = nx.DiGraph()
Graph.add_edge("A", "B", cost=2)
Graph.add_edge("B", "C", cost=2)
Graph.add_edge("A", "H", cost=2)
Graph.add_edge("H", "G", cost=2)
Graph.add_edge("C", "F", cost=1)
Graph.add_edge("F", "G", cost=1)
Graph.add_edge("G", "F", cost=1)
Graph.add_edge("F", "C", cost=1)
Graph.add_edge("C", "D", cost=10)
Graph.add_edge("E", "D", cost=2)
Graph.add_edge("G", "E", cost=2)

# define the desired parameters using the aco variable and find the shortest path and cost between start node and end node
# ACO = Ant Colony Optimization Algorithm
init_algorithm = ACO(Graph, ant_max_steps=100, num_iterations=100, ant_random_spawn=True)

shortest_path, lowest_cost = init_algorithm.find_shortest_path(
    source="A",
    destination="D",
    number_ants=100,
)

