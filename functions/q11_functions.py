# Q.11: Building on your solutions from the previous exercises, write a function local_greet that takes a locale as
# input, and returns a greeting. The locale lets us greet people from different countries appropriately, even when
# they share a common language, for example:

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


def extract_language(locale):
    return locale[:2]


def extract_region(locale):
    return locale[3:5]


def local_greet(locale):
    language = extract_language(locale)
    region = extract_region(locale)

    match (language, region):
        case ('en', 'US'):
            return 'Hey!'
        case ('en', 'GB'):
            return 'Hello!'
        case ('fr', 'FR'):
            return 'Salut!'
        case _:
            return greet(language)

print(local_greet('en_US.UTF-8'))       # Hey!
print(local_greet('en_GB.UTF-8'))       # Hello!
print(local_greet('fr_FR.UTF-8'))       # Salut!!
