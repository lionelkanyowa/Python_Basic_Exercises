# Q.9: What will the following code do and why? Don't run it until you have tried to answer.

a = 7

def my_function(b):
    b += 10

my_function(a)
print(a)

# The output will be 7. Since the function call in line 8 is calling the variable 'a', the function will point to the
# global variable in line 3.

# During the execution of the += operation inside the my_function function, b += 10 effectively becomes b = b + 10.
# This operation creates a new integer object 17 and updates b to reference this new object. However, the original
# variable a remains unaffected and retains its value of 7.