# Create CSV files with mad lib data & import them.
    # https://www.geeksforgeeks.org/working-csv-files-python/
    # https://docs.python.org/3/library/csv.html
import csv

csv_text = "data/mad_libs_text.csv"
csv_input_categories = "data/mad_libs_input_categories.csv"

def format_prompts(prepend_str, list, append_str):
    new_list = []
    for index in range(len(list)):
        list_item = prepend_str + list[index] + append_str
        index + 1
        new_list.append(list_item)
    return new_list


# Create MadLib class, each instance will be one mad lib.


# In each instance, create list of requirements (adjective, noun, etc) from CSV data. 

input_categories_lists = []
with open(csv_input_categories, newline='') as csvfile_categories:
    csvreader_categories = csv.reader(csvfile_categories, delimiter=',')
    for row in csvreader_categories:
        input_categories_lists.append(row)
# print("\n", "INPUT CATEGORIES LIST:", "\n", "\n", input_categories_list)

# In each instance, create list of strings for text between blanks, interspersed with numbers each representing the index of the category on the requirements list, from CSV data.

text_list = []
with open(csv_text, newline='') as csvfile_text:
    csvreader_text = csv.reader(csvfile_text, delimiter=',')
    for row in csvreader_text:
        text_list.append(row)
# print("\n", "TEXT LIST:", "\n", "\n", text_list)


## TEST OF PRINTING OUT FULL TEXT WITH NUMBERS WHERE USER INPUT GOES
# with open(csv_text, newline='') as csvfile__print_text:
#     csvreader__print_text = csv.reader(csvfile__print_text, delimiter=',')
#     for row in csvreader__print_text:
#         print("\n", "TEXT AS STRING:", "\n", "\n", ' '.join(row))


# Get user's inputs for each requirement and save them to a new list at the same indexes as their requirements.
print("\nThese are the titles of the current available Mad Libs:", "\n")
for title in input_categories_lists:
    print(input_categories_lists.index(title) + 1, title[0])
title_choice = int(input("\nPlease enter the number next to one of them to choose it: \n")) - 1

print("You chose " + (input_categories_lists[title_choice])[0] + ".")
chosen_title_text_list = text_list[title_choice]

# make this more readable
chosen_title_categories_list = (input_categories_lists[title_choice])[1:len(input_categories_lists[title_choice])]

user_prompt_list = format_prompts("Please enter a word that fits the category ", chosen_title_categories_list, ": ")
# make format_prompts a method within the class once I create the class

user_input_list = chosen_title_categories_list # temp for testing (real code below)
# user_input_list = []
# for category in user_prompt_list:
#     user_input = input(category)
#     user_input_list.append(user_input)
#     # before adding NLP, add basic checks that user entered something, and for "verb ending in ing" it has "ing" as the last 3 letters etc.
# print(user_input_list)


# Print interspersed list to screen as concatenated string.
completed_madlib_list = chosen_title_text_list.copy()

    # for each item in user_input_list, match the index of that item to the (unstringified) number in the chosen_title_text_list that equals that item's index number.

for i in range(len(user_input_list)):
    for j in range(len(completed_madlib_list)):
        if str(i) == completed_madlib_list[j]:
            completed_madlib_list[j] = user_input_list[i]

    # format to print nicely to screen
completed_madlib = " ".join(completed_madlib_list) 
# add conditions to eliminate spaces before punctuation and interpret \n or \" instead of printing it.
print(completed_madlib)

# Option to save concatenated string as a text file?

# ADD LATER:
# Use NLP library to check that what the user entered matches what the mad lib asked for (adjective, etc.)