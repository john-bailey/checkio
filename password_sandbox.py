def eval_password(password: str) -> bool:
    if 'password' in password.lower():
        return False
    if len(set([i for i in password])) < 3:
        return False
    if len(password) > 9:
        return True
    count = sum([1 for i in password if i.isdigit()])
    has_digits = True if count > 0 and count < len(password) else False
    has_length = True if len(password) > 6 else False
    return  True if has_digits and has_length else False

assert eval_password('dope') == False
assert eval_password('dopebuzz') == False
assert eval_password('dopebuzzers') == True
assert eval_password('dopebu22') == True
assert eval_password('1234562') == False
assert eval_password('1234567890') == True
assert eval_password('password12345') == False
assert eval_password('PASSWORD12345') == False
assert eval_password('pass1234word') == True
assert eval_password('aaaaaa1') == False
assert eval_password('aaaaaabbbbb') == False
