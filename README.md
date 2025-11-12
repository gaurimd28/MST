# 🕸️ Minimum Spanning Tree (MST) using Kruskal’s & Prim’s Algorithms

A Python program to find the **Minimum Spanning Tree (MST)** of a connected weighted graph using  
👉 **Kruskal’s Algorithm** and 👉 **Prim’s Algorithm**.

This project demonstrates how two classic graph algorithms work to minimize total edge weight while connecting all vertices — ideal for **network design**, **campus layout**, or **infrastructure planning** problems.

---

## 🚀 Features

- Supports **weighted, undirected graphs**
- Implements both **Kruskal’s** (edge-based) and **Prim’s** (vertex-based) MST algorithms  
- Uses an **Adjacency Matrix** representation  
- Prints the **edges included in MST** with their weights  
- Simple and easy-to-understand Python code

---

## 🧩 Algorithms Overview

### 🔹 Kruskal’s Algorithm
- Works by **sorting edges** in ascending order of weight.  
- Adds edges one by one to the MST while ensuring **no cycle** is formed (using **Disjoint Set Union**).  
- Best suited for **sparse graphs**.

**Time Complexity:** `O(E log E)`  
**Space Complexity:** `O(V)`

---

### 🔹 Prim’s Algorithm
- Builds MST by growing a tree starting from an arbitrary vertex (here, vertex 0).  
- At each step, adds the **cheapest edge** that connects a new vertex.  
- Best suited for **dense graphs**.

**Time Complexity:** `O(V²)` (using adjacency matrix)  
**Space Complexity:** `O(V)`

---

## ⚙️ How It Works

Each vertex in this program represents a **campus department**, and the edges represent **paths or distances** between departments.

| Vertex | Department        |
|--------|-------------------|
| 0 | Computer Science |
| 1 | Mechanical |
| 2 | Electrical |
| 3 | Civil |
| 4 | IT |
| 5 | Architecture |

---

## 💻 Example Code

```python
# Example usage
if __name__ == "__main__":
    g = Graph(6)

    # Add edges with distances (in meters)
    g.add_edge(0, 1, 4)
    g.add_edge(0, 2, 3)
    g.add_edge(1, 2, 1)
    g.add_edge(1, 3, 2)
    g.add_edge(2, 3, 4)
    g.add_edge(3, 4, 2)
    g.add_edge(4, 5, 6)
    g.add_edge(3, 5, 3)

    print("Minimum Spanning Tree using Kruskal's algorithm:")
    mst_kruskal = g.kruskal_mst()
    for u, v, w in mst_kruskal:
        print(f"Edge {u} - {v} with distance {w}")

    print("\nMinimum Spanning Tree using Prim's algorithm:")
    mst_prim = g.prim_mst()
    for u, v, w in mst_prim:
        print(f"Edge {u} - {v} with distance {w}")

