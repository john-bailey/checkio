# find the second occurance of a character in a string or return None
from typing import Union

def second_index(text: str, key: str) -> Union[int, None]:
    first = text.find(key)
    if first == -1 or first+1 == len(text):
        return None
    second = text.find(key, first+1)
    if second == -1:
        return None
    else:
        return second

if __name__ == '__main__':
    assert second_index("sims", "s") == 3, "First"
    assert second_index("find the river", "e") == 12, "Second"
    assert second_index("hi", " ") is None, "Third"
    assert second_index("hi mayor", " ") is None, "Fourth"
    assert second_index("hi mr Mayor", " ") == 5, "Fifth"
    print('You are awesome! All tests are done! Go Check it!')
