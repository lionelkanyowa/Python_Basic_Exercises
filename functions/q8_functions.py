# Q.8: Use Python's control structures to create a function that takes an ISO 639-1 language code and returns
# a greeting in that language. You can take the examples below or add whatever languages you like.

def greet(code):
    match code:
        case 'en':
            return 'Hi!'
        case 'fr':
            return 'Salut!'
        case 'pt':
            return 'Ola!'
        case 'de':
            return 'Hallo!'
        case 'sv':
            return 'Heji!'
        case 'af':
            return 'Haai'


print(greet('en'))
print(greet('fr'))
print(greet('pt'))
print(greet('de'))
print(greet('sv'))
print(greet('af'))
