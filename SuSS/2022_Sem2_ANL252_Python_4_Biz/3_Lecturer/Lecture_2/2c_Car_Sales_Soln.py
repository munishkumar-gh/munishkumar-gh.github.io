# Car sales program:
# Modify the Car sales program in a way that the car brands are
# stored as the keys of a dictionary. The value of the corresponding
# dictionary key is a sub-dictionary in which the model is used
# as key and the price is stored as value.

# Note that we should only have one key for each brand
# in the dictionary. That means, if the user enters multiple cars
# for the same brand, the value of that key should be a
# sub-dictionary which contains multiple keys. And the value
# for each of the key in the sub-dictionary is the price of one
# model.


finallist = {}
i = 1
proceed = True

print(f"\nPlease enter following data (ENTER to quit):")

while proceed == True:
    std_brand = str(input(f"\n Brand of Car {i}: "))
    if std_brand == "":
        proceed = False
        break
    std_model = str(input(f"\n Model of Car {i}: "))
    if std_model == "":
        proceed = False
        break

# This code is buggy, can you fix it?
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

        # Nested Dict
        if proceed == True:
            templist = {std_brand: {std_model: std_price}}
            finallist = {**finallist, **templist} #merge 2 dict

            i = i+1

if i > 1:
    print(f"\nThe following data has been entered:\n{finallist}\n")
