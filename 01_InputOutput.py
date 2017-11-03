# Single line comment
'''
multi line comment
'''
# Ask for name
name = input('What is your name ')
# Print the Greetings
print ('Welcome ',name)

# Ask the user to enter 2 values and store the values as num1 and num2
#num1 = input('Enter the first number ')
#num2 = input('Enter the second number ')
# better way is
num1,num2 = input('Enter 2 numbers ').split()

# Convert the strings that user enters into regular numbers Integers
num1 = int(num1)
num2 = int(num2)

# Add the values and store the result to sum
sum = num1+num2
# Subtract the values and store the result in diff
diff = num1-num2
# Multiply the values and store the result in product
prod = num1 * num2
# Divide the values and store the result in quotient
quotient = num1/num2
# Use modulus operator to find teh remainder
remainder = num1%num2
# print the results
print ("{} + {} = {}".format(num1,num2,sum))
print ("{} - {} = {}".format(num1,num2,diff))
print ("{} * {} = {}".format(num1,num2,prod))
print ("{} / {} = {}".format(num1,num2,quotient))
print ("{} % {} = {}".format(num1,num2,remainder))