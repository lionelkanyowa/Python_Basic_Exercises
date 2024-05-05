animal = 'horse'

match animal:
    case 'duck':
        print('quack')
    case 'squirrel':
        print('nook nook')
    case 'horse':
        print('neigh')
    case 'bird':
        print('tweet tweet')
    case _:
        print('*cricket*')

# The code above will print 'neigh'. Since the the variable's value was initialized as 'horse', Python will look at
# that value as a truthy value, and if that value is the only one that will return a truthy value in the case
# statement.