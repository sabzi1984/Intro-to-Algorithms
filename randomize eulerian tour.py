import random
def create_tour(nodes):
    connected=[]
    unconnected=[n for n in nodes]
    tour=[]
    degree={}
    x=unconnected.pop()
    y=unconnected.pop()
    tour.append((x,y))
    connected.append(x)
    connected.append(y)
    degree[x]=1
    degree[y]=1
    while len(unconnected)>0:
        x=random.choice(connected)
        y=unconnected.pop()
        tour.append((x,y))
        connected.append(y)
        degree[x]+=1
        degree[y] =1
    odd_nodes=[m for m,n in degree.items() if n%2==1]
    even_nodes=[m for m,n in degree.items() if n%2==0] 
    while len(odd_nodes)>0:
        x=odd_nodes.pop()
        cn=check_connected_nodes(x,odd_nodes,tour)
        if cn is not None:
            odd_nodes.remove(cn)
            even_nodes.append(x)
            even_nodes.append(cn)
            degree[x]+=1
            degree[cn]+=1
            tour.append((x,cn))
            
        else:
            cn=check_connected_nodes(x,even_nodes,tour)
            odd_nodes.append(cn)
            even_nodes.append(x)
            even_node.remove(cn)
            degree[x]+=1
            degree[cn]+=1            
            tour.append((x,cn))
    return tour
        
def check_connected_nodes(x,nodes,tour):
    for node in nodes:
        if (x,node) or (node,x) not in tour:
            return node
    return None
nodes=[20,30,40,50,60]
print(create_tour(nodes))
