
print('''
+ ADD
- SUBTRACT
* MULTIPLY
/ DIVIDE
''')

num1=int(input("value1:"))
num2=int(input("value2"))

if opr=="+":
    print(num1+num2)
elif opr=="-":
    print(num1-num2)
elif opr=="*":
    print(num1*num2)
elif opr=="/":
    print(num1/num2)
else:
    print(not found)