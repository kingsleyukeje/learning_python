def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def mul(x, y):
    return x * y

def div(x, y):
    return x / y

def prompt ():
    print ("Welcome to your personal calculator")   
    print("""       
        Enter 1: For Addition
        Enter 2: For Subtraction
        Enter 3: For Multiplication
        Enter 4: For Division
        Enter 0: To exit""")

sentinel= True

while sentinel:
    prompt()
    
    num = int(input("Enter number? "))

    if num > 4:
        print ("Please be serious")
        continue

    
    firnum = int(input("Enter first number you want to calculate? "))
    secnum = int(input("Enter second number you want to calculate? "))

    if num == 1:
        answer = add(firnum, secnum)
        print ("Your answer is " + str(answer))
    elif num == 2:
        answer = sub(firnum, secnum)
        print ("Your answer is " + str(answer))
    elif num == 3:
        answer = mul(firnum, secnum)
        print ("Your answer is " + str(answer))
    else:
        answer = div(firnum, secnum)
        print ("Your answer is " + str(answer))  

    print ("Do you want to continue. Press 0 to exit")
    
    num = int(input("Enter number? "))

    if num == 0:
        sentinel = False



