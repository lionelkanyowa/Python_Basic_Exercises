# Q.10: Determine what the following code snippet prints. First solve it in your head or on paper, then run it in
# your Python environment to check the result.

speed = 0
acceleration = 24
breaking_force = 19
is_moving = breaking_force < acceleration and (speed > 0 or acceleration > 0)
# This would return a False
print(is_moving)

# Bonus question: Do we need the parentheses in the boolean expression or could we have written the following?:

# is_moving = braking_force < acceleration and speed > 0 or acceleration > 0

# Yes, we need the parentheses. Since and has a higher operator precedence than or, so:

# removing the parentheses will still print True. However, we still need the parentheses for different values
# for speed, acceleration, and braking_force.