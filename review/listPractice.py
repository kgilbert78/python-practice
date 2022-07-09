list1 = [3.1, 1.2, 5.9]
list2 = [3.0, 2.5]

list3 = list1 + list2

print(list3)

list4 = [3.1, 1.2, 5.9]
list5 = [3.0, 2.5]

list4 += list5

print("List 4: ", list4, "List 5: ", list5)

list5.append(3.9)
print("appended list 5: ", list5)