#promt the user for a math expression
#ignore it if it isn't number space operator space number
#do the math
def main():
    while True:
        answer = 0
        user_input = 0
        try:
            user_input = input("Enter an arithmatic expression (Ex. 1 + 2) or type end to end: ")
            if user_input.lower() == "end":
                break
            expression = user_input.split(" ")
            term_1 = float(expression[0])
            operator = expression[1]
            term_2 = float(expression[2])
            if operator == "+":
                answer = term_1 + term_2
                print(f"{answer:.2f}")
            elif operator == "-":
                answer = term_1 - term_2
                print(f"{answer:.2f}")
            elif operator == "*":
                answer = term_1 * term_2
                print(f"{answer:.2f}")
            elif operator == "/":
                answer = term_1 / term_2
                print(f"{answer:.1f}")
            else:
                print("ERROR: Enter a simple operator ( + - * / )")
        except:
            continue

main()