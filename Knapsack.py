def Knapsack(V, W, totalWeight,n):
    c = [[0 for x in range(totalWeight+1)] for x in range(n+1)]  # c = (n+1) row x (totalWeight+1) colums, initialize 0
    s = []
    for i in range(1,n+1):  # start by row, each ith item // the outer loop is loop for each row
        # the index of each item in V and W is i-1
        for w in range(1, totalWeight+1):       # the inner loop is loop for each colum in a row
            # case 1: W[i] > w -> c[i,w] = c[i-1,w]
            if(W[i-1] > w):
                c[i][w] = c[i-1][w]

            # case 2: W[i] <= totalWeight: either update c with [the max sum within current w] or [replace it with the optimal value in this w]
            elif(W[i-1] <= w):
                c[i][w] = max(V[i-1] + c[i-1][w - W[i-1]], c[i-1][w])
    
    w = totalWeight
    for i in range (n, 0, -1):
        if(c[i][w] != c[i-1][w]):  # if the current one != the upper one, store it
            s.append(i)
            w = w - W[i-1]         # substract this weight out of the totalWeight 
    
    for row in c:
        print(row)
    
    print("Optimal value =" , c[n][totalWeight])
    print("Optimal set of items =", s)
    return


V = [40, 35, 18, 4, 10, 2]
W = [100, 50,45,20, 10, 5]
n = len(V)
totalWeight = 100
Knapsack(V, W, totalWeight, n)
