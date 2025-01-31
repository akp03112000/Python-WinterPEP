s=['a','b','b','a','b','c','c','c','a','b']
result=[]
for i in s:
    if not result:
     result.append(i)
    elif i == result[-1]:
     result.pop()
else:
    result.append(i)
    print (result)