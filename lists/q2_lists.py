# Q.2: Write a function that returns the last element of a list provided as an argument. For example:

# Be sure to handle the case where the input list is empty.
def last(lst):
    return 'No last element in the list to return' if not lst else lst.pop()


print(last(['Earth', 'Moon', 'Mars']))  # Mars
print(last([]))                         # No last element in the list to return
