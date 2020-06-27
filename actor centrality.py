import csv
import random
def read_graph(filename):
    tsv = csv.reader(open(filename), delimiter='\t')
    G = {}
    actors = set()
    for (actor, movie, year) in tsv:
        make_link(G, actor, movie + '(' + year + ')')
        actors.add(actor)
    return G, actors
def centrality(G, v):
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
    
    return (float(sum(distance_to_node.values())))/len(distance_to_node)  
def make_link(G, node1, node2):
    if node1 not in G:
        G[node1] = {}
    (G[node1])[node2] = 1
    if node2 not in G:
        G[node2] = {}
    (G[node2])[node1] = 1
    return G
def compute_centralities(G, actors):
    C = {}
    for actor in actors:
        C[actor] = centrality(G, actor)
    return C

def partition(C, v):
    smaller={}
    bigger={}
    middle={}
    for val in C.keys():
        if C[val] < C[v]:
            smaller[val]=C[val]
            
        if C[val] > C[v]:
            bigger[val]=C[val]
        if C[val]==C[v]:
            middle[val]=C[val] 
    return smaller,middle,bigger

def Kth_element(C,k):
    v=random.choice(C.keys())
    (left,middle,right)=partition(C, v)
    if len(left)>=k:
        return Kth_element(left,k)  
    elif len(left)+len(middle)>=k: return v, C[v]
    
        
    return Kth_element(right,k-len(left)-len(middle))
    
actors_graph, actors = read_graph("imdb-1.tsv")
centrality_of_actors=compute_centralities(actors_graph, actors)
print (Kth_element(centrality_of_actors,20))

