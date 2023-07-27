cname = input("What is your name? ")
earnings = int(input("what are your earning? "))
if earnings <= 30000:
    calc = (15/100) * earnings
    print("Your tax is " + str(calc))
else:
    calcc = (20/100) * earnings
    print("Your tax is " + str(calcc))
