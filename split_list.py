# split_list.py
'''
You have to split a given array into two arrays.
If it has an odd amount of elements, then the first array should have more elements.
If it has no elements, then two empty arrays should be returned.
'''

def split_list(array: list) -> list[list]:
    split_array = []
    parity = 0 if len(array) % 2 == 0 else 1
    split_array.append(array[:int(len(array)/2 + parity)])
    split_array.append(array[int(len(array)/2 + parity):])
    return split_array

assert split_list([1, 2, 3, 4, 5, 6]) == [[1, 2, 3], [4, 5, 6]]
assert split_list([1, 2, 3]) == [[1, 2], [3]]
assert split_list([]) == [[], []]

'''
In this mission you should check if all elements in the given list are equal.
'''

def all_the_same(array: list) -> bool:
    try:
        is_equal = True if int(len(array)) == array.count(array[0]) else False
    except IndexError:
        is_equal = True
    return is_equal

assert all_the_same([1, 1, 1]) == True
assert all_the_same([1, 2, 1]) == False
assert all_the_same(['a', 'a', 'a']) == True
assert all_the_same([]) == True
