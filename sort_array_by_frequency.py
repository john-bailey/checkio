# sort_array_by_frequency.py
'''
Sort the given iterable so that its elements end up in the decreasing frequency order, 
that is, the number of times they appear in elements. If two elements have the same frequency, 
they should end up in the same order as the first appearance in the iterable.
'''
def frequency_sort(items: list) -> list:
    sorted_list = []
    # get the frequency
    count_dict = {i: items.count(i) for i in items}
    # increment through the count dictionary keys, sorted by frequency
    for j in sorted(count_dict, key=lambda x: count_dict[x], reverse=True):
        # extend the list with each item in items that matches
        sorted_list.extend([i for i in items if i == j])
    return sorted_list

assert frequency_sort([4, 6, 2, 2, 6, 4, 4, 4]) == [4, 4, 4, 4, 6, 6, 2, 2]
assert frequency_sort([6, 4, 2, 2, 6, 4, 4, 4]) == [4, 4, 4, 4, 6, 6, 2, 2]
assert frequency_sort([4, 2, 6, 2, 6, 4, 4, 4]) == [4, 4, 4, 4, 2, 2, 6, 6]
assert frequency_sort(['bob', 'bob', 'carl', 'alex', 'bob']) == ['bob', 'bob', 'bob', 'carl', 'alex']
