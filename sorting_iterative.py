def is_sorted(items):
    """
    Return a boolean indicating whether given items are in sorted order.
    Running time: O(n) It loops through every single item in the list to compare to its adjecent value
    Memory usage: No new memory taken up.
    """
    # Check that all adjacent items are in order, return early if so
    for i in range(len(items) - 1):
        if items[i] > items[i+1]:
            return False
    return True

def bubble_sort(items):
    """
    Sort given items by swapping adjacent items that are out of order, and repeating until all items are in sorted order.
    Running time: Worst Case: O(n^2) Average Case: O(n^2) Best Case: O(n) if list is already sorted.
    Memory usage: O(1), because only a single additional memory space is required for n temp variable 
    """
    # Repeat until all items are in sorted order
    # Swap adjacent items that are out of order
    n = len(items)
    for i in range(n - 1):
        for i in range(0, n - i - 1):
            if items[i] > items[i+1]:
                items[i], items[i + 1] = items[i + 1], items[i]
    return items


def selection_sort(items):
    """
    Sort given items by finding minimum item, swapping it with first
    unsorted item, and repeating until all items are in sorted order.
    Running time: Worst Case: O(n^2) Best case: O(n^2) Average case: O(n^2)
    No matter the case, even if its sorted, you loop through every items, then do it again subtracting 1 from the loop every time, on second loop.
    Memory usage: O(1) It will never make O(n) swaps, because it only swaps constant time at maximum swaps.
    """
    # Repeat until all items are in sorted order
    for i in range(len(items)):
        min_index = i
        for j in range(i+1, len(items)):
            # Find minimum item in unsorted items
            if items[min_index] > items[j]: 
                min_index = j
        # Swap it with first unsorted item
        items[i], items[min_index] =  items[min_index], items[i]
    return items

def insertion_sort(items):
    """
    Sort given items by taking first unsorted item, inserting it in sorted
    order in front of items, and repeating until all items are in order.
    Running time: Best case: O(n) if its sorted, Worst case: O(n^2) Average case: O(n^2)
    Memory usage: O(1) It always sets variables in constant time, not needed in outside scope.
    """
    # Repeat until all items are in sorted order
    for i in range(1, len(items)): # i starts at 1 so we can compare it to the element to the left of it.
        value = items[i] # Init value we are sorting
        # This loop first checks that the value still needs to be swapped(its less then the element to the left of it), then it makes sure i is not 0
        while value < items[i - 1] and i > 0:
            items[i], items[i - 1] = items[i - 1], items[i] # Swap elements
            i -= 1 # Update i to so we can compare next value
    return items

print(insertion_sort([5,3,4,3,2,4,20,200,1,6]))