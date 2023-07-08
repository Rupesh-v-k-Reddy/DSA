graph ={}
vertices_no= 0

#Add a vertex to the graph
def add_vertex(v):
    global graph
    global vertices_no
    if v in graph:
        print(f'vertex {v} already exists in graph')
    else:
        vertices_no +=1
        graph[v]= []

#add a edge between two vertices with an edge weight e
def add_edge(v1,v2,e):
    global graph
    if v1 not in graph:#check if v1 is a valid vertex
        print(f'vertex {v1} is not a valid vertex')
    elif v2 not in graph:#check if v2 is a valid vertex
        print(f'vertex {v1} is not a valid vertex')
    # Since this code is not restricted to a directed or an undirected graph, an edge between v1 v2 does not
    # imply that an edge exists between v2 and v1
    else:
        temp = [v2,e]
        graph[v1].append(temp)

def print_graph():
    global graph
    for vertex in graph:
        for edges in graph[vertex]:
            print(f'{vertex} -> {edges[0]} ,edge weight :{edges[1]}')


#driver code
add_vertex(1)
add_vertex(2)
add_vertex(3)
add_vertex(4)
# Add the edges between the vertices by specifying
# the from and to vertex along with the edge weights.
add_edge(1, 2, 1)
add_edge(1, 3, 1)
add_edge(2, 3, 3)
add_edge(3, 4, 4)
add_edge(4, 1, 5)
print_graph()
# Reminder: the second element of each list inside the dictionary
# denotes the edge weight.
print ("Internal representation: ", graph)


#output
1  ->  2  edge weight:  1
1  ->  3  edge weight:  1
2  ->  3  edge weight:  3
3  ->  4  edge weight:  4
4  ->  1  edge weight:  5
Internal representation:  {1: [[2, 1], [3, 1]], 2: [[3, 3]], 3: [[4, 4]], 4: [[1, 5]]}
