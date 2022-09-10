def binarySearch(sequence,item):
    start_index = 0
    end_index = len(sequence)-1
    while start_index <= end_index:
        mid_point =start_index+(end_index-start_index)//2
        mid = sequence[mid_point]
        if mid ==item:
            return mid_point
        elif item < mid:
            end_index = mid_point-1
        else:
            start_index = mid_point+1
    return None
    
# Other way 
def binary_Search(sequence,item):
    if item in sequence:
        return sequence.index(item)
    else:
        return -1
    
arr=[1,2,3,4,5,6,7,8,9]
item = 10
print(binarySearch(arr,item))
