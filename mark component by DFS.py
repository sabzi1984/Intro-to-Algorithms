def mark_component(G, node, marked):
    open_list = [node]
    total_marked = 1
    marked[node] = True
    while len(open_list) > 0:
        node = open_list.pop()
        for neighbor in G[node]:
            if neighbor not in marked:
                open_list.append(neighbor)
                marked[neighbor] = True
                total_marked+=1
    return total_marked
#########
# Code for testing
#
def make_link(G, node1, node2):
    if node1 not in G:
        G[node1] = {}
    (G[node1])[node2] = 1
    if node2 not in G:
        G[node2] = {}
    (G[node2])[node1] = 1
    return G


test_edges = [(1, 2), (2, 3),(3,4), (4, 5), (5, 6),(1,5),(1,6),(2,7)]
G = {}
for n1, n2 in test_edges:
    make_link(G, n1, n2)
marked = {}
print(mark_component(G, 1, marked))
