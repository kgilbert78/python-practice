# assuming the 2 strings are:
#   - the same length
#   - made up of lowercase letters a-z only
#   - have the same number of spaces (if any)
# then each character from the first string can be checked against the characters
# in the second string, and if they match, can be "checked off" via replacement.


def anagram_solution1(string1, string2):
    string2_list = list(string2)
    # conversion because lists are mutable, strings are not

    i = 0
    is_anagram = True

    while i < len(string1) and is_anagram:
        j = 0
        match_found = False
        while j < len(string2_list) and not match_found:
            if string1[i] == string2_list[j]:
                match_found = True
            else:
                j = j+1

        if match_found:
            string2_list[j] = None
        else:
            is_anagram = False

        i = i+1

    return (f"'{string1}' is an anagram of '{string2}': {is_anagram}")


# https://examples.yourdictionary.com/anagram-examples.html


result = anagram_solution1("heart", "earth")
print(result)

result2 = anagram_solution1("dusty", "study")
print(result2)

result3 = anagram_solution1("word", "work")
print(result3)

result4 = anagram_solution1("a gentleman", "elegant man")
print(result4)
