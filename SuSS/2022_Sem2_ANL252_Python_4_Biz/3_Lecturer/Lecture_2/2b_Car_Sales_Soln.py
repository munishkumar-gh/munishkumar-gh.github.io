# Car sales program:
# Extend the Car sales program by storing all the car brand,
# model and price of each entry in a list within the “outer”
# list in which all the entries of the user inputs are stored.

finallist = []
i = 1
proceed = True

print("\nPlease enter following data (ENTER to quit):")

while proceed == True:
    std_brand = str(input(f"\n Brand of Car {i}: "))
    if std_brand == "":
        proceed = False
        break
    std_model = str(input(f"\n Model of Car {i}: "))
    if std_model == "":
        proceed = False
        break

# There is a bug in this code - can you fix it?
    valid_in2 = False
    while valid_in2 == False:
        std_price = input(f"\n Price of Car {i}: ")
        if std_price == "":
            proceed = False
            break
        try:
            std_price = float(std_price)
        except ValueError:
            print("Non-Numeric input - try again")
        else:
            valid_in2 = True

        if proceed == True:
            templist = [std_brand, std_model, std_price]
            finallist = finallist + [templist]
            i = i+1

if i > 1:
    print(f"\nThe following data has been entered:\n{finallist}\n")
