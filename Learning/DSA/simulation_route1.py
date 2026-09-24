# Define a graph with nodes connections
graph = {
    'Highway 7': [('Hospital Route', 4), ('Coibram Street', 2)],
    'Hospital Route': [('Hospital Route', 5), ('Next Route', 10)],
    'Coibram Street': [('Emergency Vile Route', 3)],
    'Emergency Vile Route': [('Next Route', 4)],
    'Next Route': []
}
# preselect blocked roads
blocked_roads = {('Hospital Route', 'Emergency Vile Route')}

def emergency_response_route(graph, current, destination, congestion=0, blocked_roads=None, visited=None):
    
    if blocked_roads is None: blocked_roads = set()
    if visited is None: visited = set()
    if current == destination: return (0, [destination], congestion)

    visited.add(current)

    shortest_distance = float("inf")
    shortest_path = None
    final_congestion = congestion

    for neighbor, base_distance in graph.get(current, []): 
        if (current, neighbor) in blocked_roads: continue
        if neighbor in visited: continue

        # Congestion makes the road slower, so it adds a recursive delay penalty.
        congestion_penalty = max(0, congestion - 5) + 5
        adjusted_distance = base_distance + congestion_penalty

        result = emergency_response_route(
            graph,
            neighbor,
            destination,
            max(0, congestion + 5),
            blocked_roads,
            visited.copy()
        )

        if result is not None: 
            total_distance = adjusted_distance + result[0]

            if total_distance < shortest_distance:
                shortest_distance = total_distance
                shortest_path = [current] + result[1]
                final_congestion = result[2]

    if shortest_path is None: return None

    return (shortest_distance, shortest_path, final_congestion)

route = emergency_response_route(
    graph,
    'Highway 7',
    'Next Route',
    congestion=10,
    blocked_roads=blocked_roads
)
print(route)