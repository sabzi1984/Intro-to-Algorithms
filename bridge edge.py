def make_link_simple(G, node1, node2):
    if node1 not in G:
        G[node1] = {}
    (G[node1])[node2] = 1
    if node2 not in G:
        G[node2] = {}
    (G[node2])[node1] = 1
    return G
def make_link(G, node1, node2, color):
    if node1 not in G:
        G[node1] = {}
    (G[node1])[node2] = color
    if node2 not in G:
        G[node2] = {}
    (G[node2])[node1] = color
    return G
def create_rooted_spanning_tree(G, root):
    
    open_list = [root]
    S = {root:{}}
    while len(open_list) > 0:
        current = open_list.pop()
       
        for neighbor in G[current]:
            if neighbor not in S:
                make_link(S, current, neighbor, 'green')
                open_list.append(neighbor)
            else:
                
                if current not in S[neighbor]:
                    make_link(S, current, neighbor, 'red')
    return S
def get_children(S, root, parent):
    n=[]   
    for node, edge in S[root].items():
        if node != parent and edge == 'green' :  
            n.append(node)
    return n
def get_children_all(S, root, parent):
    
    green = []
    red = []
    for n, e in S[root].items():
        if n == parent:
            continue
        if e == 'green':
            green.append(n)
        if e == 'red':
            red.append(n)
    return green, red
def post_order_helper(S, root, parent, val, po):
    children = get_children(S, root, parent)    
    for c in children:
        val = post_order_helper(S, c, root, val, po)
    po[root] = val
    return val + 1

def post_order(S, root):
    po = {}
    post_order_helper(S, root, None, 1, po)
    return po
def _general_post_order(S, root, parent, po, gpo, comp):
    green, red = get_children_all(S, root, parent)
    val = po[root]
    for c in green:
        test = _general_post_order(S, c, root, po, gpo, comp)
        if comp(val, test):
            val = test
    for c in red:
        test = po[c]
        if comp(val, test):
            val = test
    gpo[root] = val
    return val
def lowest_post_order(S, root, po):
    lpo = {}
    _general_post_order(S, root, None, po, lpo, lambda x, y: x > y) 
    return lpo
def highest_post_order(S, root, po):
    hpo = {}
    _general_post_order(S, root, None, po, hpo, lambda x, y: x < y)
    return hpo
def number_of_descendants_help(S, root, parent, nd):
    children = get_children(S, root, parent)
    nd_val = 1
    for c in children:
        nd_val += number_of_descendants_help(S, c, root, nd)
    nd[root] = nd_val
    return nd_val
def number_of_descendants(S, root):
    nd = {}
    number_of_descendants_help(S, root, None, nd)
    return nd
def bridge_edges(G, root):
    S = create_rooted_spanning_tree(G, root)
    po = post_order(S, root)
    nd = number_of_descendants(S, root)
    lpo = lowest_post_order(S, root, po)
    hpo = highest_post_order(S, root, po)
    bridges = []
    open_list = [(root, None)]
    while len(open_list) > 0:
        node, parent = open_list.pop()
        for child in get_children(S, node, parent):
            if hpo[child] <= po[child] and lpo[child] > (po[child] - nd[child]):
                bridges.append((node, child))
            open_list.append((child, node))
    return bridges

edges = [('a', 'g'), ('a', 'd'), ('g', 'c'), ('g', 'd'), 
             ('b', 'f'), ('f', 'e'), ('e', 'h'), ('d','h')]
G = {}
for v1, v2 in edges:
    graph=make_link_simple(G, v1, v2)
print(bridge_edges(graph, 'a'))
