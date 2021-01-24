arr = [5, 7, 2, 3, 8, 9, 1, 4, 6]

def selectionSort(arr):
    for i in range(len(arr)-1): # -1 so that it doesn't include the first index (0)
        # mindex = index where the minimum value currently is
        # starts at 0 because we don't know yet
        mindex = i
        for j in range(i+1,len(arr)): # + 1 so that it doesn't count the current iteration 
            # mindex = j if it's smaller than i 
            if arr[j] < arr[mindex]:
                mindex = j
            #print("index", mindex, "value", arr[mindex])
        # change index if minimum is updated
        if mindex != i:
            arr[i], arr[mindex] = arr[mindex], arr[i]
    return arr

print(selectionSort(arr))
