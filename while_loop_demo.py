def main():
    #create a while loop that prints integers between 1 and 10
    output_value=0
    stop_value=10
    #run the loop while the output is less then or equal to stop value
    while output_value<=stop_value:
        print(output_value)
        #increment output value
        #(output_value=output_value+1) the long way to increment
        output_value+=1
    print("\n\n")
    output_value=0
    while True:
        print(output_value)
        output_value+=1
        #if output value is greater than stop value break the loop
        if output_value>stop_value:
            break
main()