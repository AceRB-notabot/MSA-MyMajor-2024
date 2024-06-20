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

#generate a number of random questions equal to the number the user asked for
#use a list to store the values to be used in the equations
#have three section in mainn for the three different levels
#if the user gets an equation right add one to the amount of questions answered correctly
#if the user answered wrong repeat the question to a max of three repeats
#declare variables to represent strikes, # of correct answers, the answer to each question, and the problem number
def main():
    difficulty = get_difficulty()
    strikes = 0
    correct_answers = 0
    problem_number = 0
    value_1 = 0
    value_2 = 1
    if difficulty == 1:
        rand_list = []
        n = int(get_number_question())
        for i in range(n*2):
            rand_list.append(random.randint(0, 9))
    elif difficulty == 2:
        rand_list = []
        n = int(get_number_question())
        for i in range(n*2):
            rand_list.append(random.randint(10, 99))
    elif difficulty == 3:
        rand_list = []
        n = int(get_number_question())
        for i in range(n*2):
            rand_list.append(random.randint(100, 999))
    while True:
        try:
            if problem_number < n:
                answer = rand_list[value_1] + rand_list[value_2]
                user_answer = int(input(f"What is the answer to {rand_list[value_1]} + {rand_list[value_2]}: "))
                if user_answer == answer:
                    print("CORRECT!")
                    problem_number += 1
                    correct_answers += 1
                    value_1 += 2
                    value_2 += 2
                else:
                    print("WRONG!")
                    strikes += 1
                    if strikes == 3:
                        print(f"The answer was {answer}")
                        strikes = 0
                        problem_number += 1
                        value_1 += 2
                        value_2 += 2
            else:
                break
                
        except:
            print("WRONG!")
            strikes += 1
            continue
    final_score = correct_answers / n
    print(f"You answered {n} questions and got {correct_answers} right.\nThat is a final score of {final_score * 100:.2f}%")

main()