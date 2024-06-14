#create a function to return the season based on the month
#input: month number
#ouput: season name
#create a decision structure to determine the season: winter, spring, summer, fall, based on month
#winter:12, 1, 2, spring: 3, 4, 5, summer: 6, 7, 8, fall: 9, 10, 11
#have the user enter the number value (1-12) of the month andf determine the season
def get_season():
    user_month=0
    while(True):
        try:
            user_month=int(input("Enter the number of the month:"))
            if user_month<1 or user_month>12:
                print("ERROR: Please enter a whole number for month between 1 and 12")
                continue
            else:
                break
        except:
            print("ERROR: Please enter a whole number for month between 1 and 12")
    if user_month==12 or user_month==1 or user_month==2:
        season='Winter'
    elif user_month in range(3, 5):
        season='Spring'
    elif user_month in range(6, 8):
        season='Summer'
    else:
        season='Fall'
    return season
def main():
   season=get_season()
   print(f"The season is {season}")
   #ask user if they want to continue
   run_again=input("Do you want to run the program again? y or Y")
    
main()