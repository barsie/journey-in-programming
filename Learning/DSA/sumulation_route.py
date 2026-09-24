graph = {
    'Highway 7': [('Hospital Route', 4), ('Coibram Street', 2)],
    'Hospital Route': [('Hospital Route', 5), ('Next Route', 10)],
    'Coibram Street': [('Emergency Vile Route', 3)],
    'Emergency Vile Route': [('Next Route', 4)],
    'Next Route': []
}

blocked_roads = {('Hospital Route', 'Emergency Vile Route')}


def shortest_route(graph, current, destination, visited=None):
    if visited is None:
        visited = set()

    if current == destination:
        return (0, [destination])

    visited.add(current)

    shortest_distance = float('inf')
    shortest_path = None

    for neighbor, distance in graph[current]:

        if (current, neighbor) in blocked_roads:
            continue

        if neighbor not in visited:

            result = shortest_route(
                graph,
                neighbor,
                destination,
                visited.copy()
            )

            if result:

                total_distance = distance + result[0]

                if total_distance < shortest_distance:
                    shortest_distance = total_distance
                    shortest_path = [current] + result[1]

    if shortest_path:
        return shortest_distance, shortest_path

    return None


route = shortest_route(graph, 'Highway 7', 'Next Route')

print(route)


def simulate_traffic_congention(level, congestion):
    """Simulate traffic congestion recursion."""

    if level == 0:
        print("Predicted congestion:", congestion)
        return

    # Traffic worsens
    simulate_traffic_congention(level - 1, congestion + 10) #recursion here

    # Traffic improves
    simulate_traffic_congention(level - 1, max(0, congestion - 5)) #recursion here

simulate_traffic_congention(1, 5)


# Complet merged function

def emergency_response_route(
    graph, 
    current, 
    destination, 
    congestion=0, 
    blocked_roads=None, 
    visited=None
):
    
    if blocked_roads is None:
        blocked_roads = set()
    if visited is None:
        visited = set()

    if current == destination:
        return (0, [destination], congestion)

    visited.add(current)

    shortest_distance = float("inf")
    shortest_path = None
    final_congestion = congestion

    for neighbor, base_distance in graph.get(current, []):
        if (current, neighbor) in blocked_roads:
            continue

        if neighbor in visited:
            continue

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

    if shortest_path is None:
        return None

    return (shortest_distance, shortest_path, final_congestion)


route = emergency_response_route(
    graph,
    'Highway 7',
    'Next Route',
    congestion=10,
    blocked_roads=blocked_roads
)

print(route)