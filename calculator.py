#Simple Calculator maybe if i will have free time, will try to make it more realistic with real calculator that would have more functionality
# And YES i understand that allot of code repeat it self, While loop inside of While loop is bad, 
# and that it will allways print out the meniu and its a minus because you dont see console and you need to scroll up to check your results.


# to add 
#Decimal Precision: 
# By allowing the user to specify the desired decimal precision, 
# you provide more flexibility in the calculator's output. 
# You can add an option for the user to input the desired precision (e.g., the number of decimal places) 
# and use Python's round() function to round the calculated results to the specified precision.
#Memory Functionality: 
# Adding memory functionality allows users to store and recall values during multiple calculations. 
# You can include options such as "M+" (add to memory), "M-" (subtract from memory), "MR" (recall from memory), or "MC" (clear memory). 
# This can be useful when performing calculations that depend on previous results, eliminating the need for the user to re-enter values.
#Refractor code:
#Refractor the code so it would be more easy to read it, and it would be closer looking as a real calculator with basic functionality.
#Adding UI and making it as a .exe fyle:
#Remake calculator so it would work from opening caculator.exe file and it would have an interface similar as a calculator with basic funcionality.

import math
import sys

exit_loop = False

#while not exit_loop:
while True:
    print("-")
    print("Hello, this is simple calculator \nPlease write either number or simbol that you see from the list below.")
    print("Dont forget it will repeat it self after completing one operation")
    print("1. +")
    print("2. -")
    print("3. /")
    print("4. *")
    print("5. //")
    print("6. **")
    print("7. %")
    print("8. sqrt - Square root")
    print("9. sin - Sine")
    print("10. cos - Cosine")
    print("11. tan - Tangent")
    print("0. Exit program")

    z = input("Operation that you want to excecute: ")
        
    if z == "1" or z == "+":
        try:
            x = float(input("First number: "))
            y = float(input("Second number: "))
        except (ValueError, NameError):
            print(f"ValueError: Your input is not a valid number")
            continue
        
        result = x + y
        print(f"Result after + operation: {x} + {y} = {result}")
        
        while True:
            print("If you want to repeat operation write 1 or word repeat or again.\nIf you want to exit write exit or number 2")
            excecute = input("Wirte operation that you would like to excecute from shown meniu above: ")
            
            if excecute == "1" or excecute.lower() == "repeat" or excecute.lower() == "again":
                
                try:
                    x = float(input("First number:" ))
                    y = float(input("Second number: "))
                except (ValueError, NameError):
                    print(f"ValueError: Your input is not a valid number")
                    continue
                
                result = x + y
                print(f"Result after + operation: {x} + {y} = {result}")
                
            elif excecute == "2" or excecute.lower() == "exit":
                print("Thanks for using the simple calculator, have a nice day")
                # exit_loop = True
                sys.exit()
                # break

    if z == "2" or z == "-":
        try:
            x = float(input("First number: "))
            y = float(input("Second number: "))
        except (ValueError,NameError):
            print(f"ValueError: Your input is not a valid number")
            continue
        
        result = x - y
        print(f"Result after - operation: {x} - {y} = {result}")

        while True:
            print("If you want to repeat operation write 1 or word repeat or again.\nIf you want to exit write exit or number 2")
            excecute = input("Wirte operation that you would like to excecute from shown meniu above: ")
            
            if excecute == "1" or excecute.lower() == "repeat" or excecute.lower() == "again":
                
                try:
                    x = float(input("First number:" ))
                    y = float(input("Second number: "))
                except (ValueError, NameError):
                    print(f"ValueError: Your input is not a valid number")
                    continue
                
                result = x - y
                print(f"Result after - operation: {x} - {y} = {result}")
                
            elif excecute == "2" or excecute.lower() == "exit":
                print("Thanks for using the simple calculator, have a nice day")
                # exit_loop = True
                sys.exit()
                # break


    if z == "3" or z== "/":
        while True:
            try:
                x = float(input("First number: "))
                y = float(input("Second number: "))
            except (ValueError,NameError,ZeroDivisionError):
                print(f"ValueError: Your input is not a valid number, or it can't be divided by zero")
                continue
            
            if x > 0 and y > 0:
                result = x / y
                print(f"Result after / operation: {x} / {y} = {result}")
                
                while True:
                    print("If you want to repeat operation write 1 or word repeat or again.\nIf you want to exit write exit or number 2")
                    excecute = input("Wirte operation that you would like to excecute from shown meniu above: ")
                    
                    if excecute == "1" or excecute.lower() == "repeat" or excecute.lower() == "again":
                        try:
                            x = float(input("First number: "))
                            y = float(input("Second number: "))
                        except (ValueError,NameError,ZeroDivisionError):
                            print(f"ValueError: Your input is not a valid number, or it can't be divided by zero")
                            continue
                        result = x / y
                        print(f"Result after / operation: {x} / {y} = {result}")
                    elif excecute == "2" or excecute.lower() == "exit":
                        print("Thanks for using the simple calculator, have a nice day")
                        # exit_loop = True
                        sys.exit()
                        # break
                        
            if x <= 0 or y <= 0:
                print("One of numbers that you wrote are 0 and it can't be divided by zero, please write number that is not a 0")
            try:
                x = float(input("First number: "))
                y = float(input("Second number: "))
            except (ValueError,NameError,ZeroDivisionError):
                print(f"ValueError: Your input is not a valid number, or it can't be divided by zero")
                continue
            result = x / y
            print(f"Result after / operation: {x} / {y} = {result}")
            
            while True:
                print("If you want to repeat operation write 1 or word repeat or again.\nIf you want to exit write exit or number 2")
                excecute = input("Wirte operation that you would like to excecute from shown meniu above: ")
                if excecute == "1" or excecute.lower() == "repeat" or excecute.lower() == "again":
                    try:
                        x = float(input("First number: "))
                        y = float(input("Second number: "))
                    except (ValueError,NameError,ZeroDivisionError):
                        print(f"ValueError: Your input is not a valid number, or it can't be divided by zero")
                        continue
                    result = x / y
                    print(f"Result after / operation: {x} / {y} = {result}")
                elif excecute == "2" or excecute.lower() == "exit":
                    print("Thanks for using the simple calculator, have a nice day")
                    # exit_loop = True
                    sys.exit()
                    # break

    if z == "4" or z == "*":
        try:
            x = float(input("First number: "))
            y = float(input("Second number: "))
        except (ValueError,NameError):
            print(f"ValueError: Your input is not a valid number")
            continue
        
        result = x * y
        print(f"Result after * operation: {x} * {y} = {result}")

    if z == "5" or z == "//":
        try:
            x = float(input("First number: "))
            y = float(input("Second number: "))
        except (ValueError,NameError):
            print(f"ValueError: Your input is not a valid number")
            continue
        
        result = x // y
        print(f"Result after // operation: {x} // {y} = {result}")
        
    if z == "6" or z == "**":
        try:
            x = float(input("First number: "))
            y = float(input("Second number: "))
        except (ValueError,NameError):
            print(f"ValueError: Your input is not a valid number")
            continue
        
        result = x ** y
        print(f"Result after ** operation: {x} ** {y} = {result}")
        
    if z == "7" or z == "%":
        try:
            x = float(input("First number: "))
            y = float(input("Second number: "))
        except (ValueError,NameError):
            print(f"ValueError: Your input is not a valid number")
            continue
        
        result = x % y
        print(f"Result after % operation: {x} % {y} = {result}")
        
    if z == "8" or z.lower() == "sqrt" or z.lower() == "square root" or z.lower() == "root" or z.lower() == "square":
        try:
            x = float(input("Your number: "))
        except (ValueError,NameError):
            print(f"ValueError: Your input is not a valid number")
            continue
        
        result = math.sqrt(x)
        print(f"Result after square root operation: Square Root: {x} = {result}")
        
    if z == "9" or z.lower() == "sin" or z.lower() == "sine":
        try:
            x = float(input("Your number: "))
        except (ValueError,NameError):
            print(f"ValueError: Your input is not a valid number")
            continue
        
        result = math.sin(x)
        print(f"Result after sine operation: sine: {x} = {result}")
    
    if z == "10" or z.lower() == "cos" or z.lower() == "cosine":
        try:
            x = float(input("Your number: "))
        except (ValueError,NameError):
            print(f"ValueError: Your input is not a valid number")
            continue
        
        result = math.cos(x)
        print(f"Result after cosine operation: cosine: {x} = {result}")
        
    if z == "11" or z.lower() == "tan" or z.lower() == "tangent":
        try:
            x = float(input("Your number: "))
        except (ValueError,NameError):
            print(f"ValueError: Your input is not a valid number")
            continue
        
        result = math.tan(x)
        print(f"Result after tangent operation: tangent: {x} = {result}")
        
    if z == "0" or z.lower() == "exit":
        print("Thanks for using the simple calculator, have a nice day")
        break