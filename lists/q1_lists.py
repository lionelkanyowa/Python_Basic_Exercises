# Q.1: Write a function that returns the first element of a list provided as an argument.

# Be sure to handle the case where the input list is empty.
def first(lst):
    if lst:
        return lst[0]
    else:
        return 'No first element in list to return'


print(first(['Earth', 'Moon', 'Mars']))
print(first([]))
