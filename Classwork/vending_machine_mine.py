#create a variable for the amount due
#prompt user to input a coin of one of the accepted values
#error check user inputs
#display new amount due
#end program when no more is due
def amount_due():
    debt=50
    print(f"Amount Due: {debt}")
def get_coin():
    coin_list=[1, 5, 10, 25]
    while(True):
        user_coin=int(input("Insert Coin: "))
        if user_coin in coin_list:
            
def main():
    print("Vending Machine\n -------------")
main()