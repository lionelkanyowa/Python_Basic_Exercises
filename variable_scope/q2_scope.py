# Q.2: WHat will the following code do and why? Don't run it until you have tried to answer.

x = 10


def my_function():
    x = x + 5
    print(x)


my_function()

# This will output an error. The x initialized in line 3 is a different x being initialized in line 7.
# Within the function, we are trying to re-initialize x, but x has no original value to begin with, it is an
# unresolved reference.
