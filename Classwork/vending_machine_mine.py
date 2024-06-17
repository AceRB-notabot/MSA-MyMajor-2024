#create a variable for the amount due
#prompt user to input a coin of one of the accepted values
#error check user inputs
#display new amount due
#end program when no more is due
#if user overpays return the excess
'''
def amount_due():
    debt=50
    print(f"Amount Due: {debt}")
    return debt
'''

def get_coin():
    coin_list=[1, 5, 10, 25]
    while(True):
        try: 
            user_coin=int(input("Insert Coin:\n"))
        except:
            continue

        if user_coin in coin_list:
            break
        else:
            continue

    return user_coin
            
def main():
    print("Vending Machine\n -------------")
    amount_due=50

    while True:
        print(f"Amount Due: {amount_due}")
        user_coin=get_coin()
        amount_due-=user_coin
        if amount_due<=0:
            break
    
    print(f"Change Owed: {abs(amount_due)}")
main()