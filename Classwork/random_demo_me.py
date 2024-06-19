import random
def main():
    #print a random number between one and ten
    print("Random number: 1 - 10")
    random_value = random.randint(1, 10)
    print(f"Random value: {random_value}")
    #generate ten random numbers between one and ten
    for i in range(10):
        print("\nRandom number: 1 - 10\n-----------")
        print(f"Random number {i+1}: {random.randint(1, 10)}")
    #choose a randoim value from a liust of values
    rand_list = [4, 7, 10, 5, 8, 24, 44, 18, 9, 12]
    random_index = random.randint(0, len(rand_list) - 1)
    print(f"Random index: {random_index + 1}")
    print(f"Random list value: {rand_list[random_index]}")
    #ask a user for the start and stop values to generate a random number between them
    #ask user how many random numbers to generate and generate that many
    print("\nUser Generated Random Numbers\n-------------------")
    user_start = int(input("Enter start value: "))
    user_stop = int(input("Enter stop value: "))
    number_of_randoms = int(input("How many random numbers do you want?: "))
    for i in range(number_of_randoms):
        print(f"Random number {i + 1}: {random.randint(user_start, user_stop)}")

    
main()