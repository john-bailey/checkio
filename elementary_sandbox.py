# %% [markdown]
## End Zeros

### find out how many zeros a given number has at the end

# %%
def end_zeros(number: int) -> int:
    count = 0
    for n in str(number)[::-1]:
        if n == '0':
            count += 1
        else:
            break
    return count

# %%
assert end_zeros(0) == 1
assert end_zeros(1) == 0
assert end_zeros(10) == 1
assert end_zeros(100) == 2
assert end_zeros(101) == 0
print ('success')

# %% [markdown]
## Remove all before

### remove all elements before the given one

# %%
def remove_all_before(data: list, border: int) -> list:
    try:
        return data[data.index(border):]
    except ValueError:
        return data
# %%
assert remove_all_before([1, 2, 3, 4, 5], 3) == [3, 4, 5]
assert remove_all_before([1, 2, 3, 4, 5], 6) == [1, 2, 3, 4, 5]
assert remove_all_before([1, 1, 2, 2, 3, 3], 2) == [2, 2, 3, 3]
assert remove_all_before([], 3) == []
print('Success')
# %% [markdown]
## All upper

### check if all is upper case

#### If the string is empty or doesn't have any letter in it - function should return True.

# %%
def is_all_upper(text: str) -> bool:
    return False if [i for i in text if i.islower()] else True

# %%
assert is_all_upper('ALL UPPER') == True
assert is_all_upper('all lower') == False
assert is_all_upper('mixed UPPER and lower') == False
assert is_all_upper('') == True
assert is_all_upper('444') == True
assert is_all_upper('55 55 5') == True
print('Success')
# %%
