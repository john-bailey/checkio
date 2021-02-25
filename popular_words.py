'''
In this mission your task is to determine the popularity of certain words in the text.

At the input of your function are given 2 arguments: the text and the array of words the popularity of which you need to determine.

When solving this task pay attention to the following points:

The words should be sought in all registers. This means that if you need to find a word "one" then words like "one", "One", "oNe", "ONE" etc. will do.
The search words are always indicated in the lowercase.
If the word wasn’t found even once, it has to be returned in the dictionary with 0 (zero) value.
Input: The text and the search words array.

Output: The dictionary where the search words are the keys and values are the number of times when those words are occurring in a given text.
'''

DATA = '''
The quick red fox
jumps over the lazy
dog, but the slow brown
raccoon beats it to the prize every time.
Brown raccoon over Red Fox for the win.
'''
# testing
print(DATA)
count = [1 for i in DATA.split() if i.lower() == 'the']
print(sum(count))

# function
def wordPopularity(text: str, keys: list) -> list:
    pophash = {} 
    for key in keys:
        count = sum([1 for i in text.split() if i.lower() == key])
        pophash[key] = count
    return pophash
 
assert wordPopularity(DATA, ['the']) == {'the': 5}
assert wordPopularity(DATA, ['over']) == {'over': 2}
assert wordPopularity(DATA, ['one']) == {'one': 0}
