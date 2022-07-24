# Python program for simple calculator
 
# Function to add two numbers
def add(num1, num2, num3, num4):
    return num1 + num2 + num3 + num4
 

# Function to multiply two numbers
def multiply(num1, num2,num3,num4):
    return num1 * num2 * num3 * num4
 

 
print("Please select operation -\n" \
        "1. Add\n" \
        "2. Multiply\n" )
        
 
 
# Take input from the user
select = int(input("Select operations form 1, 2, 3, 4 :"))
 
number_1 = int(input("Enter first number: "))
number_2 = int(input("Enter second number: "))
number_3 = int(input("Enter third number: "))
number_4 = int(input("Enter fourth number: "))
 
if select == 1:
    print(number_1, "+", number_2,  "+" ,number_3,"+",number_4,"=",
                    add(number_1, number_2,number_3,number_4))
 

elif select == 2:
    print(number_1, "*", number_2, "*",number_3 ,"*",number_4,"=",
                    multiply(number_1, number_2,number_3,number_4))
 

else:
    print("Invalid input")

 #output   PS C:\Users\91770\Desktop\anusha python\012_Anusha_Santhoshi_Contributions> python SimpleCalculator.py
#Please select operation -
#1. Add
#2. Multiply

#Select operations form 1, 2, 3, 4 :1
#Enter first number: 2
#Enter second number: 4
#Enter third number: 6
#Enter fourth number: 8
#2 + 4 + 6 + 8 = 20

#PS C:\Users\91770\Desktop\anusha python\012_Anusha_Santhoshi_Contributions> python Simplecalculator.py
#Please select operation -
#1. Add
#2. Multiply

#Select operations form 1, 2, 3, 4 :2
#Enter first number: 2
#Enter second number: 4
#Enter third number: 6
#Enter fourth number: 8
#2 * 4 * 6 * 8 = 384
