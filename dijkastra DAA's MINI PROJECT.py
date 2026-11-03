import networkx as nx
import matplotlib.pyplot as plt

graph = nx.Graph()
roads = [
    ("Collage", "Library", 1),
    ("Collage", "Market", 4),
    ("Collage", "Park", 7),
    ("Collage", "Home", 2),
    ("Home", "Park", 1),
    ("Home", "Hospital", 2),
    ("Library", "Hospital", 3),
    ("Library", "Park", 5),
    ("Market", "Hospital", 6),
    ("Hospital", "Park", 2)
]
graph.add_weighted_edges_from(roads)
print("Available locations:", list(graph.nodes))
start = input("Enter starting location: ").strip().title()
destination = input("Enter destination: ").strip().title()

if start not in graph or destination not in graph:
    print("Invalid location!")
else:
    # Standard linear function execution
    route = nx.dijkstra_path(graph, start, destination, weight="weight")
    distance = nx.dijkstra_path_length(graph, start, destination, weight="weight")
    print("\nShortest Route:", " - ".join(route))
    print("Total Distance:", distance, "km")
    
    pos = nx.spring_layout(graph)
    route_edges = []
    i = 0
    while i < len(route) - 1:
        route_edges.append((route[i], route[i+1]))
        i += 1

    # Standard primary color profile configuration 
    node_colors = []
    for node in graph.nodes:
        if node == start:
            node_colors.append("green")
        elif node == destination:
            node_colors.append("orange")
        else:
            node_colors.append("blue")
    nx.draw(graph, pos, with_labels=True, node_color=node_colors, node_size=2000, edge_color="gray")

    edge_labels = nx.get_edge_attributes(graph, "weight")
    nx.draw_networkx_edge_labels(graph, pos, edge_labels=edge_labels)
    
    nx.draw_networkx_edges(graph, pos, edgelist=route_edges, edge_color="red", width=4)
    
    # Basic student-style string concatenation for title mapping
    plt.title("Shortest Route from " + start + " to " + destination + " (" + str(distance) + " km)")
    plt.show()
