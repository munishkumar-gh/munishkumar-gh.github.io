# Car sales program:
# Create a program in which the user is asked to enter the brand, model and
# selling price of a car. Print the information in one print() command
# subsequently using formatting printing.

input_brand = str(input("Please Enter Car Brand:"))
input_model = str(input("Please Enter Car Model:"))
input_price = int(input("Please Enter Car Selling Price:"))

print("--------------------")
print("Welcome to the program to print your car parameters")
print(f"The car Brand you have entered is {input_brand}")
print(f"The car Model you have entered is {input_model}")
print(f"The car Price you have entered is {input_price}")

print("--------------------")
print("Here it is combined:")
print(
f"The car you have entered is {input_brand}, {input_model}, {input_price}"
)

# Impact of double quatation Marks
#print(f""What does this print?"")
print("\"What does this print?\"")
print("What does this print?")
