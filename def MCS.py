def MCS(X, Y, m, n):
    substrings= []
    #loop from X one by one to compare
    for i in range(0,m):
        for j in range(0,n):
            if(X[i] == Y[j]):
                limit = min(m-1-i,n-1-j)
                if (i > j):
                    for next in (0, limit):
                        Xnext = i + next
                        Ynext = j + next
                        if (X[Xnext] == Y[Ynext]):
                            sub = ""
                            for a in range(i, Xnext+1):
                                sub = sub + X[a]
                                if(sub not in substrings):
                                    substrings.append(sub)
                        else: 
                            break
                else:
                    for next in (0, limit):
                        Xnext = i + next
                        Ynext = j + next
                        if (X[Xnext] == Y[Ynext]):
                            sub = ""
                            for a in range(j, Ynext+1):
                                sub = sub + Y[a]
                                if(sub not in substrings):
                                    substrings.append(sub)
                        else: 
                            break
                

    print(substrings)
    return

X = "photograph" 
Y = "tomography"
m = len(X)
n = len(Y)
MCS(X,Y,m,n)