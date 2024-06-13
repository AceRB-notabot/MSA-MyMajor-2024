def main():
    #list demo
    #create a list of string names
    names=["john", "mary", "alice", "bob"]
    list_of_integers=[10, 16, 24, 42, 14, 9]
    random_type_list=["cyd", 15, 22.3, "Frank"]
    print(names)
    print(list_of_integers)
    #add values to a list
    names.append("jonny")
    list_of_integers.append(5)
    list_of_integers.append(63)
    print(names)
    print(list_of_integers)
    #get the number of items in a list
    number_of_items=len(list_of_integers)
    print("\n\n")
    print(f"Number of items in integer list: {number_of_items}")
    #get values from our list
    #get the first value in the list of integers
    print(f"\n First item in integer list: {list_of_integers[0]}")
    #get the fourth value from integer list
    print(f"\nFourth item in integer list: {list_of_integers[3]}")
    #print all items on list of integer
    print("\nInteger list items:")
    for item in list_of_integers:
        print(item)
    print("\n")
    for index in range(number_of_items):
        print(f"Item {index+1}: {list_of_integers[index]}")
main()