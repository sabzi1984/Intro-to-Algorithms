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
    tsv = csv.reader(open(filename), delimiter='\t')
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
    #inverse the weight in charG to heapify 
    #the most strong element will be the firs element of the list
    for char1 in charG:
        for char2 in charG[char1]:
            charG[char1][char2] = 1.0 / charG[char1][char2]
    return charG

def heap_sort(charG,characters,k):
    heap=[]
    for char1 in characters:
        for char2 in charG[char1]:
            if char1 < char2:
                if len(heap)<k:
                    insert_heap(heap, (charG[char1][char2],(char1,char2)))
                elif charG[char1][char2]<heap[k-1][0]:
                    #if the element weight is less than kth element in the heap list
                    #add it to the list to be sorted 
                    insert_heap(heap, (charG[char1][char2],(char1,char2)))
                    del heap[k]
    return heap[k-1]
                    
def insert_heap(heap, v):
    heap.append(v)
    up_heapify(heap, len(heap) - 1)
    
def up_heapify(heap, i):
    while i > 0: 
        p = (i - 1) // 2
        if heap[i][0] < heap[p][0]:
            (heap[i], heap[p])=(heap[p],heap[i])
            up_heapify(heap, p)
        else:
            break
marvelG, characters = read_graph('uniq_edges.tsv')
charG=make_char_graph(marvelG,characters)
print(heap_sort(charG,characters,2))
