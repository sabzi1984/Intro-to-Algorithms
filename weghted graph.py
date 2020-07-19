# In lecture, we took the bipartite Marvel graph,
# where edges went between characters and the comics
# books they appeared in, and created a weighted graph
# with edges between characters where the weight was the
# number of comic books in which they both appeared.
#
# In this assignment, determine the weights between
# comic book characters by giving the probability
# that a randomly chosen comic book containing one of
# the characters will also contain the other
#
import pickle
marvel = pickle.load(open("smallG.pkl","rb"))
characters = pickle.load(open("smallChr.pkl","rb"))
def create_weighted_graph(bipartiteG, characters):
    G = {}    
    for char1 in characters:
        G[char1]={}
        for char2 in characters:
            G[char1][char2]=None
            
    for char1 in characters:
        for comic in bipartiteG[char1]:
            for char2 in bipartiteG[comic]:
                if char1!=char2:
                    """if char1 not in G:
                        G[char1]={}
                    if char2 not in G:
                        G[char2]={}"""
                    comic1=list(bipartiteG[char1])
                    comic2=list(bipartiteG[char2])
                    common_comics=0
                    for comic11 in comic1:
                        for comic22 in comic2:
                            if comic11==comic22:
                                common_comics+=1
                    prob=round(float(common_comics/(len(comic1)+len(comic2)-common_comics)),4)
                    G[char1][char2]=prob
    return G
				

bipartiteG = {'charA':{'comicB':1, 'comicC':1},'charB':{'comicB':1, 'comicD':1},
'charC':{'comicD':1},'comicB':{'charA':1, 'charB':1},'comicC':{'charA':1},
'comicD': {'charC':1, 'charB':1}}
G = create_weighted_graph(bipartiteG, ['charA', 'charB', 'charC'])
print(G)
