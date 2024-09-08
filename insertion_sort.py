def insertion_sort(arr):
    # Check if length of array is 0 or 1
    if len(arr) <= 1: 
        return arr
    
    # If length is greater than 1, perform insertion sort
    else:
        for i in range(1, len(arr)):

            key = arr[i] # Assign key to compare in array (2nd Element)
            j = i - 1 # Define index to start comparison (1st Element)

            while j >= 0 and arr[j] > key: # Move elements greater than key to one position ahead
                
                arr[j + 1] = arr[j] # Put the greater number in the right position
                j -= 1 # Move index to the previous element

            arr[j + 1] = key # Put the smaller number in sorting order
        
        return arr # Return sorted array
    
# Example
arr = [12, 11, 13, 5, 6]

sorted_arr = insertion_sort(arr.copy()) # Send a copy of original list for sorting as lists are mutable in python.

print(f"Before sorting: ", arr)
print(f"After insertion sort: ", sorted_arr)



## Time Complexity

# Best case (already sorted array): O(n)
# Worst case (reverse sorted array): O(n²)
# Average case: O(n²)


## Space Complexity

# O(1)


## Asymptotic Notations

# Big O (O): Describes the worst-case time complexity (upper bound).
# Omega (Ω): Describes the best-case time complexity (lower bound).
# Theta (Θ): Describes the average-case or tight bound (both upper and lower bound).
# Little o (o): Upper bound, but not tight.
# Little omega (ω): Lower bound, but not tight.