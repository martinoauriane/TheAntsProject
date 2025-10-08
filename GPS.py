node_indexes = {
   0: "Z",
   1: "Y",
   2: "X", 
   3: "A", 
   4:  "C",
}

manhattan_distances = [
  [0, 5, 10, 3, 12], 
  [5, 0, 9, 2, 11],
  [10, 2, 0, 8, 14],
  [3, 2, 8, 0, 17], 
  [12, 11, 14, 17, 0],  
]

start_node = "Z"
end_node = "X"

def get_driver_position():
  return lat, long

def convert_latlong(lat, long):
  lat, long 
  return "Z"

def closest_neighboor(current_node, visited):
  x_node = node_indexes[current_node]
  shortest_distance = float('inf')
  closest_neighbor = ''
  for i in range(len(manhattan_distances[x_node])):
    if i == x_node : 
      continue 
    neighbor = node_indexes[i]
    if neighbor in visited: 
      continue
    neighbor_distance = manhattan_distances[x_node][i]
    if neighbor_distance < shortest_distance:
      shortest_distance = neighbor_distance
      closest_neighboor = node_indexes[i]
  return shortest_distance, closest_neighboor


def find_shortest_path(current_node, end_node):
  total_distance = 0
  visited = set([current_node])
  path= [current_node]
  while current_node != end_node: 
    driver_position = get_driver_position()
    current_node = driver_position
    shortest_distance, best_neighboor = closest_neighboor(current_node)
    current_node = best_neighboor
    total_distance += shortest_distance
    visited.add(best_neighboor)
    path.append(current_node)
    if best_neighboor == end_node:
      print(f"Destination attained in {total_distance/60} hours")
  return path, total_distance

def implement_GPS():
  current_node = convert_latlong(lat, long)
  end = input()
  destination = convert_latlong(end)
  trajectory, travel_time = find_shortest_path(current_node, destination)
  print(f"In order to get to {destination}, please first take {", then ".join(trajectory)}")