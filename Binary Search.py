# Binary Search
def bin_find_in(arr, item):
    # sort_arr = sort(arr)
    min = 0
    max = len(arr) - 1
    for i in range(len(arr) - 1):
        mid = (min + max) // 2
        if(arr[mid] == item): return mid
        else:
            if(arr[mid] < item):
                min = mid + 1
            else:
                max = mid - 1
    return -1

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(bin_find_in(list1, 5))