# Q.6: Write a function that checks whether a string is empty or not.

def is_empty(string):
    return string == ''
    #if string == '':
        #return True
    #else:
        #return False

print(is_empty('mars')) # False
print(is_empty(' '))    # False
print(is_empty(''))     # True

