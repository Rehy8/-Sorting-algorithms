# ╔══╗─╔╗─╔╗╔══╗─╔══╗─╔╗───╔═══╗     ╔═══╗╔═══╗╔═══╗╔════╗
# ║╔╗║─║║─║║║╔╗║─║╔╗║─║║───║╔══╝     ║╔═╗║║╔═╗║║╔═╗║║╔╗╔╗║
# ║╚╝╚╗║║─║║║╚╝╚╗║╚╝╚╗║║───║╚══╗     ║╚══╗║║─║║║╚═╝║╚╝║║╚╝
# ║╔═╗║║║─║║║╔═╗║║╔═╗║║║─╔╗║╔══╝     ╚══╗║║║─║║║╔╗╔╝──║║──
# ║╚═╝║║╚═╝║║╚═╝║║╚═╝║║╚═╝║║╚══╗     ║╚═╝║║╚═╝║║║║╚╗──║║──
# ╚═══╝╚═══╝╚═══╝╚═══╝╚═══╝╚═══╝     ╚═══╝╚═══╝╚╝╚═╝──╚╝──
import random


def bubble_sort(nums):
    # Set swapped to True so that the loop will run at least once
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                # Swap elements
                nums[i], nums[i + 1] = nums[i + 1], nums[i]

                # Set swapped to True for the next iteration
                swapped = True


# ╔═══╗╔═══╗╔╗───╔═══╗╔═══╗╔════╗╔══╗╔═══╗╔═╗─╔╗     ╔═══╗╔═══╗╔═══╗╔════╗
# ║╔═╗║║╔══╝║║───║╔══╝║╔═╗║║╔╗╔╗║╚╣─╝║╔═╗║║║╚╗║║     ║╔═╗║║╔═╗║║╔═╗║║╔╗╔╗║
# ║╚══╗║╚══╗║║───║╚══╗║║─╚╝╚╝║║╚╝─║║─║║─║║║╔╗╚╝║     ║╚══╗║║─║║║╚═╝║╚╝║║╚╝
# ╚══╗║║╔══╝║║─╔╗║╔══╝║║─╔╗──║║───║║─║║─║║║║╚╗║║     ╚══╗║║║─║║║╔╗╔╝──║║──
# ║╚═╝║║╚══╗║╚═╝║║╚══╗║╚═╝║──║║──╔╣─╗║╚═╝║║║─║║║     ║╚═╝║║╚═╝║║║║╚╗──║║──
# ╚═══╝╚═══╝╚═══╝╚═══╝╚═══╝──╚╝──╚══╝╚═══╝╚╝─╚═╝     ╚═══╝╚═══╝╚╝╚═╝──╚╝──

def selection_sort(nums):
    # The i value corresponds to the number of sorted values
    for i in range(len(nums)):

        # Initially, we consider the first element to be the smallest
        lowest_value_index = i

        # This loop iterates over the unsorted elements
        for j in range(i + 1, len(nums)):
            if nums[j] < nums[lowest_value_index]:
                lowest_value_index = j

        # Change the smallest element with the first one in the lis
        nums[i], nums[lowest_value_index] = nums[lowest_value_index], nums[i]


# ╔══╗╔═╗─╔╗╔═══╗╔═══╗╔═══╗╔════╗╔══╗╔═══╗╔═╗─╔╗     ╔═══╗╔═══╗╔═══╗╔════╗
# ╚╣─╝║║╚╗║║║╔═╗║║╔══╝║╔═╗║║╔╗╔╗║╚╣─╝║╔═╗║║║╚╗║║     ║╔═╗║║╔═╗║║╔═╗║║╔╗╔╗║
# ─║║─║╔╗╚╝║║╚══╗║╚══╗║╚═╝║╚╝║║╚╝─║║─║║─║║║╔╗╚╝║     ║╚══╗║║─║║║╚═╝║╚╝║║╚╝
# ─║║─║║╚╗║║╚══╗║║╔══╝║╔╗╔╝──║║───║║─║║─║║║║╚╗║║     ╚══╗║║║─║║║╔╗╔╝──║║──
# ╔╣─╗║║─║║║║╚═╝║║╚══╗║║║╚╗──║║──╔╣─╗║╚═╝║║║─║║║     ║╚═╝║║╚═╝║║║║╚╗──║║──
# ╚══╝╚╝─╚═╝╚═══╝╚═══╝╚╝╚═╝──╚╝──╚══╝╚═══╝╚╝─╚═╝     ╚═══╝╚═══╝╚╝╚═╝──╚╝──

def insertion_sort(nums):
    # We start sorting from the second element, because the first element is considered to be already sorted
    for i in range(1, len(nums)):
        item_to_insert = nums[i]

        # Keeping a reference to the index of the previous element
        j = i - 1

        #  Elements of the sorted segment are moved forward if they are larger than the element to be inserted
        while j >= 0 and nums[j] > item_to_insert:
            nums[j + 1] = nums[j]
            j -= 1

        # Insert element
        nums[j + 1] = item_to_insert


# ╔═══╗╔╗─╔╗╔══╗╔═══╗╔╗╔═╗     ╔═══╗╔═══╗╔═══╗╔════╗
# ║╔═╗║║║─║║╚╣─╝║╔═╗║║║║╔╝     ║╔═╗║║╔═╗║║╔═╗║║╔╗╔╗║
# ║║─║║║║─║║─║║─║║─╚╝║╚╝╝─     ║╚══╗║║─║║║╚═╝║╚╝║║╚╝
# ║╚═╝║║║─║║─║║─║║─╔╗║╔╗║─     ╚══╗║║║─║║║╔╗╔╝──║║──
# ╚══╗║║╚═╝║╔╣─╗║╚═╝║║║║╚╗     ║╚═╝║║╚═╝║║║║╚╗──║║──
# ───╚╝╚═══╝╚══╝╚═══╝╚╝╚═╝     ╚═══╝╚═══╝╚╝╚═╝──╚╝──

def partition(nums, low, high):
    # Select the middle element as the pivot
    # It is also possible to select the first, last or arbitrary elements as reference
    pivot = nums[(low + high) // 2]
    i = low - 1
    j = high + 1
    while True:
        i += 1
        while nums[i] < pivot:
            i += 1

        j -= 1
        while nums[j] > pivot:
            j -= 1

        if i >= j:
            return j

        # If the element at index i (to the left of the pivot) is bigger than
        # element with index j (to the right of the pivot), swap them
        nums[i], nums[j] = nums[j], nums[i]


def quick_sort(nums):
    # Create a helper function that is called recursively
    def _quick_sort(items, low, high):
        if low < high:
            # This is the index after the pivot, where our lists are split
            split_index = partition(items, low, high)
            _quick_sort(items, low, split_index)
            _quick_sort(items, split_index + 1, high)

    _quick_sort(nums, 0, len(nums) - 1)


# ╔═╗╔═╗╔═══╗╔═══╗╔═══╗╔═══╗     ╔═══╗╔═══╗╔═══╗╔════╗
# ║║╚╝║║║╔══╝║╔═╗║║╔═╗║║╔══╝     ║╔═╗║║╔═╗║║╔═╗║║╔╗╔╗║
# ║╔╗╔╗║║╚══╗║╚═╝║║║─╚╝║╚══╗     ║╚══╗║║─║║║╚═╝║╚╝║║╚╝
# ║║║║║║║╔══╝║╔╗╔╝║║╔═╗║╔══╝     ╚══╗║║║─║║║╔╗╔╝──║║──
# ║║║║║║║╚══╗║║║╚╗║╚╩═║║╚══╗     ║╚═╝║║╚═╝║║║║╚╗──║║──
# ╚╝╚╝╚╝╚═══╝╚╝╚═╝╚═══╝╚═══╝     ╚═══╝╚═══╝╚╝╚═╝──╚╝──

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2

        # We split the array into two halves, find the index of the middle of the array
        # and create two new arrays - left_half and right_half
        left_half = arr[:mid]
        right_half = arr[mid:]

        # We recursively call the merge_sort function for each of these two arrays.
        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        # In the while loop, as long as i is less than the length of left_half and j is less than the length of right_half,
        # we compare the elements left_half[i] and right_half[j].
        # If left_half[i] is less than right_half[j], then write left_half[i] to arr[k] and increment i and k by 1.
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        # If there are elements left in left_half, copy them to arr, increasing i and k by 1
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        # Likewise for riht_half
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

    return arr


# ╔═══╗╔╗─╔╗╔═══╗╔╗───╔╗───     ╔═══╗╔═══╗╔═══╗╔════╗
# ║╔═╗║║║─║║║╔══╝║║───║║───     ║╔═╗║║╔═╗║║╔═╗║║╔╗╔╗║
# ║╚══╗║╚═╝║║╚══╗║║───║║───     ║╚══╗║║─║║║╚═╝║╚╝║║╚╝
# ╚══╗║║╔═╗║║╔══╝║║─╔╗║║─╔╗     ╚══╗║║║─║║║╔╗╔╝──║║──
# ║╚═╝║║║─║║║╚══╗║╚═╝║║╚═╝║     ║╚═╝║║╚═╝║║║║╚╗──║║──
# ╚═══╝╚╝─╚╝╚═══╝╚═══╝╚═══╝     ╚═══╝╚═══╝╚╝╚═╝──╚╝──

def shell_sort(arr):
    n = len(arr)
    gap = n // 2

    # It iterates over the array from current gap index to the end of the array, denoted by the range
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i

            # It compares the element at index `j - gap` with `temp` and if it is greater,
            # it shifts the element at index `j - gap` to index `j`,
            # effectively moving elements to the right until a correct position is found for `temp`.
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap

            # It assigns the value of `temp` to the index `j`, effectively placing `temp` at the correct position
            # within the sorted subarray.
            arr[j] = temp
        gap //= 2
    return arr


# ╔═══╗╔╗──╔╗╔═══╗╔═══╗╔═╗╔═╗╔══╗╔═══╗     ╔═══╗╔═══╗╔═══╗╔════╗
# ║╔═╗║║╚╗╔╝║║╔═╗║║╔═╗║║║╚╝║║╚╣─╝╚╗╔╗║     ║╔═╗║║╔═╗║║╔═╗║║╔╗╔╗║
# ║╚═╝║╚╗╚╝╔╝║╚═╝║║║─║║║╔╗╔╗║─║║──║║║║     ║╚══╗║║─║║║╚═╝║╚╝║║╚╝
# ║╔══╝─╚╗╔╝─║╔╗╔╝║╚═╝║║║║║║║─║║──║║║║     ╚══╗║║║─║║║╔╗╔╝──║║──
# ║║─────║║──║║║╚╗║╔═╗║║║║║║║╔╣─╗╔╝╚╝║     ║╚═╝║║╚═╝║║║║╚╗──║║──
# ╚╝─────╚╝──╚╝╚═╝╚╝─╚╝╚╝╚╝╚╝╚══╝╚═══╝     ╚═══╝╚═══╝╚╝╚═╝──╚╝──
def heapify(nums, heap_size, root_index):
    # The index of the largest element is considered the root index
    largest = root_index
    left_child = (2 * root_index) + 1
    right_child = (2 * root_index) + 2

    # If the left child of the root is a valid index and the element is bigger
    # than the current largest, update the largest element
    if left_child < heap_size and nums[left_child] > nums[largest]:
        largest = left_child

    # Same for the right child of the root
    if right_child < heap_size and nums[right_child] > nums[largest]:
        largest = right_child

    # If the largest element is no longer the root, they are swapped
    if largest != root_index:
        nums[root_index], nums[largest] = nums[largest], nums[root_index]

        # Heapify the new root element to ensure it's the largest
        heapify(nums, heap_size, largest)


def heap_sort(nums):
    n = len(nums)

    # Create Max Heap from list
    # The second argument means to stop the algorithm before the element -1,
    # i.e. before the first element of the list
    # The 3rd argument means iterate through the list in the opposite direction,decrement counter i by 1

    for i in range(n, -1, -1):
        heapify(nums, n, i)

    # Move the Max Heap Root to the End of the List
    for i in range(n - 1, 0, -1):
        nums[i], nums[0] = nums[0], nums[i]
        heapify(nums, i, 0)

