#(Validating User Input) Modify the script of Fig. 3.3 to validate its inputs. 
#For any input, if the value entered is other than 1 or 2, keep looping until the user enters a correct
#value. Use one counter to keep track of the number of passes, then calculate the number
#of failures after all the user’s inputs have been received.

ehiz = True
total = 0

while (ehiz):
  fnum = int(input("Input the first integer: "))
  if fnum in range(1,3):
    total = total + fnum #2
    ehiz = False

ehiz = True

while (ehiz):
    snum = int(input("Enter the second integer: "))
    if snum in range(1,3):
      total = total + snum
      ehiz = False
      
print("The total sum of number is ", total)