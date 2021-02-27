def checkio(text: str) -> bool:
    found = []
    brackets = {'(': ')', '[': ']', '{': '}'}
    for n in text:
        if n in brackets.keys():
            found.append(n)
        elif n in brackets.values():
            try:
                if brackets[found.pop()] != n:
                    return False
            except IndexError:
                return False
    return True if len(found) == 0 else False

assert checkio("((5+3)*2+1)") == True

assert checkio("{[(3+1)+2]+}") == True

assert checkio("(3+{1-1)}") == False

assert checkio("[1+1]+(2*2)-{3/3}") == True

assert checkio("(({[(((1)-2)+3)-3]/3}-3)") == False

assert checkio("2+3") == True
