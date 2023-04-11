def extractMin(verts, array):
    'return index of min value in the list'
    min = 9999999
    for v in range(len(verts)):
        if verts[v] < min and array[v] == False:
            min = verts[v]
            minIndex = v
    return minIndex

def printMST(parents):
    print("Edges:")
    for i in range(len(parents)):
        print(f"{i}, {parents[i]}")

def mst(g):
    '''create lists to track keys, parents, and if the key has been visited
    (boolArray), finds minimun value in each vertex and updates boolArray
    once it has been visited'''

    keys = [float("inf") for i in range(len(g))]
    parents = [None for i in range(len(g))]
    boolArray = [False for i in range(len(g))]

    keys[0] = 0
    parents[0] = -1

    for vertex in g:
        k = extractMin(keys, boolArray)
        boolArray[k] = True
        for v in range(len(vertex)):
            if g[k][v] > 0 and g[k][v] < keys[v] and boolArray[v] == False:
                keys[v] = graph[k][v]
                parents[v] = k
    printMST(parents)

graph = [[0, 7, 0, 0, 0, 10, 15, 0],
         [7, 0, 12, 5, 0, 0, 0, 9],
         [0, 12, 0, 6, 0, 0, 0, 0],
         [0, 5, 6, 0, 14, 8, 0, 0],
         [0, 0, 0, 14, 0, 3, 0, 0],
         [10, 0, 0, 8, 3, 0, 0, 0],
         [15, 0, 0, 0, 0, 0, 0, 0],
         [0, 9, 0, 0, 0, 0, 0, 0]]

mst(graph)