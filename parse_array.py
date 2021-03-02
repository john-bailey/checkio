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
def my_parse_array(input: str) -> list:
    try:
        data = literal_eval(input.strip())
        sehr_gut = True
    except:
        sehr_gut = False
    if not sehr_gut:
        raise ValueError
    return data

assert my_parse_array("[1, 2, 3]") == [1, 2, 3]
assert my_parse_array("[[1], 2, 3]") == [[1], 2, 3]
assert my_parse_array("[-3, [-2, 0], 10]") == [-3, [-2, 0], 10]

try:
    my_parse_array("[asd]")
    assert False, "Only integers"
except ValueError:
    pass

try:
    my_parse_array("[2, 3]]")
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
                raise ValueError(f'Wrong string: {ch}, not started_flag and not stack')
            if closed_flag or accumulator:
                raise ValueError(f'closed_flag or accumulator')
            in_array = []
            if stack:
                stack[-1](in_array)
            else:
                array = in_array
                started_flag = True
            stack.append(in_array.append)
        elif not started_flag:
            raise ValueError(f'Wrong string: {ch}, not started_flag')
        elif ch == "]":
            if not stack:
                raise ValueError(f'Wrong string: {ch}, not stack')
            if accumulator:
                stack[-1](int(accumulator))
                accumulator = ""
            stack.pop()
            if not stack:
                started_flag = False
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
                raise ValueError(f'Wrong string: {ch}, _sep but not accumulator and not closed_flag')
            sep_flag = True
            closed_flag = False
            whitespace_flag = False
        else:
            if whitespace_flag and accumulator or closed_flag:
                raise ValueError(f'whitespace_flag: {whitespace_flag} and accumulator {accumulator} or closed_flag {closed_flag}')
            accumulator += ch
        whitespace_flag = False
    if started_flag:
        raise ValueError(f'extra brackets')
    if not array is None:
        return array
    else:
        raise ValueError(f'array is None')


# fails
# returning "[3]" instead of ValueError
try:
    parse_array("[3],")
    assert False, "Excess separator"
except ValueError:
    pass

# fails
# returning "[[2]]" instead of ValueError
try:
    parse_array("[[2]")
    assert False, "Excess opened bracket"
except ValueError:
    pass

# testing
parse_array("[1, 2, 3],") == [1, 2, 3]

parse_array("[[1], 2, 3]") == [[1], 2, 3]



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

try:
    parse_array("[++2, 1]")
    assert False, "Two plus"
except ValueError:
    pass

try:
    parse_array("[10, 11, , 12]")
    assert False, "Two separators"
except ValueError:
    pass

try:
    parse_array(" 13 ")
    assert False, "Where is a list?"
except ValueError:
    pass

# fails
try:
    parse_array("[[2]")
    assert False, "Excess opened bracket"
except ValueError:
    pass

try:
    parse_array("[3 4]")
    assert False, "Check for spurious spaces within a number"
except ValueError:
    pass

try:
    parse_array("[10, 11,, 12]")
    assert False, "Check for double separators without a space in between"
except ValueError:
    pass

try:
    parse_array("[[]3]")
    assert False, "Check for missing separators after []"
except ValueError:
    pass

try:
    parse_array("[2[]]")
    assert False, " Check for missing separators before []"
except ValueError:
    pass

# fails
try:
    parse_array("[3],")
    assert False, "Excess separator"
except ValueError:
    pass

try:
    parse_array("[1,2]3")
    assert False, "Excess number"
except ValueError:
    pass

try:
    parse_array("[1], [2,3]")
    assert False, "Here should be only one array."
except ValueError:
    pass
