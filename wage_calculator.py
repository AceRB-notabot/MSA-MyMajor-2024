#get two inputs from the user
#use math to calculate annual wage
workdays=400
tax=.12
def get_hours():
  user_hours=0
  while(True):
    try:
      user_hours=float(input("Enter your daily hours:"))
      if user_hours<=0:
        print("ERROR: Enter a number of hours greater than 0")
        continue
      elif user_hours>=24:
        print("ERROR: Enter a number of hours less than 24")
        continue
      else:
        break
    except:
      print("ERROR: Please enter a number of hours greater than 0")
  return user_hours
def get_wage():
  user_wage=0
  while(True):
    try:
      user_wage=float(input("Enter your hourly wage:"))
      if user_wage<=0:
        print("ERROR: Enter a number for your wage greater than 0")
        continue
      else:
        break
    except:
      print("ERROR: Please enter a number for your wage greater than 0")
  return user_wage
user_hours=get_hours()
user_wage=get_wage()
wage_before_tax=user_hours*user_wage*workdays
tax_total=wage_before_tax*tax
wage_post_tax=wage_before_tax-tax_total
print(f"Pay Advice\n ----------\n Hours Worked:{user_hours}\n User Wage:${user_wage}\n Wage Before Taxes:${wage_before_tax:.2f}\n Tax Amount:${tax_total:.2f}\n Annual Wage After Taxes:${wage_post_tax:.2f}")