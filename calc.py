operator = input("Enter the operator (+,-,* or /): ")
num1 = float(input("Enter 1st number: "))
num2 = float(input("Enter the 2nd number: ")) 

if operator == "+": 
    result = round(num1 + num2, 2) 
    print (f"The result of {num1} {operator} {num2} = {result}") 
elif operator == "-": 
    result = round(num1 - num2, 2) 
    print (f"The result of {num1} {operator} {num2} = {result}") 
elif operator == "*": 
    result = round(num1 * num2, 2) 
    print (f"The result of {num1} {operator} {num2} = {result}") 
elif operator == "/": 
    result = round(num1 / num2, 2) 
    print (f"The result of {num1} {operator} {num2} = {result}") 
else:
    print ("Invalid input")




