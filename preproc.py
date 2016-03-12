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


def import_dictionaryfile(file_name):

    wordlist = set()

    with open(file_name,'r') as f:
        for word in f:
            word = word.strip('\n')
            wordlist.add(word)
    f.close()

    return wordlist

