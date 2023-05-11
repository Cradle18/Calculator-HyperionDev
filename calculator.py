"""
This is a basic calculator programme that uses try-exception blocks, to calculte the input from a user and return
the calculation printed to a text file.
"""

print("Welcome to the Cal100")
print("Please input two numbers you wish to be calculated and the operator you wish to use.")

file1 = open("input.txt", "a")#Open a file in append mode, so we can continue to add new input to the end of the file.


while True: #Checking for valid int input
    try:
        int1 = int(input("Please enter a number: "))
        int2 = int(input("Please enter the second number: "))
        break
    except ValueError:
        print("Invalid input, try again!")


#Checks operator is valid and calculates sum.
while True: 
    try:
        operator = input("Please enter the operator you wish to use: ")
        if operator in ("+", "-", "*", "/"):
            if operator == "+":
                total = int1 + int2
                print(f"{int1} {operator} {int2} = {total}\n")
            elif operator == "-":
                total = int1 - int2
                print(f"{int1} {operator} {int2} = {total}\n")
            elif operator == "*":
                total = int1 * int2
                print(f"{int1} {operator} {int2} = {total}\n")
            elif operator == "/":
                if int2 == 0:
                    raise ZeroDivisionError("Cannot divide by zero!")
                total = int1 / int2
                print(f"{int1} {operator} {int2} = {total}\n")
            break
        else:
            print("Invalid operator")
    except (TypeError, ZeroDivisionError) as e:
        print(f"Invalid input: {e}. Please use a different operator!")

file1.write(f"{int1} {operator} {int2} = {total} \n") #write the full sum with answer to file.
file1.close()

read_file = input("Do you wish for a file to be read? Enter file name:\n") #Allows use to enter a file or there choice to be read.

if read_file.endswith(".txt"):#Check if the file is the correct format of .txt
#Read over the file and prints the result.
    try: 
        file1 = open(read_file, "r")
        print("Reading file....")
        print(file1.read())
        file1.close()
    except FileNotFoundError:
        print("Error file not found!")

print("Thank you for using Cal100")


    
    




    








