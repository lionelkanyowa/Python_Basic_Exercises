# Q.11: We have a grocery list. As we check off items on that list, we want to remove them from the list.
#
# Write code that removes the items from grocery_list, one by one, until it is empty. If you print the elements
# you remove, the expected behavior would look as follows.

grocery_list = ['paprika', 'tofu', 'garlic', 'quinoa',
                'carrots', 'broccoli', 'hummus']

while grocery_list:
    removed_item = grocery_list.pop()
    print('Removed item:', removed_item)
    print('Updated list:', grocery_list)
