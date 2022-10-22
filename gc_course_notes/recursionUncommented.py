def merge_sort(big_list):
    list_length = len(big_list)
    if list_length <= 1:
        return
    list_first_half = big_list[:list_length//2]
    list_second_half = big_list[list_length//2:]
    merge_sort(list_first_half)
    merge_sort(list_second_half)
    merge(big_list, list_first_half, list_second_half)
    return

def merge(big_list, list_first_half, list_second_half): 
    index_big_list = 0
    index_first_half = 0
    index_second_half = 0
    while (index_first_half < len(list_first_half)) or (index_second_half < len(list_second_half)):
        if index_first_half < len(list_first_half):
            if index_second_half < len(list_second_half):
                if list_first_half[index_first_half] < list_second_half[index_second_half]:
                    big_list[index_big_list] = list_first_half[index_first_half]
                    index_first_half += 1 
                else:
                    big_list[index_big_list] = list_second_half[index_second_half]
                    index_second_half += 1 
            else:
                big_list[index_big_list] = list_first_half[index_first_half]
                index_first_half += 1 
        else:
            big_list[index_big_list] = list_second_half[index_second_half]
            index_second_half += 1
        index_big_list += 1
    return

favorite_foods = ['pizza', 'barbeque', 'gumbo', 'chicken and dumplings', 'pecan pie', 'ice cream']
merge_sort(favorite_foods)
print(favorite_foods)
