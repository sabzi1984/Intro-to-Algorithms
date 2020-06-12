import math
def make_link(graph,node1,node2):

    if node1 not in graph:
        graph[node1]={} 
    if node2 not in graph:
        graph[node2]={}
    graph[node2][node1]=1
    graph[node1][node2]=1
    return graph
graph={}
n=9
side=int(math.sqrt(n))
for i in range(side-1):
    for j in range (side-1):
        make_link(graph,(i,j),(i+1,j))
        make_link(graph,(i,j),(i,j+1))
        make_link(graph,(i+1,j),(i+1,j+1))
        make_link(graph,(i,j+1),(i+1,j+1))
print(len(graph))
print(sum([len(graph[node]) for node in graph.keys()])/2)
print(graph)
