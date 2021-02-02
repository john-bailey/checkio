#
# check if a given string is a palindrome

## Functions

# look for palindromes within a string
def find_longest_palindrome(teststr: str) -> str:
    pal = ''
    # slice string from the left
    for i in range(len(teststr)-1):
        lslice = teststr[i:]
        # slice string from the right and test if palindrome
        for j in range(len(lslice), 1, -1):
            rslice = lslice[:j]
            if rslice == rslice[::-1] and len(rslice) > len(pal):
                pal = rslice
    return pal

# check a string of words for palindromes
def find_longest_palindrome_in_words(sentence: str) -> str:
    wordpal = ''
    for word in sentence.split():
        output = find_longest_palindrome(word)
        if len(output) > len(wordpal):
            wordpal = output
    return wordpal

## Tests

# find_longest_palindrome function
assert find_longest_palindrome('foobarabaz') == 'barab','Slice Palindrome: barab'
assert find_longest_palindrome('foobarbaz') == 'oo','Slice Palindrome: oo'
assert find_longest_palindrome('fobarbaz') == '','No Palindrome'
print('find_longest_palindrome: Success')

# find_longest palindrome_in_words
assert find_longest_palindrome_in_words('hannah the cooked tacocat') == 'tacocat', 'Longest Palindrome'
assert find_longest_palindrome_in_words('hannah the cooked takoyaki') == 'hannah', 'Longest Palindrome'
assert find_longest_palindrome_in_words('hantah the zarbah takoyaki') == '', 'No Palindrome'
print('find_longest_palindrome_in_words: Success')

print('Success')