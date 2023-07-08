vertices = []   #stores the vertices of the graph
vertices_no =0  #stores the vertices no in the graph
graph = [] 

#Add a vertex to the graph
def add_vertex(v):
    global vertices
    global vertices_no
    global graph
    if v in vertices:
        print(f' Vertex {v} already exists in Python')
    else:
        vertices_no +=1
        vertices.append(v)
        #adds a new column with a default value of 0 for existing rows  
        if vertices_no >1:
            for vertex in graph:
                vertex.append(0)
        temp = []  #adds a new row to the graph to represent the new connecction
        for i in range(vertices_no):
            temp.append(0)
        graph.append(temp)


#add a edge between two vertices with an edge weight e
def add_edge(v1,v2,e):
    global graph
    global vertices
    global vertices_no
    if v1 not in vertices: #check if v1 is a valid vertex
        print(f'vertex {v1} is not a valid vertex')
    elif v2 not in vertices: #check if v2 is a valid vertex
        print(f'vertex {v2} is not a valid vertex')
    # Since this code is not restricted to a directed or an undirected graph, an edge between v1 v2 does not
    # imply that an edge exists between v2 and v1
    else:
        index1 = vertices.index(v1)
        index2 = vertices.index(v2)
        graph[index1][index2] = e


def print_graph():
    global graph
    global vertices_no
    for i in range(vertices_no):
        for j in range(vertices_no):
            if graph[i][j] !=0:
                print(f'{vertices[i]} -> {vertices[j]} \
                         edge weight : {graph[i][j]}')


def remove_edges(v1,v2):
    global graph
    #because of the 0 indexing of lists
    if graph[v1-1][v2-1] == 0:
        print(f'no edge between {v1} and {v2}')
        return 
    else:
        graph[v1][v2] =0
        graph[v2][v1] =0

#driver code
add_vertex(1)
add_vertex(2)
add_vertex(3)
add_vertex(4)

add_edge(1, 2, 1)
add_edge(1, 3, 1)
add_edge(2, 3, 3)
add_edge(3, 4, 4)
add_edge(4, 1, 5)

print_graph()
print("Internal representation: ", graph)

#output
1  ->  2  edge weight:  1
1  ->  3  edge weight:  1
2  ->  3  edge weight:  3
3  ->  4  edge weight:  4
4  ->  1  edge weight:  5
Internal representation:  [[0, 1, 1, 0], [0, 0, 3, 0], [0, 0, 0, 4], [5, 0, 0, 0]]

#2d representation of the graph
[[0, 1, 1, 0],
 [0, 0, 3, 0],
 [0, 0, 0, 4],
 [5, 0, 0, 0]]
