def make_link(graph,node1,node2):
    if node1 not in graph:
        graph[node1]={}
    if node2 not in graph:
        graph[node2]={}
    graph[node1][node2]=1
    graph[node2][node1]=1
    return graph
def star_network(n):
    # return number of edges
    graph={}
    for i in range(1,n):
        make_link(graph,0,i)
    
    return sum(len(graph[node]) for node in graph.keys())/2
print(star_network(7))
