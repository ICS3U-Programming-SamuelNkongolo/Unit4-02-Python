#!/usr/bin/env python3
# Created by: Samuel Nkongolo
# Created on: Nov 6
# This program calculates factorials.


def main():
    # This section explains the programs's function and defining variables.
    print("This program calculates the factorial of any whole number entered.")
    user_num = input("Enter a whole number: ")
    loop_count = 0
    fact_prod = 1
    try:
        user_num_int = int(user_num)
        user_num_float = float(user_num)
        while True:
            # This section finds the factorial
            loop_count += 1
            fact_prod *= loop_count
            print("Number tracked {} times through loop...".format(loop_count))
            # This section deals with negative numbers.
            if user_num_int < 0:
                print(f"{user_num_int} is not a whole number.\n")
                break
            if loop_count >= user_num_int:
                # This section deals with telling the user the results.
                print("{}! = {}".format(user_num_int, fact_prod))
                break
            # This section deals with 0!.
            if user_num_int == 0:
                print("0! is always equal to 1.\n")
                break
            # This section deals with decimals.
            if user_num_float != user_num_int:
                print(f"{user_num_float} is not a whole number.\n")
                break
    except:
        print(f"{user_num} is not a whole number.")


# Running the program.
if __name__ == "__main__":
    main()
