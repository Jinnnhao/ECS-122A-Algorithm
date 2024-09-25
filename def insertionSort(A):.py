def insertionSort_ascending(A):     # sort in ascending order
    n = len(A)
    for j in range(1,n):  # start from the second index 
        key = A[j]         
        i = j-1 
        while (i >= 0 and A[i] > key):  # using i as the j-1 to check back all the value from j
            A[i+1] = A[i]               # if the previous data > key, then switch 
            i = i-1                     # i moves to the left 
        A[i+1] = key                    # at the end, insert to key at i+1
    print(A)
    return 

def insertionSort_descending(A):     # sort in descending order
    n = len(A)
    for j in range(1,n):  # start from the second index 
        key = A[j]         
        i = j-1 
        while (i >= 0 and A[i] < key):  # using i as the j-1 to check back all the value from j
            A[i+1] = A[i]               # if the previous data > key, then switch 
            i = i-1                     # i moves to the left 
        A[i+1] = key                    # at the end, insert to key at i+1
    print(A)
    return 



A = [9,3,6,7,8,4,2,11,99,66,88]
insertionSort_ascending(A)

B = [9,3,6,7,8,4,2,11,99,66,88]
insertionSort_descending(B)