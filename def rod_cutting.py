def rod_cutting(price, n, c): 
    revenue = [0] * (n+1)  # array with size of n+1, becasue length = 0, price = 0
    bestCut = [0] * (n+1)

    for i in range(1,n+1):  # start from 1 and stop at n
        # when there is no cut 
        max_revenue = price[i]
        bestCut[i] = i
        for j in range(1, i):  # start from 1 to i 
            if (max_revenue < (price[j] - c + revenue[i-j])):
                max_revenue = (price[j] - c + revenue[i-j])
                bestCut[i] = j

        revenue[i] = max_revenue

    print(revenue[1:])
    print(bestCut[1:])
    return 

 
price = [0, 1, 4, 5, 9, 10, 12, 15, 18, 19,20]
n = 10
c = 1 
rod_cutting(price, n, c)





