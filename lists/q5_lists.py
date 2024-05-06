# Q.5: Count the number of elements in scores that are 100 or above.

scores = [96, 47, 113, 89, 100, 102]

i = 0
for numbers in scores:
    if numbers >= 100:
        i += 1
print(i)