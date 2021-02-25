#
# parse.py
'''
 The initial and final markers are always different.
If there is no initial marker, then the first character should be considered the beginning of a string.
If there is no final marker, then the last character should be considered the ending of a string.
If the initial and final markers are missing then simply return the whole string.
If the final marker comes before the initial marker, then return an empty string.
'''
def parse_string(text: str, start: str, end: str) -> str:
    start_index = 0 if text.find(start) == -1 else text.find(start) + len(start)
    end_index = len(text) if text.find(end) == -1 else text.find(end)
    if start_index > end_index:
        return ''
    else:
        return text[start_index:end_index]

# Tests
assert parse_string("The quick brown fox jumps", "qu", "brown") == 'ick ', 'good match'
assert parse_string("The quick brown fox jumps", "qu", "brwn") == 'ick brown fox jumps', 'no end'
assert parse_string("The quick brown fox jumps", "qi", "fox") == 'The quick brown ', 'no start'
assert parse_string("The quick brown fox jumps", "brown", "The") == '', 'end before start'

print('Success')
