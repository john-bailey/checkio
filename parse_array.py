'''
You are given a string that contains a list with integers or nested lists.
The integers could have single plus or minus sign before them.
If the input string does not contain an array, then raise ValueError.
For an incorrectly formatted string -- raise ValueError.
Elements of the array are separated by commas
'''
# my solution
# works!
from ast import literal_eval
def parse_array(input: str) -> list:
    try:
        data = literal_eval(input.strip())
        sehr_gut = True
    except:
        sehr_gut = False
    if not sehr_gut:
        raise ValueError
    return data

assert parse_array("[1, 2, 3]") == [1, 2, 3]
assert parse_array("[[1], 2, 3]") == [[1], 2, 3]
assert parse_array("[-3, [-2, 0], 10]") == [-3, [-2, 0], 10]

try:
    parse_array("[asd]")
    assert False, "Only integers"
except ValueError:
    pass

try:
    parse_array("[2, 3]]")
    assert False, "Excess bracket"
except ValueError:
    pass

#==============================================

# checkio provided solution
# find the bugs
WHITESPACE_STR = ' \t\n\r'
def parse_array(s, _w=WHITESPACE_STR, _sep=","):
    array = None
    stack = []
    accumulator = ""
    closed_flag = False
    sep_flag = False
    whitespace_flag = False
    started_flag = False
    for ch in s:
        if ch in _w:
            whitespace_flag = True
            continue
        if ch == "[":
            if started_flag and not stack:
                raise ValueError("Wrong string.")
            if closed_flag or accumulator:
                raise ValueError
            in_array = []
            if stack:
                stack[-1](in_array)
            else:
                array = in_array
                started_flag = True
            stack.append(in_array.append)
        elif not started_flag:
            raise ValueError("Wrong string.")
        elif ch == "]":

            if not stack:
                raise ValueError("Wrong string.")
            if accumulator:
                stack[-1](int(accumulator))
                accumulator = ""
            stack.pop()
            closed_flag = True
            sep_flag = False
            whitespace_flag = False
        elif ch in _sep:
            if accumulator:
                stack[-1](int(accumulator))
                accumulator = ""
            elif closed_flag:
                pass
            else:
                raise ValueError("Wrong string.")
            sep_flag = True
            closed_flag = False
            whitespace_flag = False
        else:
            if whitespace_flag and accumulator or closed_flag:
                raise ValueError
            accumulator += ch
        whitespace_flag = False
    if not array is None:
        return array
    else:
        raise ValueError("Wrong string")


#These "asserts" using only for self-checking and not necessary for auto-testing
assert parse_array("[1, 2, 3]") == [1, 2, 3], "Simple"
assert parse_array("[[1], 2, 3]") == [[1], 2, 3], "Nested"
assert parse_array("[-3, [-2, 0], 10]") == [-3, [-2, 0], 10], "Negative integers"
assert parse_array("[100]") == [100], "One number"
assert parse_array("[2,     3]") == [2, 3], "Whitespaces"
assert parse_array("[[10, [11]], [[[1], 2], 3], 5]") == [[10, [11]], [[[1], 2], 3], 5], "Deep nested"
assert parse_array("   [3, 4]   ") == [3, 4], "Skip whitespaces"
assert parse_array("[[], 0]") == [[], 0], "Empty arrays"
assert parse_array("[[0,], 0]") == [[0], 0], "Comma - closed bracket"

try:
    parse_array("[asd]")
    assert False, "Only integers"
except ValueError:
    pass

try:
    parse_array("[2, 3]]")
    assert False, "Excess bracket"
except ValueError:
    pass
