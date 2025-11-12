class Graph:
    def __init__(self, vertices):
        self.V = vertices
        # Initialize adjacency matrix with 0 (no edge)
        self.graph = [[0] * vertices for _ in range(vertices)]

    def add_edge(self, u, v, w):
        # Undirected graph
        self.graph[u][v] = w
        self.graph[v][u] = w

    # Helper function for Kruskal's algorithm: Find set of an element i
    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    # Helper function for Kruskal's algorithm: Union of two sets
    def union(self, parent, rank, x, y):
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)

        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else:
            parent[yroot] = xroot
            rank[xroot] += 1

    # a) Kruskal's algorithm
    def kruskal_mst(self):
        edges = []
        # Extract all edges
        for i in range(self.V):
            for j in range(i, self.V):  # to avoid duplicates since undirected
                if self.graph[i][j] != 0:
                    edges.append((self.graph[i][j], i, j))

        # Sort edges based on weight
        edges.sort(key=lambda x: x[0])

        parent = []
        rank = []

        # Create V subsets with single elements
        for node in range(self.V):
            parent.append(node)
            rank.append(0)

        mst = []
        e = 0  # number of edges in MST
        i = 0  # index for sorted edges

        while e < self.V - 1 and i < len(edges):
            w, u, v = edges[i]
            i += 1
            x = self.find(parent, u)
            y = self.find(parent, v)

            if x != y:
                e += 1
                mst.append((u, v, w))
                self.union(parent, rank, x, y)

        return mst

    # b) Prim's algorithm
    def prim_mst(self):
        key = [float('inf')] * self.V
        parent = [None] * self.V
        key[0] = 0  # Start from vertex 0
        mstSet = [False] * self.V

        for _ in range(self.V):
            # Pick the minimum key vertex not yet included in MST
            min_key = float('inf')
            u = -1
            for v in range(self.V):
                if not mstSet[v] and key[v] < min_key:
                    min_key = key[v]
                    u = v

            mstSet[u] = True

            # Update key and parent for adjacent vertices
            for v in range(self.V):
                if self.graph[u][v] and not mstSet[v] and self.graph[u][v] < key[v]:
                    key[v] = self.graph[u][v]
                    parent[v] = u

        mst = []
        for i in range(1, self.V):
            mst.append((parent[i], i, self.graph[i][parent[i]]))
        return mst

# Example usage
if __name__ == "__main__":
    # Suppose campus departments: 0-Computer Science, 1-Mechanical, 2-Electrical,
    # 3-Civil, 4-IT, 5-Architecture

    g = Graph(6)

    # Add edges with distances (example values in meters)
    g.add_edge(0, 1, 4)  # CS - Mechanical
    g.add_edge(0, 2, 3)  # CS - Electrical
    g.add_edge(1, 2, 1)  # Mechanical - Electrical
    g.add_edge(1, 3, 2)  # Mechanical - Civil
    g.add_edge(2, 3, 4)  # Electrical - Civil
    g.add_edge(3, 4, 2)  # Civil - IT
    g.add_edge(4, 5, 6)  # IT - Architecture
    g.add_edge(3, 5, 3)  # Civil - Architecture

    print("Minimum Spanning Tree using Kruskal's algorithm:")
    mst_kruskal = g.kruskal_mst()
    for u, v, w in mst_kruskal:
        print(f"Edge {u} - {v} with distance {w}")

    print("\nMinimum Spanning Tree using Prim's algorithm:")
    mst_prim = g.prim_mst()
    for u, v, w in mst_prim:
        print(f"Edge {u} - {v} with distance {w}")
