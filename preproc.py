# Andrew Sweeney
# G00237144
# February 2016

# From in class and numerous examples online, this recursive method
# seems to be the de-facto way of generating permutaions efficiently

# Sources
# https://sites.google.com/site/learnjav/java/recursion
# https://sites.google.com/site/learnjav/java/recursion/Anagrams.java?attredirects=0

# Added a parameter for passing a set
# It's a set because it ignores duplicates when
# using words with repeating characters e.g test has two t's
# but a word with no repeating characters would be something like bath


def import_dictionaryfile(file_name, debugmsg):

    if debugmsg is True:
        print("\nimport_dictionaryfile\n")

    with open(file_name, 'r') as filein:
        wordlist = filein.readlines()
    filein.close()

    return wordlist


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
