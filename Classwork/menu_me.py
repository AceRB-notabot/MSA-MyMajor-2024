#get an item from the user
#ignore anything that isn't an item
#display total cost with a ($) and 2 decimel places
#end the program when the user types end in any case
#create a dictionary of the menu
#use the user input to check the menu's key value pairs


    
            
def main():

    menu_prices={
        "Baja Taco": 4.00,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00
    }

    total_price=0
    while True:

        user_item = input("Item: ")
        #check if the user entered end
        if user_item.lower() == "end":
            break

        if user_item in menu_prices.keys():
            total_price += menu_prices[user_item]
            print(f"Toatal: ${total_price:.2f}")
        else:
            continue
        

main()