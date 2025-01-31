def pren(a):
    result=[]
    for i in a:
        if i=="(":
            result.append(i)
        elif i==")":
            if result and result[-1]=="(":
                result.pop()
            else:
                return False
        else:
            pass
    return True
a="(a+b)(b+c))c-d("
print(pren(a))