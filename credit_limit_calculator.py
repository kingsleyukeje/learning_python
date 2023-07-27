account_number = int(input("Enter your account number? "))
bal = int(input("Enter your balance at the beginning of the month? "))
items_charged = int(input("Enter your total of all items charged by the customer this month? "))
total_credits = int(input("enter total of all credits applied to the customer’s account this month? "))
allowed_credit = int(input("Enter your allowed credit limit? "))

new_balance = bal + items_charged - total_credits
print("Your new balance is " + str(new_balance))

if new_balance >= allowed_credit:
    print ("wahala dey oo")
else: 
    print ("You're good to go")