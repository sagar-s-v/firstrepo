tuffle_1 = ('item1', 'item2', 'item3')
print(tuffle_1)
# We can only print or acess elements, but not modify them in tuffle unlike list.
# We can use tuffle to store multiple data types in a single variable.
tuffle_2 = ('item2',3.14, True, 5)
print(tuffle_2)
#------------------------------------------------------------------------------------------------#
#sets#
set_1 = {'item1', 'item2', 'item3','item2'}  # Sets are unordered collections of unique elements and removes duplicates.
set_2 = {'item4', 'item5', 'item6','item3'}
print(set_1)
print(set_2.intersection(set_1))  # This will print the common elements between set_1 and set_2.
print(set_1.union(set_2))  # This will print the union of set_1 and set_2.
print(set_1.difference(set_2))  # This will print the elements in set_1 that are not in set_2.