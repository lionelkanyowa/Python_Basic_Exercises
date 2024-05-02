# Q.4: Is there a method to reverse a string, for example turning 'hello' into 'olleh'?

my_str = 'hello'

# There is no built-in method in the str type specifically for reversing a string.

# You can use slicing.

reversed_str = my_str[::-1]
print(reversed_str)