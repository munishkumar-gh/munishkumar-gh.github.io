# Car sales program:
# Construct a tuple of the car brands you know (e.g., Toyota, Kia, BMW,
# Chrysler, Mercedes Benz, Porsche, Fiat, etc.).

# Extend the Car sales program from Study Unit 1 by listing the car brands
# stored in the tuples and listed them out on the screen when the user is asked
# to enter the brand of the car.

# Note that the user must enter one of the brands in the tuple, i.e.,
# any brand not stored in the tuple is considered as invalid input.
# Furthermore, the exact spelling of the brand in the tuple should also be
# stored in the variable for the car brand input.

# Recall - Tuples are defined by round brackets "(" & ")"
car_brands = (
"Toyota", "Kia", "BMW", "Chrysler", "Mercedes Benz", "Porsche", "Fiat",
"Honda", "Nissan", "Volswagon", "Renault", "Lambo", "Hyundai"
)

lenlist = len(car_brands)
for i in range(lenlist):
    print(f"The car brand is {car_brands[i]}")

User_qn = str(input("Which car brand do you want?:"))

count_car = 0
for j in range(lenlist):
    if car_brands[j] == User_qn:
        count_car = j
        break

# This part of the code is buggy - can you fix it?
if count_car > 0:
    print(f"You have entered a valid car brand {car_brands[count_car]}")
else:
    print("You have entered an invalid car brand")
