def calc(x,y,ops):
    if ops not in "+-*/":
        return "only +-*/!!!!!"
    if ops=="+":
        return (str(x) +""+ ops +str(y)+"="+str(x+y))
    elif ops=="-":
        return (str(x) +""+ ops +str(y)+"="+str(x-y))
    elif ops == "*":
        return (str(x) + "" + ops + str(y) + "=" + str(x * y))
    elif ops == "/":
        return (str(x) + "" + ops + str(y) + "=" + str(x / y))
x=int(input("please enter first number"))
y=int(input("please enter second number"))
ops=input("choose between +,-,*,/")
print(calc(x,y,ops))
