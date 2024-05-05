# Q.6: Take your code from the previous Check the Weather exercise and rewrite it as a match-case statement.
# Feel free to add more cases besides 'sunny' and 'rainy'.

# weather = 'snowy'

# if weather == 'sunny':
   # print("It's a beautiful day.")
# elif weather == "rainy:":
   # print("Grab your umbrella.")
# else:
    # print("Let' stay inside.")

weather = 'sunny'

match weather:
    case 'sunny':
        print("It's a beautiful day.")
    case 'rainy':
        print("Grab your umbrella.")
    case _: # default case
        print("Let's stay inside.")

