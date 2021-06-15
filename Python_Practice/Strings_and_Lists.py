# -*- coding: utf-8 -*-
"""
 String & list methods

 STRING METHODS

"""
# upper(), lower(), isupper(), islower()
test_string = 'This is a test string'
print(test_string)
print("upper() method:", test_string.upper())
print("lower() method:", test_string.lower())

print("islower() method:", test_string.islower())
lower_string = test_string.lower()
print("islower() method:", lower_string.islower())

print("isupper() method:", test_string.isupper())
upper_string = test_string.upper()
print("isupper() method:", upper_string.isupper())

# isX() methods return boolean

# startswith() and endswith() methods return boolean

"""
 join() and split() methods
     * .join() returns a string.
     * .split() returns a list.
"""
new_string = ', and this is another string'
join_result = "".join([test_string, new_string])
print("join() method result:", join_result)
another_join = 'XX'.join([test_string, new_string])
print("Using XX as a separator:", another_join)

split_result = test_string.split()
print("split() method:", split_result)

another_split = join_result.split(sep=',')
print("split() method using ',':", another_split)

"""
 find() and rfind() methods
     * .find() returns index of substring.
     * .rfind() finds substring start at the end
       of the string.

"""
print("Index of 'a' is", test_string.find('a'),
      "in", "'"+test_string+"'")


print("Index of 'string' is",
      test_string.rfind('string'),
      "in", "'"+test_string+"'")

"""
 LIST METHODS
 sort(), sorted(), index(), find(), rfind()
     * .sort() takes a list and sorts it in place.
     * sorted() is a function, NOT a method.
       It is similar to sort() but instead returns
       a list which is sorted.
     * .index() returns zero-based index in the
       list of the first item whose value is equal
       to 'x'.

"""
dummy_list = ['d', 'c', 'b', 'a']
print("Unsorted list:", dummy_list)
dummy_list.sort()
print("Sorted list:", dummy_list)

dummy_list2 = ['3', '2', '1']
dummy_list2_sorted = sorted(dummy_list2)
print("Unsorted list:", dummy_list2)
print("Sorted list:", dummy_list2_sorted)

b_index = dummy_list.index('b')
print("'b' appears at position", b_index+1,
      "in string", dummy_list)
