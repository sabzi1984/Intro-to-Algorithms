def k_subsets(lst, k):
    if len(lst) < k:
        return []
    if len(lst) == k:
        return [lst]
    if k == 1:
        return [[i] for i in lst]
    return k_subsets(lst[1:],k) +list( map(lambda x: x + [lst[0]], k_subsets(lst[1:], k-1)))

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
        for subset in k_subsets(nodes, i):
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
   
# This function should use the k_clique_decision function
# to solve the independent set decision problem
def independent_set_decision(H, s):
    nodes=list(H.keys())
    G={}
    if s==1:
        return True
    for node1 in nodes:
        for node2 in nodes:
            if node1>node2:
                if node1 not in H[node2]:
                    make_link(G, node1, node2)
    if k_clique_decision(G, s):
        return True
    return False    
         
       
             
H={1:{2:1, 3:1}, 2:{1:1}, 3:{1:1}, 4:{}}
print(independent_set_decision(H, 3))
