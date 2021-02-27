# %%
test = 'add'
dir(test)
# %%
help(test.translate)

# %%
'add'.translate(('add'.split(), 'egg'.split()))
# %%
tr_table = ''.maketrans('add', 'egs')
'add'.translate(tr_table)
# %%
ord('a')

# %%
def isometric_strings(lhs: str, rhs: str) -> bool:
    trmatrix = {}
    for n in range(len(lhs)):
        try:
            if lhs[n] not in trmatrix:
                trmatrix[lhs[n]] = rhs[n]
            else:
                if trmatrix[lhs[n]] != rhs[n]:
                    return False
        except IndexError:
            return False
    return True

mylhs = 'foo'
myrhs = 'bar'
print(isometric_strings(mylhs, myrhs))
# %%
def isometric_strings(str1: str, str2: str) -> bool:
    print('===')
    print(set(zip(str1, str2)))
    print(len(set(zip(str1, str2))))
    print('+++')
    print(set(str1))
    print(len(set(str1)))
    print('===\n')
    return len(set(zip(str1, str2))) == len(set(str1))

assert isometric_strings('adp', 'egg') == True
assert isometric_strings('egg', 'adp') == False
assert isometric_strings('paper', 'words') == False
assert isometric_strings('paper', 'title') == True
assert isometric_strings('add', 'egg') == True
assert isometric_strings('foo', 'bar') == False
assert isometric_strings('', '') == True
assert isometric_strings('all', 'all') == True

# %%
str1 = 'adp'
str2 = 'egg'
print(set(zip(str1, str2)))
print(len(set(zip(str1, str2))))
print('===')
print(set(str1))
print(len(set(str1)))
# %%
str1 = 'paper'
str2 = 'words'
#dir(zip(str1, str2))
#help(zip)
print(set(zip(str1, str2)))
print(set(str1))

# %%
