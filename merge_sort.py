def merge_sort(arr):
    # Check if length of array is greater than 1
    if len(arr) > 1:
        # Find the middle index of arr
        mid = len(arr) // 2

        # Split the arr into two halves based on the mid index
        left_half = arr[:mid]
        right_half = arr[mid:]

        # Recursivelly call merge_sort on both halves to perform divide and conquer
        merge_sort(left_half)
        merge_sort(right_half)

        # Define index for left halve, right halve and sorted_arr
        i = j = k = 0

        # Compare elements of both halves and add to sorted arr
        while i < len(left_half) and j < len(right_half):
            
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                k += 1
                i += 1

            else:
                arr[k] = right_half[j]
                k += 1
                j += 1
        
        # Add left out elements from both left and right halves to sorted_arr
        while i < len(left_half):
            arr[k] = left_half[i]
            k += 1
            i += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            k += 1
            j += 1


arr = [38, 27, 43, 3, 9, 82, 10]
print("Array before merge sort: ", arr)

merge_sort(arr)
print("Array after merge sort: ", arr)

# Time Complexity
## Best, Average, Worst => O(nlogn)

# Space Complexity => O(n)