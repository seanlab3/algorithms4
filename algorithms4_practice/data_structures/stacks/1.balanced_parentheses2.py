examples = ['((()))', '((())', '(()))']
def check(parentheses):
    alist=[]
    for i in parentheses:
        if i=="(":
            alist.append(i)
        elif i==")":
            if len(alist)<1:
                return False
            else:
                alist.pop()
    if len(alist)>=1:
        return False
    else:
        return True
def group_check(s):
    if s == "":
        return True
    if len(s) % 2 != 0:
        return False
    for i in range(len(s) - 1):
        if s[i] + s[i + 1] in ["[]", "()", "{}"]:
            return group_check(s[:i] + s[i + 2:])
    return False

for i in examples:
    print(check(i))
