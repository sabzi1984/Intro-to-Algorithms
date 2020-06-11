def find_eulerian_tour(graph):
    euler_tour=[]
    current_node=graph[0][0]
    euler_tour.append(current_node)
    
    while len(graph)>0:
        next_edges=[]
        for edge in graph:
            if current_node in edge:
                next_edges.append(edge)
        for edge in next_edges:
            if not would_disconnect(graph, edge):
                break
        graph.remove(edge)
        if edge[0]==current_node:
            current_node=edge[1]
        elif edge[1]==current_node:
            current_node=edge[0]
        euler_tour.append(current_node)             
    return euler_tour
def if_connected(graph):
    if len(graph) == 0:
        return True
    all_nodes = set(x[0] for x in graph).union(set(x[1] for x in graph))
    connected_set = set(graph[0])
    graph.remove(graph[0])
    while len(graph)>0:
        for edge in graph:
            n1, n2 = edge
            if n1 in connected_set and n2 not in connected_set:
                connected_set.add(n2)
                graph.remove(edge)
            elif n2 in connected_set and n1 not in connected_set:
                connected_set.add(n1)
                graph.remove(edge)
            else:
                graph.remove(edge)
        
    if connected_set == all_nodes:
        return True
    else:
        return False
def would_disconnect(graph, edge):
    new_graph = []
    
    for old_edge in graph:
        if old_edge != edge:
            new_graph.append(old_edge)
    if edge[1] in new_graph:
        return  not if_connected(new_graph)
    else:
        return True
graph=[(0, 1), (1, 5), (1, 7), (4, 5),(4, 8), (1, 6), (3, 7), (5, 9),(2, 4), (0, 4), (2, 5), (3, 6), (8, 9)]
print(find_eulerian_tour(graph))
