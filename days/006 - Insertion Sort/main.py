def insertionSort(arr: list):
    for i in range(1, len(arr)):
        for j in range(len(arr)):
            if(arr[i] < arr[j]):
                arr.insert(j, arr.pop(i))
