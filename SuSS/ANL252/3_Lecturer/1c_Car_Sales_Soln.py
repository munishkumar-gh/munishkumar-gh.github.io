# Car sales program:
# Extend the Car sales program created in the previous chapter with the
# following functionality:

# After entering the brand, model and price of the first car, the user is
# required to answer they would like enter the same information of a second
# car. If the user’s reply is yes, ask the user those questions from the
# previous chapter again. If his reply is no, end the program

input_brand = str(input("Please Enter Car Brand:"))
input_model = str(input("Please Enter Car Model:"))
input_price = int(input("Please Enter Car Selling Price:"))

print(
f"The car you have entered is {input_brand}, {input_model}, {input_price}"
)

terminate_qns = str(input("Do you want to go again (Y/N):"))

if terminate_qns == "Y":
    input_brand = str(input("Please Enter Car Brand:"))
    input_model = str(input("Please Enter Car Model:"))
    input_price = int(input("Please Enter Car Selling Price:"))

    print(
    f"The car you have entered is {input_brand}, {input_model}, {input_price}"
    )

elif terminate_qns == "N":
    print(f"Goodbye")
else:
    print(f"Your input is incorrect")
