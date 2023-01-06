# Car sales program:
# Extend the Car sales program created in the previous chapter with the
# following functionality:

# After entering the brand, model and price of the first car, the user is
# required to answer they would like enter the same information of a second
# car. If the user’s reply is yes, ask the user those questions from the
# previous chapter again. If his reply is no, end the program

valid_input = False
while valid_input == False:
    try:
        add_car = str(input("Add a new car (yes / no):"))
        if add_car == "yes":
            input_b = str(input("Please Enter Car Brand:"))
            input_m = str(input("Please Enter Car Model:"))
            input_p = int(input("Please Enter Car Selling Price:"))
            print(f"You have entered is {input_b}, {input_m}, {input_p}")
        elif add_car == "no":
            valid_input = True
            print("Goodbye!")
            break
    except ValueError:
        print("Your input is of the wrong type. Please try again")
