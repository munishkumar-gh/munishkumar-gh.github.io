#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Car sales program:
#Modify the Car sales program in a way that the trailing and leading
#white spaces in the inputs of the car brand and model
#should be removed by some built-in Python functions.
#Furthermore, the first letter of the brand should be stored in
#capital letters (only the first letter of the entire input,
#not the first letter of each word in the input) while all the subsequent
#letters should be kept in the format as entered by the user.
# Find and fix the bug if you can

# Find and fix the bug if you can
finallist = {}
i = 1
proceed = True
print("\nPlease enter following data (ENTER to quit):")
while proceed == True:
    std_brand = str(input(f"\n Brand of Car {i}: "))
    if std_brand == "":
        proceed = False
        break
    std_brand = std_brand.lstrip(" ").rstrip(" ") # Remove leading and trailing spaces
    s = list(std_brand) # A string is just a list of characters
    s[0] = s[0].upper()  # Only focus on the first letter
    std_brand_new = ''.join(s) # combine to characters to form a string again
    std_model = str(input(f"\n Model of Car {i}: "))
    if std_model == "":
        proceed = False
        break
    std_model = std_model.rstrip(" ").rstrip(" ") # Remove leading and trailing spaces
    bol_startOfLoop = True 
    while bol_startOfLoop  == True:
        std_price = input(f"\n Price of Car {i}: ")
        
        if std_price == "":
            proceed = False
            break
        try:
            std_price = float(std_price)
            
            #prompt user to re-input a valid input if he/she input a negative value or 0
            while std_price <=0:
                print("Please re-input the price as you have entered a negative value or 0.")
                std_price = float(input(f"\n Price of Car {i}: "))
                
            # Nested Dict
            if proceed == True:
                templist = {std_brand_new: {std_model: std_price}}
                finallist = {**finallist, **templist} #merge 2 dict
                i = i+1
        except ValueError:
            print("Non-Numeric input - try again")
        else:
            bol_startOfLoop = False
if i > 1:
    print(f"\nThe following data has been entered:\n{finallist}\n")


# In[ ]:




