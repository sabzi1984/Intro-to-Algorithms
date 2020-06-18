def centrality_max(G, v):
    marked_node={}
    marked_node[v]=True
    distance_to_node={}
    distance_to_node[v]=0
    open_list=[v]
    while len(open_list)>0:
        current=open_list.pop(0)
        for neighbor in G[current].keys():
            if neighbor not in marked_node:
                marked_node[neighbor]=True
                open_list.append(neighbor)
                distance_to_node[neighbor]=distance_to_node[current]+1
    
    return max(distance_to_node.values())

#################
# Testing code
#
def make_link(G, node1, node2):
    if node1 not in G:
        G[node1] = {}
    (G[node1])[node2] = 1
    if node2 not in G:
        G[node2] = {}
    (G[node2])[node1] = 1
    return G

chain = ((1,2), (2,3), (3,4), (4,5), (5,6))
G = {}
for n1, n2 in chain:
    make_link(G, n1, n2)
print(centrality_max(G, 1))
