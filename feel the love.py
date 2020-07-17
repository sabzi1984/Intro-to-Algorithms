# Take a weighted graph representing a social network where the weight
# between two nodes is the "love" between them.  In this "feel the
# love of a path" problem, we want to find the best path from node `i`
# and node `j` where the score for a path is the maximum love of an
# edge on this path. If there is no path from `i` to `j` return
# `None`.  The returned path doesn't need to be simple, ie it can
# contain cycles or repeated vertices.
#
# Devise and implement an algorithm for this problem.

import heapq
from collections import defaultdict
def feel_the_love(G, i, j):
	# return a path (a list of nodes) between `i` and `j`,
	# with `i` as the first node and `j` as the last node,
	# or None if no path exists
	path = dijkstra(G, i)
	if  j not in path:
		return None
	node_a, node_b = max_weight_edge(G, i)
	if node_a==j: 
		return path[node_b]+[j]
	if node_b==j:
		return path[node_a]+[j]
	else:	
		path_a = path[node_a]
		path_b = (dijkstra(G, node_b))[j]
	
	return path_a + path_b

def max_weight_edge(G, i):
	max_so_far = 0
	edge       = None
	reachable  = dijkstra(G, i)
	for node in G:
		for neighbor in G[node]:
			if (G[node])[neighbor] > max_so_far and node in reachable:
				max_so_far = (G[node])[neighbor]
				edge = node, neighbor

	return edge

def val(pair): return pair[0]
def id(pair): return pair[1]

def dijkstra(G,v):
	heap = [ [0, v] ]
	dist_so_far = {v:[0, v]}
	final_dist = {}
	final_path=defaultdict(list)
	while  dist_so_far:
			 
		w = heapq.heappop(heap)
		node = id(w)
		dist = val(w)
		
		del dist_so_far[node]
			    

		final_dist[node] = dist
		for x in G[node]:
			if x not in final_dist:
				new_dist = dist + G[node][x]
				new_entry = [new_dist, x]
				if x not in dist_so_far:
					dist_so_far[x] = new_entry
					final_path[x]=final_path[node]+[node]
					heapq.heappush(heap, new_entry)
				
				elif new_dist < val(dist_so_far[x]):
					dist_so_far[x][1] = "REMOVED"
					dist_so_far[x] = new_entry
					final_path[x]="REMOVED"
					final_path[x]=final_path[node]+[node]                   
					heapq.heappush(heap, new_entry)
	    
	for node in final_path:
		final_path[node] += [node]
	return final_path
G = {'a':{'c':1},
         'b':{'c':1},
         'c':{'a':1, 'b':1, 'e':1, 'd':1},
         'e':{'c':1, 'd':2},
         'd':{'e':2, 'c':1},
         'f':{}}
print(feel_the_love(G,'a','b'))
