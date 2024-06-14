def get_month():
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
  return user_month
def main():
    a=7
    b=7
    if a>b:
        print(f"{a} is greater than {b}")
    elif b>a:
        print(f"{b} is greater than {a}")
    else:
        print(f"{a} is equal to {b}")
    #print the appropriate letter grade for the score
    #A:100-90, B:89-80, C:79-70, D:69-60, F
    print("\nGrade Decision: 1")
    test_score=90
    if test_score<=100 and test_score>=90:
        print(f"{test_score} --> A")
    elif test_score<90 and test_score>=80:
        print(f"{test_score} --> B")
    elif test_score<80 and test_score>=70:
        print(f"{test_score} --> C")
    elif test_score<70 and test_score>=60:
        print(f"{test_score} --> D")
    else:
        print(f"{test_score} --> F")
    #grade decision statement restructured
    print("\nGrade Decision: 2")
    if test_score>=90:
        print(f"{test_score} --> A")
    elif test_score>=80:
        print(f"{test_score} --> B")
    elif test_score>=70:
        print(f"{test_score} --> C")
    elif test_score>=60:
        print(f"{test_score} --> D")
    else:
        print(f"{test_score} --> F")
    #create a decision structure to determine the season: winter, spring, summer, fall, based on month
    #winter:12, 1, 2, spring: 3, 4, 5, summer: 6, 7, 8, fall: 9, 10, 11
    #have the user enter the number value (1-12) of the month andf determine the season
    user_month=get_month()
    if user_month==12 or user_month==1 or user_month==2:
        print("It is winter")
    elif user_month in range(3, 5):
        print("It is spring")
    elif user_month in range(6, 8):
        print("It is summer")
    else:
        print("It is fall")
main()