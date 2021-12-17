# Create CSV files with mad lib data & import them.
    # https://www.geeksforgeeks.org/working-csv-files-python/
    # https://docs.python.org/3/library/csv.html
import csv

csv_text = "data/mad_libs_text.csv"
csv_input_categories = "data/mad_libs_input_categories.csv"


# Create MadLib class, each instance will be one mad lib.


# In each instance, create list of requirements (adjective, noun, etc) from CSV data. 

input_categories_list = []
with open(csv_input_categories, newline='') as csvfile_categories:
    csvreader_categories = csv.reader(csvfile_categories, delimiter=',')
    for row in csvreader_categories:
        input_categories_list.append(row)
print("\n", "INPUT CATEGORIES LIST:", "\n", "\n", input_categories_list)

# In each instance, create list of strings for text between blanks, interspersed with numbers each representing the index of the category on the requirements list, from CSV data.

text_list = []
with open(csv_text, newline='') as csvfile_text:
    csvreader_text = csv.reader(csvfile_text, delimiter=',')
    for row in csvreader_text:
        text_list.append(row)
print("\n", "TEXT LIST:", "\n", "\n", text_list)


## TEST OF PRINTING OUT FULL TEXT WITH NUMBERS WHERE USER INPUT GOES
# with open(csv_text, newline='') as csvfile__print_text:
#     csvreader__print_text = csv.reader(csvfile__print_text, delimiter=',')
#     for row in csvreader__print_text:
#         print("\n", "TEXT AS STRING:", "\n", "\n", ' '.join(row))


# Get user's inputs for each requirement and save them to a new list at the same indexes as their requirements.

# Print interspersed list to screen as concatenated string.

# Option to save concatenated string as a text file?

# ADD LATER:
# Use NLP library to check that what the user entered matches what the mad lib asked for (adjective, etc.)