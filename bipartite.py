# Write a function, `bipartite` that
# takes as input a graph, `G` and tries
# to divide G into two sets where 
# there are no edges between elements of the
# the same set - only between elements in
# different sets.
# If two sets exists, return one of them
# or `None` otherwise
# Assume G is connected
import random
def bipartite(G):
        random_node=random.choice(list(G.keys()))
        open_list=set(random_node)
        g1=set()
        g1.add(random_node)
        cheked_no_edge={}
        
        
        while len(open_list)>0:
                node=list(open_list).pop(0)
                open_list.remove(node)
                if node not in cheked_no_edge.keys():
                        cheked_no_edge[node]={}
                        
                neighbors=list(G[node].keys())
                for neighbor in neighbors:
                        neighbors_of_neighbors=list(G[neighbor].keys())
                        for neighbor2 in neighbors_of_neighbors:
                                if neighbor2 not in cheked_no_edge.keys():
                                        cheked_no_edge[neighbor2]={}
                                if node!=neighbor2:
                                        if neighbor2 not in cheked_no_edge[node]:
                                                if node in G[neighbor2].keys():
                                                        return None
                                                cheked_no_edge[node][neighbor2]=True
                                                cheked_no_edge[neighbor2][node]=True
                                                
                                                open_list.add(neighbor2)
                                                g1.add(neighbor2)                               
        for node in g1:
                for neighbor in G[node]:
                        if neighbor in g1:
                                return None
                return g1
        
 
G1 = {'a': {'s': 1}, 'c': {'h': 1, 'b': 1, 'm': 1, 'e': 1, 'l': 1}, 'b': {'c': 1, 'o': 1}, 'e': {'c': 1, 'o': 1}, 'd': {'q': 1, 'p': 1, 'k': 1, 't': 1, 'o': 1}, 'g': {'k': 1, 'o': 1}, 'f': {'i': 1, 's': 1, 't': 1}, 'i': {'q': 1, 'f': 1}, 'h': {'c': 1}, 'k': {'v': 1, 'd': 1, 'g': 1, 'n': 1}, 'j': {'t': 1}, 'm': {'q': 1, 's': 1, 'c': 1, 't': 1}, 'l': {'q': 1, 'p': 1, 'c': 1, 's': 1}, 'o': {'b': 1, 'e': 1, 'd': 1, 'g': 1, 'v': 1}, 'n': {'p': 1, 'k': 1}, 'q': {'i': 1, 'm': 1, 'd': 1, 'l': 1}, 'p': {'n': 1, 'r': 1, 'l': 1, 'd': 1, 'v': 1}, 's': {'a': 1, 'f': 1, 'm': 1, 'l': 1, 'u': 1, 'v': 1}, 'r': {'p': 1, 't': 1}, 'u': {'s': 1}, 't': {'r': 1, 'm': 1, 'd': 1, 'f': 1, 'j': 1}, 'v': {'p': 1, 'k': 1, 's': 1, 'o': 1}}

g1 = bipartite(G1)
print(g1)
