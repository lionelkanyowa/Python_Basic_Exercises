# The following code raises a SyntaxError:

speed_limit = 60
current_speed = 80

# if current speed > speed_limit
    # print('"People are so bad at driving cars that '
          # "computers don\'t have to be that good to be "
          # 'much better." -- Marc Andreessen')

# What does a SyntaxError indicate? Try running the above code, then use the resulting error message to fix the error.

# SyntaxError indicates that there is something wrong with the code's syntax is resulting in an error when the code
# is ran. When we look closely at the if statement, we see that the colon was missed in line 6.

if current_speed > speed_limit:
    print('"People are so bad at driving cars that '
    "computers don\'t have to be that good to be "
     'much better." -- Marc Andreessen')