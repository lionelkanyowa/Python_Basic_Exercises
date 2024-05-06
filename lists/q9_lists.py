# Q.9: The destinations list contains a list of travel destinations.

destinations = ['Prague', 'London', 'Sydney', 'Belfast',
                'Rome', 'Aruba', 'Paris', 'Bora Bora',
                'Barcelona', 'Rio de Janeiro', 'Marrakesh',
                'new York City']

# Write a function that, without using the built-in in operator, checks whether a specific destination is included
# within destinations. For example: When checking whether 'Barcelona' is contained in destinations, the expected
# output is True, whereas the expected output for 'Nashville' is False.

def contains(city, destination):
    for place in destination:
        if place == city:
            return True

    return False



print(contains('Barcelona', destinations))
print(contains('Nashville', destinations))