#promt the user for a math expression
#ignore it if it isn't number space operator space number
#do the math
def main():
    user_input = input("Enter an arithmatic expression (Ex. 1 + 2): ")
    expression = user_input.split(" ")
    
main()