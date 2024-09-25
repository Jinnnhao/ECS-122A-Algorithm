def mergeSort(A,low, high):
    if low < high:
        mid = (low + high)//2             # divide in halves 
        mergeSort(A, low, mid)      # conquer the left half
        mergeSort(A, mid+1, high)   # conquer the right half
        Merge(A, low, mid, high)    # combine/ merge 
    return

def Merge(A, low, mid, high): 
    left = mid - low + 1
    right = high - mid 
    L = [0] * (left+1)   # hold the left part of A
    R = [0] * (right+1)  # hold the right part of A
     # merge the left half
    for i in range(0,left):
        L[i] = A[low+i] 
    
    for i in range(0,right):
        R[i] = A[mid+1+i]
    
    L[left] = float('inf')
    R[right] = float('inf')
    i = 0; j = 0  # i is the index for L, j is for R

    # Begin mergeing !!!
    for k in range(low, high+1):
        if(L[i] <= R[j]):       # if Left <= Right 
            A[k] = L[i]         # set A[k] = L[i]
            i = i +1    
        else:                   # else Left > Right 
            A[k] = R[j]         # set A[k] = R[j]
            j = j+1
    return


A = [5, 2, 4, 7, 1, 3, 2, 6]
low = 0
high = 7
mergeSort(A, low, high)
print(A)

       
