import numpy as np
class Graph():
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)]\
                              for row in range(vertices)]

    def isSafe(self, v, colour, c):
        for i in range(self.V):
            if self.graph[v][i] == 1 and colour[i] == c:
                return False
        return True
     

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
        if self.graphColourUtil(m, colour, 0) == None:
            return False
        print ("\nThe solution is")
        for c in colour:
            print ("Colour:",c,end=', ')
        return True

list_m=[]
n=int(input("Enter the number of nodes "))
f_list=[]
print("\nEnter the values of adjacency matrix.\ni.e.",n*n,"inputs sepereated by a space")
a=input()
list_m=a.split()
list_m = [int(i) for i in list_m]

list_m=(list_m)
f_list=np.array_split(list_m,n)
g=Graph(n)
g.graph=list(f_list)
m=int(input("\nEnter the chromatic number: "))
g.graphColouring(m)