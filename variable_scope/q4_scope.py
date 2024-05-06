# Q.4: What will the following code do and why? Don't run it until you have tried to answer.

a = 1


def my_function():
    print(a)


my_function()

# On line 8, the function is called my guess is since 'a' is initialized outside the method scope on line 3, this
# makes it globally accessible throughout the code, including within the function's body(my_function).
# the final output would be 1.
