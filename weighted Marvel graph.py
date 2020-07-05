import csv

def make_link(G, node1, node2):
    if node1 not in G:
        G[node1] = {}
    if node2 not in G[node1]:
        (G[node1])[node2] = 0
    (G[node1])[node2] += 1
    if node2 not in G:
        G[node2] = {}
    if node1 not in G[node2]:
        (G[node2])[node1] = 0
    (G[node2])[node1] += 1
    return G

def read_graph(filename):
    tsv = csv.reader(open(filename), delimiter=',')
    G = {}
    characters=set()
    for char, book in tsv: 
        make_link(G, char, book)
        characters.add(char)
    return  G, characters

def make_char_graph(marvelG,characters):
    charG = {}
    for char1 in characters:
        for book in marvelG[char1]:
            for char2 in marvelG[book]:
                # to avoid double count
                if char1 < char2:
                    make_link(charG, char1, char2)
    #inverse the weight in charG to show shorter distance 
    for char1 in charG:
        for char2 in charG[char1]:
            charG[char1][char2] = 1.0 / charG[char1][char2]
    return charG

def hop_distance (charG,v):
    hop=0
    final_dist = {v:(hop, v, None)}
    open_list=[v]
    while len(open_list) > 0:
        node = open_list.pop(0)
        
        for neighbor in G[node]:
            if neighbor not in final_dist:
                open_list.append(neighbor)
                final_dist[neighbor] = (hop + 1, neighbor, node)
                
    return final_dist
def dijkstra(charG,v):
    first_entry = (0, v, None) #(weight,hop)
    heap = [first_entry]
    location = {first_entry:0}
    dist_so_far = {v:first_entry}
    final_dist = {}
    while len(dist_so_far) > 0:
        w = heappopmin(heap, location)
        node = w[1]
        dist = w[0]
        del dist_so_far[node]
        final_dist[node] = w
        for x in charG[node]:
                if x not in final_dist:
                    new_dist = charG[node][x]+ final_dist[node]
                    new_entry = (new_dist, x, node)
                    if x not in dist_so_far:
                        dist_so_far[x] = new_entry
                        insert_heap(heap, new_entry, location)
                    
                    elif new_entry < dist_so_far[x]:
                        decrease_val(heap, location, dist_so_far[x], new_entry)
                        dist_so_far[x] = new_entry
        return final_dist        
def heappopmin(heap, location):
    val = heap[0]
    new_top = heap.pop()
    location[val] = None
    if len(heap) == 0:
        return val
    location[new_top] = 0
    heap[0] = new_top
    down_heapify(heap, 0, location)
    return val
def down_heapify(heap, i, location):
    while True:
        l = left(i)
        r = right(i)

        if l >= len(heap): 
            break

        v = heap[i][0]
        lv = heap[l][0]

        if r == len(heap):
            if v > lv:
                swap(heap, i, l, location)
            break

        rv = heap[r][0]
      
        if min(lv, rv) >= v: 
            break
        
        if lv < rv:
            swap(heap, i, l, location)
            i = l
        else:
            swap(heap, i, r, location)
            i = r
            
def left(i): 
    return 2*i+1
def right(i): 
    return 2*i+2

def swap(heap, old, new, location):
    location[heap[old]] = new
    location[heap[new]] = old
    (heap[old], heap[new]) = (heap[new], heap[old])

def insert_heap(heap, v, location):
    heap.append(v)
    location[v] = len(heap) - 1
    up_heapify(heap, len(heap) - 1, location)
    
def up_heapify(heap, i, location):
    while i > 0: 
        p = (i - 1) // 2
        if heap[i][0] < heap[p][0]:
            swap(heap, i, p, location)
            i = p
        else:
            break
def decrease_val(heap, location, old_val, new_val):
    i = location[old_val]
    heap[i] = new_val
    location[old_val] = None
    location[new_val] = i
    up_heapify(heap, i, location)
def get_parent(pair): return pair[2]
def find_path(dist, target):
    node = target
    path = [target]
    while True:
        prev = get_parent(dist[node])
        if prev is None:
            # We've rached our target, so return 
            # the path
            return path
        path.append(prev)
        node = prev
answers = [] #store a tuple ((char1, char2), (char_path, hop_dist))
# the characters that the problem asks us to look at
chars = ['SPIDER-MAN/PETER PAR',
                 'GREEN GOBLIN/NORMAN ',
                 'WOLVERINE/LOGAN ',
                 'PROFESSOR X/CHARLES ', 
                 'CAPTAIN AMERICA']

marvelG, characters = read_graph('edges.csv')
charG=make_char_graph(marvelG,characters)
        
for char1 in chars:
    # calculate the distance to each other character
    char_dist = dijkstra(charG, char1)
    # and calculate the hops required
    hop_dist = hop_distance(charG, char1)

    for char2 in char_dist:
        if char1 == char2:
            continue
        char_path = find_path(char_dist, char2)
        hop_path = find_path(hop_dist, char2)
        # if the weighted path is longer then the hop path, we need
        # to save it
        if len(char_path) > len(hop_path):
            answers.append(((char1, char2), (char_path, hop_path)))

# and now we print out the answer
print (len(answers))
