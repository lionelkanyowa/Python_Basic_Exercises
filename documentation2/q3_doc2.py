# Q.3: Find the Python Documentation on operator precedence, and use it to determine the result of
# evaluating 4 * 5 + 3**2 / 10.

sum = (4 * 5) + (3**2 / 10)
print(sum)

# According to the Operator precedence, chapter 6.17, exponentiation takes precedence, followed by multiplication and
# division concurrently, followed by addition.

# ** > (* and /) > +
 # Exp   3**2 = 9
 # Multi 4 * 5
 # Div   9 / 10
 # Add  20 + 0.9 = 20.9




