# selection sort goes through entire unsorted list on each iteration, inefficient
def selection_sort(my_list):
    max_index = len(my_list) - 1
    for sort_position_index in range(0, max_index - 1):

    # find the smallest remaining in the rest of the elements

        # assume smallest is first in remaining list
        min_index = sort_position_index
        # loop thru rest & if find smaller one, update min_index
        for remaining_elements_index in range(sort_position_index + 1, max_index + 1):
            if my_list[remaining_elements_index] < my_list[min_index]:
                min_index = remaining_elements_index

    # swap that item
        temp = my_list[sort_position_index]
        my_list[sort_position_index] = my_list[min_index]
        my_list[min_index] = temp

favorite_foods = ['pizza', 'barbeque', 'gumbo', 'chicken and dumplings', 'pecan pie', 'ice cream']

selection_sort(favorite_foods)
print(favorite_foods) # in-place sort (changes original list) 
# ... out-of-place would create a copy to sort, maintains original list unchanged.


# insertion sort is more efficient, sort elements above the index and on each iteration add one more element into the right spot
def insertion_sort(my_list):
    for item_to_sort_index in range(0, len(my_list)):
        temp = my_list[item_to_sort_index]
        # working backward through the sorted ones...
        sorted_items_index = item_to_sort_index - 1
        while (sorted_items_index >= 0) and (my_list[sorted_items_index] > temp):
            # (move each item 1 place to make room for inserting)
            my_list[sorted_items_index + 1] = my_list[sorted_items_index]
            sorted_items_index -= 1
        # ...to find where to insert the current one (beginning of list or after element not greater than the one to insert)
        my_list[sorted_items_index + 1] = temp

favorite_foods2 = ['pizza', 'barbeque', 'gumbo', 'chicken and dumplings', 'pecan pie', 'ice cream']

selection_sort(favorite_foods2)
print(favorite_foods2)

# Use Python's built in search functions (combo of insertion sort and merge sort - very efficient):

# in-place sort (changes original list)
favorite_foods3 = ['pizza', 'barbeque', 'gumbo', 'chicken and dumplings', 'pecan pie', 'ice cream']
favorite_foods3.sort()

# out-of-place would create a copy to sort, maintains original list unchanged.
favorite_foods4 = ['pizza', 'barbeque', 'gumbo', 'chicken and dumplings', 'pecan pie', 'ice cream']
sortedFavorites = sorted(favorite_foods4)
print(favorite_foods4)
print(sortedFavorites)