import random
#create function to get the difficulty level
def get_difficulty():
    while True:
        try:
            user_difficulty = int(input("Enter difficulty (1, 2, 3): "))
            if user_difficulty in range(1, 4):
                break
            else:
                continue
        except:
            continue
    return user_difficulty

#create a function to ask how many questions the user wants to be asked
def get_number_question():
    while True:
        try:
            user_number_questions = int(input("Enter number of questions to ask (3 - 10): "))
            if user_number_questions in range(3, 11):
                break
            else:
                continue
        except:
            continue
    return user_number_questions

