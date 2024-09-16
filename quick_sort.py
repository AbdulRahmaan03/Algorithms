import random


def quick_sort(arr):
    
    # Return arr if it consists 0 or 1 element
    if len(arr) <= 1:
        return arr
    
    # Case 1: Choosing Pivot as last element of arr
    # else:
    #     pivot = arr[-1]  # First element as pivot
        
    #     less_than_pivot = [x for x in arr[ : -1] if x < pivot]
    #     equal_to_pivot = [x for x in arr if x == pivot]  # All elements equal to pivot
    #     greater_than_pivot = [x for x in arr[ : -1] if x > pivot]
        
    #     return quick_sort(less_than_pivot) + equal_to_pivot + quick_sort(greater_than_pivot)

    # Case 2: Choosing pivot as first element of arr
    # else:
    #   pivot = arr[0]
      
    #   less_than_pivot = [x for x in arr[1 : ] if x < pivot]
    #   equal_to_pivot = [x for x in arr if x == pivot]
    #   greater_than_pivot = [x for x in arr[1 : ] if x > pivot]
    
    #   return quick_sort(less_than_pivot) + equal_to_pivot + quick_sort(greater_than_pivot)

    # Case 3: Choosing pivot as the middle_indexed element of arr
    # else:
    #   middle_index = len(arr) // 2
    #   pivot = arr[middle_index]
      
    #   less_than_pivot = [x for x in arr[ : middle_index] + arr[middle_index + 1 : ] if x <= pivot]
    #   greater_than_pivot = [x for x in arr[ : middle_index] + arr[middle_index + 1 : ] if x > pivot]
    
    #   return quick_sort(less_than_pivot) + [pivot] + quick_sort(greater_than_pivot)

    # Case 4: Choosing pivot as a random element of arr
    else:
      pivot = random.choice(arr)
      
      less_than_pivot = [x for x in arr if x < pivot]
      equal_to_pivot = [x for x in arr if x == pivot]
      greater_than_pivot = [x for x in arr if x > pivot]
    
      return quick_sort(less_than_pivot) + equal_to_pivot + quick_sort(greater_than_pivot) 

# Example usage
# arr = [3, 1, 3, 2, 3]
arr = [5, 3, 8, 4, 2]
sorted_arr = quick_sort(arr.copy())

print(f"Before sorting: ", arr)
print(f"After quick sort: ", sorted_arr)


## Time Complexity

# Best and Avg Case => O(n log n)
# Worst Case => O(n^2)

## Space Complexit

# Best and Avg Case => O(log n)
# Worst Case => O(n)