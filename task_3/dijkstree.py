import heapq

class Graph:
    def __init__(self):
        self.edges = {}
        self.vertices = set()

    def add_edge(self, from_vertex, to_vertex, weight):
        if from_vertex not in self.edges:
            self.edges[from_vertex] = []
        if to_vertex not in self.edges:
            self.edges[to_vertex] = []
        self.edges[from_vertex].append((to_vertex, weight))
        self.vertices.add(from_vertex)
        self.vertices.add(to_vertex)

def dijkstra(graph, start_vertex):
    # Ініціалізація мін-купи та відстаней
    min_heap = [(0, start_vertex)]
    distances = {vertex: float('infinity') for vertex in graph.vertices}
    distances[start_vertex] = 0
    visited = set()

    while min_heap:
        current_distance, current_vertex = heapq.heappop(min_heap)

        if current_vertex in visited:
            continue

        visited.add(current_vertex)

        for neighbor, weight in graph.edges[current_vertex]:
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(min_heap, (distance, neighbor))

    return distances

# Приклад використання
if __name__ == "__main__":
    g = Graph()
    g.add_edge('A', 'B', 1)
    g.add_edge('A', 'C', 4)
    g.add_edge('B', 'C', 2)
    g.add_edge('B', 'D', 5)
    g.add_edge('C', 'D', 1)

    start_vertex = 'A'
    distances = dijkstra(g, start_vertex)
    print(f"Найкоротші відстані від вершини {start_vertex}:")
    for vertex, distance in distances.items():
        print(f"{vertex}: {distance}")
