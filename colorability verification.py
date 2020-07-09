def verify(G, cert, k):
    nodes1=set(G.keys())
    nodes2=set(cert.keys())
    if nodes1!=nodes2:
        return False
    colors=set(cert.values())
    for node in cert.keys():
        if cert[node] not in range(k):
            return False
    nodes=list(G.keys())
    while len(nodes)>0:
        current=nodes.pop(0)
        for node in G[current]:
            if cert[current]==cert[node]:
                return False
    return True



def make_link(G, node1, node2):
    if node1 not in G:
        G[node1] = {}
    (G[node1])[node2] = 1
    if node2 not in G:
        G[node2] = {}
    (G[node2])[node1] = 1
    return G


(a,b,c,d,e,f,g,h) = ('a','b','c','d','e','f','g','h')
cxns = [(a,c),(a,b),(c,d),(b,d),(d,e),(d,f),(e,g),(f,g),(f,h),(g,h)]

G = {}
for (x,y) in cxns: make_link(G,x,y)


cert = {}
for (node, color) in [(a,0),(b,1),(c,2),(d,0),(e,1),(f,2),(g,0),(h,1)]:
    cert[node] = color
print (verify(G,cert,3))
cert = {}
for (node, color) in [(a,0),(b,1),(c,2),(d,0),(e,0),(f,1),(g,2),(h,0)]:
    cert[node] = color
print (verify(G,cert,4))
