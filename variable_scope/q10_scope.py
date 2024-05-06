# Q.10: What will the following code do and why? Don't run it until you have tried to answer.

b = [1, 2, 3]

def my_function():
    b[0] = 10

my_function()
print(b)

# The final output would be [10, 2, 3].

# The function call in ine 8 accesses the global variable in line 3 and mutate it to become [10, 2, 3].
# The final output online 9 would be muted value.
