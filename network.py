import matplotlib.pyplot as plt
import networkx as nx
import random

class Graph():

    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)]\
                      for row in range(vertices)]

    # A utility function to check if the current color assignment
    # is safe for vertex v
    def isSafe(self, v, colour, c):
        for i in range(self.V):
            if self.graph[v][i] == 1 and colour[i] == c:
                return False
        return True

    # A recursive utility function to solve m
    # coloring  problem
    def graphColourUtil(self, m, colour, v):
        if v == self.V:
            return True

        for c in range(1, m + 1):
            if self.isSafe(v, colour, c) == True:
                colour[v] = c
                if self.graphColourUtil(m, colour, v + 1) == True:
                    return True
                colour[v] = 0

    def graphColouring(self, m):
        colour = [0] * self.V
        if self.graphColourUtil(m, colour, 0) == False:
            return False
        return colour


z=1
while not(z % 2) == 0:  # Input how many nodes
    variable = input('Insert the number of nodes for the graph (Node number must be even): ')
    z = int(variable)

G = nx.random_regular_graph(3,z) # create a random graph with z nodes and every node has a degree of 3
B = nx.adjacency_matrix(G, nodelist=range(z))
B1 = B.todense()        #creates the adjacency matrix of the graph (B1)

g = Graph(z) #makes an instance of the class Graph
g.graph = B1.tolist()

nocolor = []
for node in G.nodes():      #creates a color map list with only white color
    nocolor.append('white')

list_of_colors = ['brown','m','magenta','yellow','green','blue','red'] # this is the list of the colors we are going to use to random choice for every coloring of the graph

pos = nx.spring_layout(G) #this a variable we use so the graph stays in the same position with every plot otherwise every node is printed in a random location (still the same graph but easier to compare when its colored and uncolored
edges = G.number_of_edges() # number of edges
e=0
while e < edges**2:

    colormap1 = g.graphColouring(3) # we call the function graphColouring to color the graph

    color1 = random.choice(list_of_colors) # 3 random colors from the list
    color2 = random.choice(list_of_colors)
    color3 = random.choice(list_of_colors)
    while not(color1 != color2 and color2 != color3 and color3 != color1): # We make sure they are 3 different colors
        color1 = random.choice(list_of_colors)
        color2 = random.choice(list_of_colors)
        color3 = random.choice(list_of_colors)

    color_map = []
    for node in G.nodes(): # Makes the list color_map which will be used as a parameter in the drawing for the colorized graph
        if colormap1[node] == 1:
            color_map.append(color1)
        elif colormap1[node] == 2:
            color_map.append(color2)
        else:
            color_map.append(color3)

    nx.draw(G, pos=pos,node_color=nocolor, with_labels=True) # Draws the graph with only white color
    plt.draw()
    plt.show()


    variable = input('Insert the number of the first node of the edge you want to challenge: ')  # Takes input the 2 nodes of the edge we are going to challenge
    edge1 = int(variable)
    variable = input('Insert the number of the second node of the edge you want to challenge: ')
    edge2 = int(variable)
    nodes = list(G.nodes)

    color_map_reveal = []

    for node in G.nodes(): # We copy only the colors for the nodes of the edge  from the color_map of the colorized graph
        if node == edge1 or node == edge2:
            for x in nodes:
                if nodes[x] == node:
                    color_map_reveal.append(color_map[x])
        else:
            color_map_reveal.append('white')



    nx.draw(G,pos=pos,node_color = color_map_reveal,with_labels = True) #and we print the graph only with the 2 nodes colored
    plt.draw()
    plt.show()
    nx.draw(G,pos=pos,node_color = color_map,with_labels = True) # print the colorized graph only to show we have the solution
    plt.draw()
    plt.show()
    e = e+1
    prop = (1-((edges-1)/edges)**e)*100 # calculates the propability of this colored graph to be the right solution
    print("You should be convinced by" ,prop,"%")