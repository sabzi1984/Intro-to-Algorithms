def make_link(graph,node1,node2):

    if node1 not in graph:
        graph[node1]={} 
    if node2 not in graph:
        graph[node2]={}
    graph[node1][node2]=1
    graph[node2][node1]=1
    return graph
graph={}
n=5
for i in range(n):
    make_link(graph,i,(i+1)%n)
#node count
print(len(graph))
# graph representation
print(graph)
#edge count
print(sum(len(graph[node])for node in graph.keys())/2)
