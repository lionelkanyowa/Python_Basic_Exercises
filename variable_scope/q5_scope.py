# Q.5: What will the following code do and why? Don't run it until you have tried to answer.

a = 1


def my_function():
    print(a)
    a = 2


my_function()

# This would print out an error. Although we have a global variable in line 3 that can be accessed within the method,
# In line 8 within the method, 'a' is being initialized to 2. The reason why this would produce an error is because 'a'
# was invoked with the print(a) statement before it was initialized in line 7.
