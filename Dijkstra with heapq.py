import heapq

def val(pair): return pair[0]
def id(pair): return pair[1]

def dijkstra_heapq(G,v):
    heap = [ [0, v] ]
    dist_so_far = {v:[0, v]}
    final_dist = {}
    while len(final_dist) < len(G):
        while True:
            w = heapq.heappop(heap)
            node = id(w)
            dist = val(w)
            if node != 'REMOVED':
                del dist_so_far[node]
                break

        final_dist[node] = dist
        for x in G[node]:
            if x not in final_dist:
                new_dist = dist + G[node][x]
                new_entry = [new_dist, x]
                if x not in dist_so_far:
                    dist_so_far[x] = new_entry
                    heapq.heappush(heap, new_entry)
                    
                elif new_dist < val(dist_so_far[x]):
                    dist_so_far[x][1] = "REMOVED"
                    dist_so_far[x] = new_entry
                    heapq.heappush(heap, new_entry)
    return final_dist
def make_link(G, node1, node2, w):
    if node1 not in G:
        G[node1] = {}
    if node2 not in G[node1]:
        (G[node1])[node2] = 0
    (G[node1])[node2] += w
    if node2 not in G:
        G[node2] = {}
    if node1 not in G[node2]:
        (G[node2])[node1] = 0
    (G[node2])[node1] += w
    return G
(a,b,c,d,e,f,g) = ('A', 'B', 'C', 'D', 'E', 'F', 'G')
triples = ((a,c,3),(c,b,10),(a,b,15),(d,b,9),(a,d,4),(d,f,7),(d,e,3), 
               (e,g,1),(e,f,5),(f,g,2),(b,f,1))
G = {}
for (i,j,k) in triples:
    make_link(G, i, j, k)
    
dist=dijkstra_heapq(G, a)
print(dist[e])
print(dist['E'])
