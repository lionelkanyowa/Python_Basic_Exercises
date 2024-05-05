# Q.9: Without running the following code, determine what will be printed.

sale = True
admission_price = 5.25 if not sale else 3.99

print(f"${admission_price}")

# This would print 3.99. Since sale is true then not sale is false.