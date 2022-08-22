import math
print('''Choose either 'investment' or 'bond' from the menu below to proceed

investment = to calculate the amount of interest you'll earn on interest
bond = to calculate the amount youll have to pay on a home loan''')



choice = input("Enter your choice from the above: ")


if choice == "investment": #If user selects investment below questions shoud be generated to them. 
   P= float(input("enter the amount of money you are depositing: "))

   r= float(input("enter the interest rate without percentage symbol: "))

   t= float(input("enter the number the number of years you plan to invest: "))
    
   interest =input("enter whether you want simple interest or compound interest: ")



   if interest == "simple interest" :#formula to calculate simple interest
       print(P*(1+r*t))
          
   elif interest == "compound interest" :
       print(P* math.pow((1+r),t))



interest_rate = "monthly interest rate"
Present_value = "present value of the house"
num_months = "number of months the bond will be repaid"

if choice == "bond":

  Present_value= float(input("Enter the present value of the house: "))
  interest_rate= float(input("Enter the interest rate: "))
  num_months = float(input("Enter the number of months you plan to repay the bond: "))
  Total = ((interest_rate*Present_value)/(1 -(1+interest_rate)**(-num_months)))
  print(Total) 

else:
    print("invalid.Try again: ")





