import time
from pathlib import Path
from collections import defaultdict

from collections import defaultdict
import networkx as nx

def part_one(input):
    graph = defaultdict(set)
    for line in input.strip().split('\n'):
        node, connections = line.split(': ')
        for conn in connections.split():
            graph[node].add(conn)
            graph[conn].add(node)

    G = nx.Graph(graph)
    
    # Compute edge betweenness centrality
    edge_betweenness = nx.edge_betweenness_centrality(G)
    
    # Sort edges by betweenness centrality
    sorted_edges = sorted(edge_betweenness.items(), key=lambda x: x[1], reverse=True)
    
    # Remove the top 3 edges
    for (u, v), _ in sorted_edges[:3]:
        G.remove_edge(u, v)
    
    # Get the sizes of the two components
    components = list(nx.connected_components(G))
    if len(components) == 2:
        return len(components[0]) * len(components[1])
    else:
        return "Error: Did not find exactly two components"


def part_two(input):
    pass

if __name__ == "__main__":
    before = time.perf_counter()
    input = Path("input_day25.txt").read_text()
    # part 1
    print("1: " + str(part_one(input)))
    # part 2
    print("2: " + str(part_two(input)))
    print(f"Time: {time.perf_counter() - before:.6f} seconds")