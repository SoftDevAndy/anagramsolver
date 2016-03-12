# Andrew Sweeney
# G00237144
# February 2016

import preproc
import random
import collections
import time


def recursive(permuset, prefix, word):
    i = 0
    if len(word) <= 1:
        permuset.add(prefix + word)
    else:
        while i < len(word):

            x = i + 1

            current = word[i:x]
            before = word[0:i]
            after = word[x:]
            recursive(permuset, prefix + current, before + after)
            i += 1


def get_permuations(given_word):
    permus = set()

    print("\nPreprocessing")

    recursive(permus, "", given_word)

    print("All Permutations generated: ", len(permus))

    return permus


def checkvalidconundrum(wordin):

    # Used the check if the 9 letter word is valid
    # Pass in a 9 letter word
    # Is uppercase
    # That contains no numbers
    # Contains at least 3 vowels and 4 consonants

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


def dropwords(anagram, wordlist):

    # Checks if a word contains the same letters as the anagram keep it
    # If it contains a letter that doesn't exist in the anagram, drop the word
    # Example would be MUG - CONUNDRUM as sets is..
    # MUG - CONDRUM
    # G is left over because CONUNDRUM doesn't contain that letter
    # Drop the word because you can't make an anagram with it

    cleanwordlist = set()
    letters = set(anagram)

    for word in wordlist:
        if len(list(set(word) - set(letters))) is 0:
            cleanwordlist.add(word)
    return cleanwordlist


def user_input():
    print("--------------")
    print("Running solver.py")
    print("--------------")

    anagram = input("Please enter a valid conundrum? ")

    while checkvalidconundrum(anagram) is False:
        print("\nThe conundrum didn't meet the criteria, try again")
        anagram = input("Please enter a valid conundrum? ")

    anagram = anagram.upper()

    print("Valid Anagram: ", anagram)

    return anagram


def random_input():
    print("--------------")
    print("Running solver.py")
    print("--------------")

    vowels = list("AEIOU")
    consonants = list("BCDFGHJKLMNPQRSTVWXYZ")

    word = ""

    word += (random.choice(vowels))
    word += (random.choice(vowels))
    word += (random.choice(vowels))

    word += (random.choice(consonants))
    word += (random.choice(consonants))
    word += (random.choice(consonants))
    word += (random.choice(consonants))

    secondlast = random.randint(0, 1)
    last = random.randint(0, 1)

    if last == 0:
        word += (random.choice(vowels))
    else:
        word += (random.choice(consonants))

    if secondlast == 0:
        word += (random.choice(vowels))
    else:
        word += (random.choice(consonants))

    return word


def reset():
    global debug_mode
    global anagramFound
    global dictionary
    global anagram

    debug_mode = True
    anagramFound = False
    dictionary = set()
    anagram = ""


def main_program():
    algorithm()


def preprocessing(anagram):
    global dictionary

    print("Random Anagram: ", " ".join(anagram))

    dictionary = preproc.import_dictionaryfile("wordfile.txt") # Importing the dictionary file
    dictionary = dropwords(anagram, dictionary)

    dictionary = sorted(dictionary, key=len, reverse=True)

    return dictionary


def algorithm():
    global dictionary
    global anagram

    size = 9  # ideal size of conundrum
    count = 0
    wordfound = "No word found"

    t0 = time.time()

    while size > 2:
        for word in dictionary:

            count += 1

            if collections.Counter(word) == collections.Counter(anagram):
                print("\nFound a nine letter conundrum!")
                wordfound = word
                size = 0
                break
        size -= 1

    # Above gets 9 letter conundrum
    # -----------------------------

    for word in dictionary:
        if not collections.Counter(word) - collections.Counter(anagram):
            wordfound = word
            break

    print()

    print("First word found: --> {} <-- word size {} ".format(wordfound.title(), len(wordfound)))

    print("\nTime: ", time.time() - t0)

    print("\nCount: ", count, size)


# Main Program

debug_mode = True
anagramFound = False

dictionary = set()
anagram = ""

# Variables

#anagram = random_input()
anagram = user_input()

preprocessing(anagram)

main_program()

