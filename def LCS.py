def LCS(X,Y, m, n):

    c = [[0 for x in range(n+1)] for x in range(m+1)]   # c = n+1 colums x m+1 rows
    b = [[0 for x in range(n+1)] for x in range(m+1)]   

    for i in range(1,m+1):
        for j in range(1,n+1):
            if(X[i-1] == Y[j-1]):     # case 1: if X[i] == Y[j], increase the length by one from c[i-1][j-1]
                c[i][j] = c[i-1][j-1]+1
                b[i][j] = 'Diag'
            elif (c[i-1][j] >= c[i][j-1]):  # case 2.1: if the upper one >= left one
                c[i][j] = c[i-1][j]         # c[i][j] = c[i-1][j], the current one = the upper one 
                b[i][j] = 'Up'
            else:
                c[i][j] = c[i][j-1]         # case 2.2: if the left > upper one
                b[i][j] = "Left"            # c[i][j] = c[i][j-1], the current one = the left one


    print("print table c: \n")
    for row in c:
        print(row)
        

    print("print table b: \n")
    for row in b:
        print(row)


X = "photograph" 
Y = "tomography"
m = len(X)
n = len(Y)

LCS(X, Y, m, n)