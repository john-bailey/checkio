'''
Check if a given string has all symbols in upper case.
If the string is empty or doesn't have any letter in it - function should return False.
'''
def is_all_upper(text: str) -> bool:
    if len(text) == 0:
        return False
    filtered = ''.join([i for i in text if i.isalpha()])
    if len(filtered) == 0:
        return False
    return True if sum([1 for i in filtered if i.isupper()]) == len(filtered) else False

assert is_all_upper('ALL UPPER') == True
assert is_all_upper('all lower') == False
assert is_all_upper('mixed UPPER and lower') == False
assert is_all_upper('') == False
assert is_all_upper('12345') == False
assert is_all_upper('UPPER WITH NUMS 1234') == True

'''
Determine whether the sequence of elements items is ascending so that its each element is strictly larger than (and not merely equal to) the element that precedes it.
empty list or single item list == True
True if each n < (n + 1) else False
'''
from typing import List

def is_ascending(items: List[int]) -> bool:
    for n in range(len(items)):
        try:
            if items[n] >= items[n+1]:
                return False
        except IndexError:
            pass
    return True

assert is_ascending([-5, 10, 99, 123456]) == True
assert is_ascending([99]) == True
assert is_ascending([4, 5, 6, 7, 3, 7, 9]) == False
assert is_ascending([]) == True
assert is_ascending([1, 1, 1, 1]) == False
