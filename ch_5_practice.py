"""
    Complete all of the TODO directions
    The number next to the TODO represents the chapter
    and section that explain the required code
    Your file should compile error free
    Submit your completed file
"""

# TODO 5.2 - calling an existing function
# beneath the following function, write the code to call it, remove the """ """ before testing

"""
def hello():
    print("Hello Sweetie!")
"""

# write the code to call the hello function on the next line

# TODO 5.2 - creating and calling a function
# Write a function called joke that prints a joke on the screen

def message():
print('why did the chicken cross the road,')
print('to get to the other side.')

# Call the message function.
message()

# TODO 5.3 designing a program in functions
# create a main function that will call separate functions that
# print each line in a knock knock joke. Make sure to call main
# as the last line of your code.

def main():
    Line1()
    Line2()
    Line3()
    Line4()
    Line5()
def Line1():
    print("knock knock")
def Line2():
    print("who's there?")
def Line3():
    print("updog")
def Line4():
    print("whats updog?")
def Line5():
    print("nothing what about you?")



# TODO 5.4 local variables
# Write a program with a main2 function that defines a variable called
# name in the main function, and assign a name to it. Print hello
# and the name variable. Call a second function get_name. In the
# get_name function, ask the user for their name, then greet them
# using a print statement. Be sure to call the main2 function.
# note - you would not normally have more than one main function
# in a program, we are just adding the number after main to allow
# us to write multiple short practice programs in this file.
def main2():
    name , "doctor"
    print("hello" + name)
    get_name()

def get_name():
    user_name , "mitch"
    print("hello" + user_name)

main2()
    # TODO 5.5 passing arguments to Functions
# complete the code below to pass the my_number variable from
# main 3 into square with the parameter name of value remove the """ """ before testing

"""
def main3():
    my_number = 7
    square()
    
    
def square():
    squared_value = value * value
    print(squared_value)
    
    
main3()

"""

# TODO 5.5 passing multiple arguments
# complete the code below to pass the variables from main into
# parameters for add. Look at the code to determine the correct
# variable / parameter names. Remove the """ """
"""
def main4():
    num_one = 5
    num_two = 7
    add(num_one, num_two)
    
    
def add():
    total = one + two
    print(total)


main4()
"""


# TODO 5.7 value returning functions
# Add a statement importing the random library
# Add the global constant PI with a value of 3.14 before the main5 function

"""
def main5():
    r = # TODO generate a random integer between 1-10, assign it to the variable r
    r2 = r * r
    area(r2)
    
    
def area(radius_squared):
    my_area =  # TODO insert the PI constant multiplied by the parameter here
    print(format(my_area, ",.2f"))
    
    
main5()
"""

# TODO 5.8 value returning functions
# Complete the following program, remove the """  """ before testing
"""
def main6():
    print("This program will calculate your BMI")
    height = float(input("What is your height in inches?  "))
    weight = float(input("What is your weight in pounds"))
    # TODO call the bmi function and assign the result to a variable named answer
    
    # TODO print the variable answer, make sure to format it to 1 decimal place
    
    # TODO modify the bmi function to accept the height and weight
    # read the code to determine the parameter names
def bmi():
    # BMI = (Weight in Pounds / (Height in inches x Height in inches)) x 703
    patient_bmi =  (weight_pounds / (height_inches * height_inches)) * 703
    # TODO send the patient_bmi value back to main6
    

main6()

"""
# TODO 5.9 the math module
# import math
# write a statement that uses the ceil function on the following variable

number_to_round = 4.243
