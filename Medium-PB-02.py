# 2.program for selection sort ?
def selection_sort(arr):
    for i in range(len(arr)):
        min=i
        for j in range(i,len(arr)):
            if arr[j]<arr[min]:
                min=j
        arr[i],arr[min]=arr[min],arr[i]
    return arr

print(selection_sort([15,69,24,10,1,25,14,100,52,96]))
