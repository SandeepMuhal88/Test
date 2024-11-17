# Merge Sort
def merge_sort(arr):
    # Case-1 is one
    if len(arr)<=1:
        return arr
    
    # Case 2 Divide
    mid=len(arr)//2

    left_half=merge_sort(arr[:mid])
    right_half=merge_sort(arr[mid:])
    return merge(left_half,right_half)
def merge(left,right):
    new_arr=[]
    v1=v2=0
    while v1<len(left) and v2<len(right):
        if left[v1]<right[v2]:
            new_arr.append(left[v1])
            v1+=1
        else:
            new_arr.append(right[v2])
            v2+=1
    new_arr.extend(left[v1:])
    new_arr.extend(right[v2:])
    return new_arr

print(merge_sort([15,52,6,74,100,21,784,300]))

