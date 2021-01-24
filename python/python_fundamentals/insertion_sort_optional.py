def insertionSort(arr):
    # We should take out the "-1" for this because we need the last element in array
    for i in range(1, len(arr)):
        anchor = arr[i]
        j = i - 1
        
        while  j>=0 and anchor < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
            
        arr[j + 1] = anchor

    return anchor


if __name__ == '__main__':
    arr = [5, 7, 2, 3, 8, 9, 1, 4, 6]
    insertionSort(arr)
    print(arr)