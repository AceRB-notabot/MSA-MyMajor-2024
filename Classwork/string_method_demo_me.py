
def main():
    #capitilize a string
    my_name= "dietrich"
    print(my_name.capitalize())
    #make a string uppercase
    print(my_name.upper())
    #make a string lowercase
    last_name="PRALLE"
    print(f"{my_name.capitalize()} {last_name.lower()}")
    #determine if a string start with a set of characters
    print(my_name.startswith("d"))
    if(not my_name.startswith("diet") and not my_name.startswith("Diet")):
        print(f"You spelled {my_name} incorrectly")
    else:
        print(f"You spelled {my_name} correctly")
    #determine if a string ends with a specified set of characters
    print(my_name.endswith("rich"))
    #find a set of characters in a string
    print(my_name.find)
    
    
    
    
    
    
    
    
    
    print("\n\n")
    sentence= "I have a dog. My dog is cute. Do you want a dog?"
    #write code that counts the number of times dog is in the sentence
    #expected output: 3
    #use a while loop to read the string
    #start at the beginning of the string
    #read the string until you find the first occurance of dog
    #add one to the number of dogs
    #continue reading from the next index: update the start index in the find() method
    start_index=0
    number_of_dogs=0
    while True:
        dog_index= sentence.find("dog", start_index)
        if dog_index==-1:
            break
        else:
            number_of_dogs+=1
            start_index =dog_index+1 
            continue
    print(f"Number of Dogs: {number_of_dogs}")

    #how to use the split method
    car_info="ferarri,f-50,2021,500000,4.8"
    car_data=car_info.split(",")
    print(f"{car_data}")
    #get the individual items from the resulting list
    car_make=car_data[0]
    car_model=car_data[1]
    car_year=int(car_data[2])
    car_price=float(car_data[3])
    engine_size=float(car_data[4])
    
main()