def make_link(graph,node1,node2):

    if node1 not in graph:
        graph[node1]={} 
    if node2 not in graph:
        graph[node2]={}
    graph[node1][node2]=1
    graph[node2][node1]=1
    return graph
def clique(n):
    graph={}
   
    for i in range(n):
        for j in range (n):
            if i!=j: make_link(graph,i,j)
    
    #edge count
    return int((sum(len(graph[i])for i in graph.keys())/2))
for i in range(1,10):
    print(i,clique(i))
