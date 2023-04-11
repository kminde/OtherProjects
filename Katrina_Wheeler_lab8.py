def printMatrix(m):
    for row in m:
        print(row)

def chainMatrix(dims):
    # Create the empty 2-D table
    n = len(dims)-1
    m = [[None for i in range(n)] for j in range(n)]
    traceback = [[None for i in range(n)] for j in range(n)]

    # Fill in the base case values
    for i in range(n):
        m[i][i] = 0
        traceback[i][i] = 0

    # Fill in the rest of the table diagonal by diagonal
    for chainLength in range(2,n+1):
        for i in range(n+1-chainLength):
            j = i + chainLength - 1
            # Fill in m[i][j] with the best of the recursive options
            m[i][j] = float("inf")
            for k in range(i,j):
                # Two previous table values plus
                # what it cost to mult the resulting matrices
                q = m[i][k]+m[k+1][j]+dims[i]*dims[k+1]*dims[j+1]
                if q < m[i][j]:
                    m[i][j] = q
                    traceback[i][j] = k

    printMatrix(m)
    parentStr(traceback, i, j)
    return m[0][n-1]

def parentStr(traceback, start, end):
    # Add parenthesis up until start and end are equivalent
    if start == end:
        print("A{}".format(start), end = '')
    else:
        k = traceback[start][end]
        print('(', end = '')
        parentStr(traceback, start, k)
        parentStr(traceback, k+1, end)
        print(')', end = '')


dims = [30,35,15,5,10,20,25]
chainMatrix(dims)
