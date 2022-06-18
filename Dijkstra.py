from queue import PriorityQueue


class Graph:
    def __init__(self, num_of_vertices):
        self.v = num_of_vertices
        self.edges = [[-1 for i in range(num_of_vertices)] for j in range(num_of_vertices)]
        self.visited = []

    def add_edge(self, u, v, weight):
        self.edges[u][v] = weight
        self.edges[v][u] = weight


    def dijkstra(self, start_vertex):
        D = {v:float('inf') for v in range(self.v)}
        D[start_vertex] = 0

        pq = PriorityQueue()
        pq.put((0, start_vertex))

        while not pq.empty():
            (dist, current_vertex) = pq.get()
            self.visited.append(current_vertex)

            for neighbor in range(self.v):
                if self.edges[current_vertex][neighbor] != -1:
                    distance = self.edges[current_vertex][neighbor]
                    if neighbor not in self.visited:
                        old_cost = D[neighbor]
                        new_cost = D[current_vertex] + distance
                        if new_cost < old_cost:
                            pq.put((new_cost, neighbor))
                            D[neighbor] = new_cost
        return D

n = int (input("Ingrese la cantidad de recorridos disponibles en el grafo(nodo a nodo): "))
g = Graph(n)
for i in range (n):
    ni = int (input("Ingrese el nodo inicial: "))
    nf = int (input("Ingrese el nodo final: "))
    p = int (input("Ingrese el peso de la arista: "))
    g.add_edge(ni,nf,p)



nb = int (input("Ingrese el nodo con el que iniciara el recorrido: "))
D = g.dijkstra(nb)
print(D)



for vertex in range(len(D)):
    print(f"Distancia del vertice",g,"al vertice", vertex, "es", D[vertex])