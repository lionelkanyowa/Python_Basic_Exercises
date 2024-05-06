# Q.5: Without running the following code, determine what it will print:

def multiples_of_three():
    divisor = 1

for dividend in range(3, 31, 3):
    print(f'{dividend} / {divisor} = 3')
    divisor += 1

multiples_of_three()

# The function will output an error. The variable in line 4 cannot be used within the function. The variable cannot be
# invoked within the function because the function has no access outside itself.

# ALso, on line 10, the function was not invoked.