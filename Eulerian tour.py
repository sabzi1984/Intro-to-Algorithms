def create_tour(nodes):
    i=0
    edge_list=[]
    for i in range (len(nodes)-1):      
        connected_nodes=(nodes[i],nodes[i+1])
        edge_list.append(connected_nodes)
    if i==len(nodes)-2:
        connected_nodes=(nodes[i+1],nodes[0])
        edge_list.append(connected_nodes)     
    return edge_list
nodes=[20,30,40,50,60]
print(create_tour(nodes))
