# Andrew Sweeney
# G00237144
# February 2016

import preproc


def checkvalidconundrum(wordin, debug):

    # Used the check if the 9 letter word is valid
    # Pass in a 9 letter word
    # Is uppercase
    # That contains no numbers
    # Contains at least 3 vowels and 4 consonants

    if debug is True:
        print("\nDebug: checkvalidconundrum\n")

    wordin = wordin.upper()

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

    return True


def dropwords(conun, wordlist):

    cleanwordlist = set()
    letters = set(conun)

    for word in wordlist:
        if len(list(set(word) - set(letters))) is 0:
            cleanwordlist.add(word)

    return cleanwordlist

# Main Program

# Variables

debug_mode = True

dictionary = set()
permutations = set()

print("--------------")
print("Running solver.py")
print("--------------")

dictionary = preproc.import_dictionaryfile("wordfile.txt", debug_mode)

# Prompting the user for a valid conundrum e.g the word conundrum is valid

conundrum = input("Please enter a valid conundrum? ")

while checkvalidconundrum(conundrum, debug_mode) is False:
    print("\nThe conundrum didn't meet the criteria, try again")
    conundrum = input("Please enter a valid conundrum? ")

conundrum = conundrum.upper()

print("Valid Conundrum: ", conundrum)

permutations = preproc.get_permuations(conundrum)

print()

print(len(dictionary))

dictionary = dropwords(conundrum, dictionary)

print(len(dictionary))

# Preprocessing building all permutations of the anagram, Importing the textfile
