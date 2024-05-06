# Q.6: What will the following code do and why? Don't run it until you have tried to answer.

a = 1


def my_function():
    a = 2


my_function()
print(a)

# The final output would be 1. In line 6 we have a local variable that is evoked when the method is called in line 10
# However, my_function() in line 10 would return None since there wasn't a print statement for the local variable.
# The print statement in line 11 is accessing the variable in line 3; therefore, 1 will be the final output.
