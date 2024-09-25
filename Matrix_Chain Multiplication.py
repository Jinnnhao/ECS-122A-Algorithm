# Matrix_Chain Multiplication 
def matrix_chain(p ,n):
              # the row              # the colum
    matrix = [[0 for x in range(n)] for x in range(n)]
    s = [[0 for x in range(n)] for x in range(n)]

    for chain_len in range (2,n+1):
        for i in range (0, n- chain_len + 1):
            j = i + chain_len -1
            matrix[i][j] = float('inf')
            for k in range(i, j):       # k determins the split position of the matrix chain
                q = matrix[i][k] + matrix[k+1][j] + p[i-1]*p[k]*p[j]
                if q < matrix[i][j]:
                    matrix[i][j] = q
                    s[i][j] = k 

    print("print table m: \n")
    for row in matrix:
        print(row)
        

    print("print table s: \n")
    for row in s:
        print(row)
        


p = [5, 6, 3, 7, 5, 3]
n = len(p) -1 
matrix_chain(p,n)