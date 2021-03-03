# checkio provided solution
# find the bugs
WHITESPACE_STR = ' \t\n\r'
def parse_array(s, _w=WHITESPACE_STR, _sep=","):
    array = None
    stack = []
    accumulator = ""
    closed_flag = False
    whitespace_flag = False
    started_flag = False
    for ch in s:
        if ch in _w:
            # skip all whitespace
            whitespace_flag = True
            continue
        if ch == "[":
            # VALID conditons for opening bracket
            # first
            # after whitespace
            # after another opening bracket
            # after a separator
            # after a separator and whitespace

            # INVALID conditions for opening bracket
            # after a closing bracket without a separator
            # after a character without a separator
            if started_flag and not stack:
                # started_flag is set at opening bracket
                # stack is popped at closing bracket
                raise ValueError(f'Wrong string: {ch}, not started_flag and not stack')
            if closed_flag or accumulator:
                # opening bracket requires separator after closing bracket or character
                raise ValueError(f'closed_flag or accumulator')
            # create a new list object
            in_array = []
            if stack:
                # append list to array
                stack[-1](in_array)
            else:
                array = in_array
                started_flag = True
            # append list.append method to LIFO stack
            stack.append(in_array.append)
            whitespace_flag = False
        elif not started_flag:
            # this catches anything before an opening bracket OR whitespace
            raise ValueError(f'Wrong string: {ch}, not started_flag')
        elif ch == "]":
            # VALID conditions for a closing bracket
            # after an opening bracket (empty list)
            # after a character
            # after a separator
            # after another closing bracket
            # after whitespace

            # INVALID conditions for a closing bracket
            # before an opening bracket
            if not started_flag:
                # there are more closing brackets than opening brackets
                raise ValueError(f'Wrong string: {ch}, not stack')
            if accumulator:
                # a closing bracket after a character is valid
                # the accumulation is finished; append int to array
                stack[-1](int(accumulator))
                accumulator = ""
            # removing the top of the LIFO stack
            stack.pop()
            if not stack:
                # indicate that this should be the last list
                started_flag = False
            closed_flag = True
            whitespace_flag = False
        elif ch in _sep:
            # VALID conditions for a separator:
            # after a character (value in accumulator)
            # after a closing bracket (closed_flag == True)

            # INVALID conditions for a separator:
            # before the first starting bracket
            #     caught above by conditional
            # without being after a closing bracket OR a character 
            #     caught below by conditional
            if accumulator:
                # a separator after a character is valid
                # the acculation is finished; append int to array
                stack[-1](int(accumulator))
                accumulator = ""
            elif closed_flag:
                # a separator after a closing bracket is valid
                pass
            else:
                raise ValueError(f'Wrong string: {ch}, _sep but not accumulator and not closed_flag')
            closed_flag = False
            whitespace_flag = False
        else:
            # VALID conditions for a character
            # after starting bracket
            #     started_flag == True
            # after a starting bracket and whitespace
            #     started_flag == True AND whitespace_flag == True
            # after a separator
            # after a separator and whitespace
            # after another character
            #     value in accumulator

            # INVALID conditions
            # whitespace + accumulator > 0
            #     whitespace_flag == True AND accumulator
            # closed_flag = True
            #     no separator
            #     _sep block sets closed_flag and whitespace_flag to False
            if (whitespace_flag and accumulator) or closed_flag:
                raise ValueError(f'Wrong string: {ch}')
            accumulator += ch
            whitespace_flag = False
    if started_flag:
        # There were more opening brackets than closing brackets
        raise ValueError(f'extra brackets')
    if not array is None:
        return array
    else:
        raise ValueError(f'array is None')



assert parse_array("[100]") == [100], "One number"
assert parse_array("   [3, 4]   ") == [3, 4], "Skip whitespaces"
assert parse_array("[[0,], 0]") == [[0], 0], "Comma - closed bracket"

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
print('Asserts Passed')

try:
    parse_array("[asd]")
    assert False, "Only integers"
except ValueError as ve:
    print(f'ValueError: {ve}')

try:
    parse_array("[2, 3]]")
    assert False, "Excess bracket"
except ValueError as ve:
    print(f'ValueError: {ve}')

try:
    parse_array("[++2, 1]")
    assert False, "Two plus"
except ValueError as ve:
    print(f'ValueError: {ve}')

try:
    parse_array("[10, 11, , 12]")
    assert False, "Two separators"
except ValueError as ve:
    print(f'ValueError: {ve}')

try:
    parse_array(" 13 ")
    assert False, "Where is a list?"
except ValueError as ve:
    print(f'ValueError: {ve}')

# fails
try:
    parse_array("[[2]")
    assert False, "Excess opened bracket"
except ValueError as ve:
    print(f'ValueError: {ve}')

try:
    parse_array("[3 4]")
    assert False, "Check for spurious spaces within a number"
except ValueError as ve:
    print(f'ValueError: {ve}')

try:
    parse_array("[10, 11,, 12]")
    assert False, "Check for double separators without a space in between"
except ValueError as ve:
    print(f'ValueError: {ve}')

try:
    parse_array("[[]3]")
    assert False, "Check for missing separators after []"
except ValueError as ve:
    print(f'ValueError: {ve}')

try:
    parse_array("[2[]]")
    assert False, " Check for missing separators before []"
except ValueError as ve:
    print(f'ValueError: {ve}')

# fails
try:
    parse_array("[3],")
    assert False, "Excess separator"
except ValueError as ve:
    print(f'ValueError: {ve}')

try:
    parse_array("[1,2]3")
    assert False, "Excess number"
except ValueError as ve:
    print(f'ValueError: {ve}')

try:
    parse_array("[1], [2,3]")
    assert False, "Here should be only one array."
except ValueError as ve:
    print(f'ValueError: {ve}')
