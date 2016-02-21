# Andrew Sweeney
# G00237144
# February 2016

# Test Functions


def test_checkvalidconundrum():
    print('\ntest_checkvalidconundrum\n')
    print(checkvalidconundrum('AAAAAAAAAA'))
    print(checkvalidconundrum('BBBBBBBBBB'))
    print(checkvalidconundrum('123456789'))
    print(checkvalidconundrum('testing'))
    print(checkvalidconundrum('conundrum'))
    print(checkvalidconundrum('AAABBBBBB'))
    print(checkvalidconundrum('CONUNDRUM'))


def checkvalidconundrum(wordin):

    # Used the check if the 9 letter word is valid
    # Pass in a 9 letter word
    # Is uppercase
    # That contains no numbers
    # Contains at least 3 vowels and 4 consonants

    vowels = list("AEIOU")
    consonants = list("BCDFGHJKLMNPQRSTVWXYZ")

    # Used this source for counting consonants and vowels
    # http://stackoverflow.com/questions/7736211/python-counting-the-amount-of-vowels-or-consonants-in-a-user-input-word

    number_of_consonants = sum(wordin.count(c) for c in consonants)
    number_of_vowels = sum(wordin.count(c) for c in vowels)

    wordin = wordin.strip()

    if len(wordin) != 9:
        return False
    if number_of_consonants < 4:
        return False
    if number_of_vowels < 3:
        return False
    if wordin.isalpha() is False:
        return False
    if wordin.isupper() is False:
        return False

    return True

# Main Program

test_checkvalidconundrum()