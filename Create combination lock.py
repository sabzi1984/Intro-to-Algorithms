# Generate a combination lock graph given a list of nodes
#

def make_link(G, node1, node2):
    if node1 not in G:
        G[node1] = {}
    (G[node1])[node2] = 1
    if node2 not in G:
        G[node2] = {}
    (G[node2])[node1] = 1
    return G

def create_combo_lock(nodes):
    G = {}
    for i in range (1,len(nodes)):
        make_link(G,nodes[0],nodes[i])
        if i<len(nodes)-1: make_link(G,nodes[i],nodes[i+1])
      
    return G
