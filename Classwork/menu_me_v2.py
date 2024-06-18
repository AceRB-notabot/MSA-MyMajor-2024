#a funtion to load menu items from the file and create a dictionary
#input:none
#output: dictionary of menu items
def get_menu_items():
    #create a file handle that gives us access to the file
    data_file = open("menu.txt", "+r")
    
    #create an empty dictionary to store menu items and prices
    menu_items = {}

    #loop through data in the file and read the file one line at a time
    for line_of_data in data_file:

    
        #split the line of data at the comma using .split()
        keys_and_values= line_of_data.split(",")

        #get item and price from the resulting list and store in the dictionary
        item = keys_and_values[0]
        price= float(keys_and_values[1])
        menu_items[item] = price
    #close the file
    data_file.close()

    return menu_items


def main():
    menu_items = get_menu_items()

    

    total_price=0
    while True:

        user_item = input("Item: ")
        #check if the user entered end
        if user_item.lower() == "end":
            break

        if user_item in menu_items.keys():
            total_price += menu_items[user_item]
            print(f"Toatal: ${total_price:.2f}")
        else:
            continue
        

main()