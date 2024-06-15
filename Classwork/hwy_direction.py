#create a program that accepts a hwy number and outputs the direction
#user enters: 95 
#Output: Interstate 95 runs south to north
#error check program so it does not crash
def get_hwy_number():
    hwy_number=0
    while(True):
        try:
            hwy_number=int(input("Enter the number of the interstate/highway: "))
            if hwy_number<=0:
                print("ERROR: please enter the roadway number as a positive integer")
                continue
            else:
                break
        except:
            print("ERROR: please enter the roadway number as a positive integer")
            continue
    
    
    return hwy_number

def check_even(hwy_number):
    remainder = hwy_number % 2
    if remainder == 1:
        return False
    else:
        return True
    

def main(): 
    hwy_number=get_hwy_number()
    evenness=check_even(hwy_number) 
    if  evenness == False:
        print(f"{hwy_number} runs north to south") 
    else:
        print(f"{hwy_number} runs east to west")
    
main()
    