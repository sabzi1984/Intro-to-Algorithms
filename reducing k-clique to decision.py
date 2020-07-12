def k_subsets(lst, k):
    if len(lst) < k:
        return []
    if len(lst) == k:
        return [lst]
    if k == 1:
        return [[i] for i in lst]
    return k_subsets(lst[1:],k) + list(map(lambda x: x + [lst[0]], k_subsets(lst[1:], k-1)))

# Checks if the given list of nodes forms a clique in the given graph.
def is_clique(G, nodes):
    for pair in k_subsets(nodes, 2):
        if pair[1] not in G[pair[0]]:
            return False
    return True

# Determines if there is clique of size k or greater in the given graph.
def k_clique_decision(G, k):
    nodes = list(G.keys())
    for i in range(k, len(nodes) + 1):

        for subset in k_subsets(nodes, k):
            if is_clique(G, subset):
                return True
    return False

def make_link(G, node1, node2):
    if node1 not in G:
        G[node1] = {}
    (G[node1])[node2] = 1
    if node2 not in G:
        G[node2] = {}
    (G[node2])[node1] = 1
    return G

def break_link(G, node1, node2):
    if node1 not in G:
        print ("error: breaking link in a non-existent node")
        return
    if node2 not in G:
        print ("error: breaking link in a non-existent node")
        return
    if node2 not in G[node1]:
        print ("error: breaking non-existent link")
        return
    if node1 not in G[node2]:
        print ("error: breaking non-existent link")
        return
    del G[node1][node2]
    del G[node2][node1]
    return G
    
def k_clique(G, k):
    if not k_clique_decision(G, k):
        return False
    Kclique=[]
    nodes=list(G.keys())
    for node1 in nodes:
        for node2 in nodes:
            if node1>node2:
                if node1 in G[node2]:
                    break_link(G, node1, node2)
                    if not k_clique_decision(G, k):
                        make_link(G, node1, node2)
    for node in G.keys():
        if len(G[node].keys())==k-1:
            Kclique.append(node) 
        
    return Kclique
G={1:{2:1, 3:1, 4:1}, 2:{1:1, 4:1}, 3:{1:1}, 4:{1:1, 2:1}}
print(k_clique(G, 3))
