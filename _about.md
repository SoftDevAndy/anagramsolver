### Andrew Sweeney - G00237144

# Countdown Letters Game Solver

This project is created for the Theory of Algorithms module as part of a fourth year project at G.M.I.T.

**Project Outline**

You are required to create two pieces: 

A python script that solves the Countdown letters game

A document explaining how your solver works.

The Countdown letters game is as detailed on Wikipedia. Essentially, you are given a list of nine random letters which contains at least three vowels and four consonants. You must find the longest possible word in the Oxford English dictionary that is an anagram of some or all of the letters in the random list. If there is more than one word of longest length, then each is an acceptable solution.

**Instructions**

Find a list of words in the Oxford English dictionary. This won't be too easy - you might need to join a few different files together. You might even try scraping the Oxford Dictionary's website. If you write any scripts to do that, include them in your submission.

Write a Python script that solves the Countdown letters game in the most efficient way you can.

Write a README file (called _about.md in above gist) about your script.

Add to your Python script a function to test your algorithm, which creates a random list of nine letters as they would be generated in Countdown.

**Extras**

Test a modified version of this project, live, on a flask server [Link](http://devandy.pythonanywhere.com/)
![Webbapp Image](http://puu.sh/oHntX/e246d23ac4.jpg)

# Contents

* Project Plan
* Running the program
* Words List
* Preprocessing
* Solver
* Results
* Summary/Reflection
* References

## Project Plan

**Starting Phase**

* ~~Outline requirements to be met~~
* ~~Research algorithms / Find existing examples~~
* ~~Create/Curate word dictionary file~~
* ~~Import words~~

**Execute Phase**

* ~~Rough draft of algorithm~~
* ~~Alternatives~~
* ~~Fine tuned algorithm~~

**Summary Phase**

* ~~Time functions and find the best results~~
* ~~Write up findings~~

## Running the Program

Download the entire gist including the **solver**, **preproc** and make sure to download the external [wordlist](https://dl.dropboxusercontent.com/u/75064039/wordfile.txt) . Make sure the wordfile.txt is in the same directory as both the **solver** and **preprocy** and then run **solver**.

If you wish to run your own timing test of the program run **compare** and make sure it's in the same directory as the other files.

If you wish to change the amount of times the test runs from the default of 50 change this line in compare.py

```python
testcount = 50
```

## Words List

The creation of the word list involves meeting some criteria.

All of the words must contain 
* No whitespace 
* No special characters
* No numbers
* No non alphabetical characters
* Must be uppercase to make parsing easier
* Must not contain proper nouns

From sources listed below I built up a large dictionary full of words with special characters,numbers and plenty of other stuff to be filtered out. Reading through the list, there were many names that were also included as 'words' and so I accounted for this issue.

Next I gathered proper nouns from the sources below and combined them all together to make a file that would be used to filter out proper nouns from the dictionary that was to be built. This involved days of the week,months,countries and capitals etc. Added to this were common male and female names. All of these sources had to be filtered.

There were many steps in creating the dictionary. Below details the steps taken, scripts created and used.

## How the wordlist.txt was built

**Steps taken for the main dictionary**

* I created a webscraper to download 3000ish commond oxford words [using this script](https://gist.github.com/AndyDev2013/fe94b562fef4dd14ba03) that I made 

Combined multiple dictionaries from sources including the 
* [Oxford3000](http://www.oxfordlearnersdictionaries.com/wordlist/english/oxford3000/)
* [Theory of Algorithms in class wordlist](http://puu.sh/nfyIh/c25f4097de.txt)
* [Second year Java dictionary](http://puu.sh/nfzcu/a8cb82715c.txt)

All three sources combined contained names, proper nouns and words with special characters. All of this must be filtered out to make a more usable dictionary.
 
**For the black list dictionary**

* Created a list of male and female names, formatted them using a [using this script](https://gist.github.com/AndyDev2013/d76cdaa3ccda9cc63194) that I created then combined this clean list of names with the  black list dictionary
* Added countries, capitals, days of the week and seasons to the black list dictionary
* Imported the main dictionary and black list dictionary file and filted out the nouns into a cleaner dictionary [using this script](https://gist.github.com/AndyDev2013/d0e7b1672688a8abe26e) that I created
* Finally the cleaner dictionary is put through [this script](https://gist.github.com/AndyDev2013/d4acb614edc83e5763d9) that I made to drop all words with special characters, larger then 9 letters and other criteria that reduces the size of the dictionary

The wordlist dictionary, even at around 1mb takes a lot of time to render as a gist in Chrome and IE so I attached it externally as a dropbox link. I would like to add that there was an attempt made to remove proper nouns from the Dictionary.  A majority of names and obvious errors will be removed by using the scripts above, however not all of them will be taken out.  In other words the dictionary is not perfect, but a great amount of effort was put in to reduce erroneous words.

The final word file holds roughly **110k** at just under **1mb** words.

[The wordlist/dictionary file](https://dl.dropboxusercontent.com/u/75064039/wordfile.txt)

## Preprocessing

All of the pre-processing was removed from the project, the exception being for the need of reading in the dictionary once from (the?) file. The clean dictionary is read in and the size of it is reduced on the fly to keep things as fast as possible. 

We have global knowledge of our project. We know that we want to find 

* At best a 9 letter anagram
* At worst a 3 letter anagram
* Our worse case is no anagram

Using these rules, I supplied a dictionary with only words between 3 and 9 letters inclusive. This was the first measure taken to reduce the search space. This reduced the amount of words. Carrying out this action as preprocessing or as part of the program would take away from our run time.

## Solver
**Working on this section currently**

**Psuedo Code**

* Take user input with a valid anagram or generate a random valid anagram
* Import the words file into a set, drop all words from the set that don't contain letters in the anagram 
* This set is sorted descending by word length and returned as a sorted list
* Run through all the words of length nine and check if it's a conundrum, remove them from the list one by one, if the word matches stop and print it out to screen
* Otherwise check the rest of the list

**Indepth**

The file gets read in as detailed in Preprocessing.

```python
def import_dictionaryfile(file_name):

    wordlist = set()

    with open(file_name, 'r') as f: # Reading in the file
        for word in f:  # For every word in the file read in
            word = word.strip('\n')  # Strip the new line character from the word
            wordlist.add(word)  # Add the word to the set
    f.close()  # Close the file

    # Finally return the set of words

    return wordlist
```

Next depending on whether you've commented the input line out or not. You'll enter the anagram which must meet the requirements of having 9 letters exactly and this word much include 4 consonants and 3 vowels and 2 more letters of your choice. Below is the code for the user input code

```python
def user_input():
    print("--------------")
    print("Running solver.py")
    print("--------------")

    anagram = input("Please enter a valid conundrum? ")     # Takes the user input

    while checkvalidconundrum(anagram) is False:    # Checks whether the user word is valid if not, try again
        print("\nThe conundrum didn't meet the criteria, try again")
        anagram = input("Please enter a valid conundrum? ")

    anagram = anagram.upper()   # Converts the word to uppercase

    print("Valid Anagram: ", anagram)       # Print success message and return the valid, uppercase word

    return anagram
```

Otherwise the word is generated randomly. For each Q that is randomized and added to the word a matching U is also added to the word. This reduces the amount of vowels to add. It's pretty well commented.

```python
def random_input():
    print("--------------")
    print("Running solver.py")
    print("--------------")

    vowels = list("AEIOU")      # List of vowels
    consonants = list("BCDFGHJKLMNPQRSTVWXYZ")      # List of consonants

    count = 0
    word = ""

    word += (random.choice(consonants))     # Added the first random consonant
    word += (random.choice(consonants))     # Added the second random consonant
    word += (random.choice(consonants))     # Added the third random consonant
    word += (random.choice(consonants))     # Added the fourth random consonant

    while count < word.count('Q'):      # Checks if the word has any Q's if so...
        word += 'U'     # Add a corresponding U
        count += 1      # Mark that we added a vowel (U)

    while count < 3:    # While count of vowels is less then 3 (could have increased because of the Q's and added U's)
        word += (random.choice(vowels))     # Add a random vowel
        count += 1      # Mark that a vowel was added

    # Now 7/9 letters have been added we randomly choose the last 2 letters to add

    secondlast = random.randint(0, 1)       # Random integer between 0 and 1, 0 for a vowel or 1 for a consonant
    last = random.randint(0, 1)     # Random integer between 0 and 1, 0 for a vowel or 1 for a consonant

    if last == 0:
        word += (random.choice(vowels))
    else:
        word += (random.choice(consonants))

    if secondlast == 0:
        word += (random.choice(vowels))
    else:
        word += (random.choice(consonants))

    # Return the finished 9 letter word meeting the criteria

    return word
```

Once the input is given we can use the letters to drop words from the dictionary that contain the same letters.

The first thing I wanted to do was to remove all of the words from the dictionary, that contain letters that aren't in the anagram. This was the second step to drastically reduce the search space when searching for anagrams.

Words in Python parsed to sets are allowed to be subtracted from each other, This operation is pretty quick and can be used to tell if a word contains the same letters in the anagram, but it doesn't account for duplicates (I account for this later).

The method below shows the following

* Converts the anagram into a set, e.g a set for the anagram CONUNDRUM would contain only the unique letters *C D M N O R U*
* Next we iterate through all the words in the dictionary of possible words t
* The word is cast into a set of letters e.g the word MUG
* Subtracting the anagram set from the word set results in ['G'] being left over
* This means the letter G isn't in the conundrum and we can throw away the word
* MUG is not an anagram of CONUNDRUM because CONUNDRUM doesn't contain the letter G 

```python
def dropwords():
     if len(list(set('MUG') - set("CONUNDRUM"))) is not 0:
         print(list(set('MUG') - set("CONUNDRUM")))
```

This was adapted into the code below. All of the words that contain valid letters for the anagram are kept and added to a cleanwordlist set and returned.

```python
def dropwords(anagram, wordlist):
    cleanwordlist = set()
    letters = set(anagram)

    for word in wordlist:
        if len(list(set(word) - set(letters))) is 0:
            cleanwordlist.add(word)
            
    return cleanwordlist
```

The following line is then called to turn the set into a list of sorted words, sorted by length. So words of length nine are at the top and words of length three are at the bottom

```python
dictionary = sorted(dictionary, key=len, reverse=True) 
```

The algorithm is finally called which uses this sorted list

```python
def algorithm():
    global dictionary
    global anagram

    tempdictionary = dictionary

    wordfound = "No word found"     # Default word
    count = 0

    t0 = time.time()

    # NB at this point we know the dictionary is in descending order my length

    print()
    print("Size of dictionary with 9 letter words: ", len(tempdictionary))

    for word in tempdictionary:     # For each word in the wordlist dictionary

        count += 1      # Increase the count, just for tracking the amount of iterations

        if collections.Counter(word) == collections.Counter(anagram):

            # If the word contains the same amount of matching letters as the anagram

            print("\nFound a nine letter conundrum!")
            wordfound = word
            break

        if len(word) != 9:  # Once you reach
            break
        else:

            # The word isn't a 9 letter anagram so remove it from the dictionary

            tempdictionary.remove(word)

    print("Size of dictionary with 9 letter words removed: ", len(tempdictionary))

    # Above gets 9 letter conundrum
    # -----------------------------

    for word in tempdictionary:

        count += 1

        if not collections.Counter(word) - collections.Counter(anagram):

            # Removes the anagram letters from the word
            # If any letters are left over in the collections.Counter(word) it's not an anagram and returns true because there is information in the counter
            # Otherwise the counter is empty which means we have a valid anagram

            print()
            print("collections.Counter(word): ", collections.Counter(word))
            print("collections.Counter(anagram): ", collections.Counter(anagram))
            print("collections.Counter(word) - collections.Counter(anagram): ", collections.Counter(word) - collections.Counter(anagram))
            wordfound = word
            break

    print()
    print("First word found: --> {} <-- word size {} ".format(wordfound.title(), len(wordfound)))
    print("\nTime: ", time.time() - t0)
    print("\nCount: ", count)

    return {'Time': time.time() - t0}
```

There is two stages to this algorithm.

**The first stage involves iterating through all the words in the word dictionary.**

Using collections.Counter which is a specialized container datatype. You can pass in a word and the container will hold key value pairings for the letters in the word. So using collections.Counter("test") would return Counter({'t': 2, 's': 1, 'e': 1}) . It counts very quickly the number of occurances of each individual letter. Using this I check is the anagram given randomly or by the user is identical in letter count to the word it's a valid nine letter conundrum. 

```python
if collections.Counter(word) == collections.Counter(anagram):
``` 

```python
import collections

print(collections.Counter("test"))
print(collections.Counter("sett"))

#Counter({'t': 2, 's': 1, 'e': 1}) Both results return the same and ordered
#Counter({'t': 2, 's': 1, 'e': 1}) Both results return the same and ordered
```

Each time a word fails this check it gets removed from the dictionary, if it passes this check the whole algorithm stops and the word is returned and printed to screen. This first iteration of the dictionary runs for aslong as the words are exactly nine in length.

**The second stage of the algorithm**

The second stage runs through the remaining dictionary after the words of length nine were removed

The important line of the second part of the algorithm is as follows

```python
if not collections.Counter(word) - collections.Counter(anagram):
```

This line takes care of many things. It lets you take all the valid letters from the word supplied.

* If any letters are left over the word can't be used and you can skip to the next word
* A word containing the same unique letters but the wrong amount of them won't be used and you can skip to the next word
* If nothing is returned (Counter() an empty Counter container) then the word contains the same letters and same amount of letters as in the anagram, meaning the word is an anagram of the anagram. Below clearly shows how all of this works.

```python
import collections

print(collections.Counter("TEASE") - collections.Counter("TASTE")) # Too many E's 
print(collections.Counter("EATS") - collections.Counter("TASTE")) # Same amount of unique letters

#Counter({'E': 1})
#Counter()
```

If the empty counter container is returned the algorithm breaks, returns the word immediately and prints it out. This is when the program ends.

The empty counter container is caught by using the below if not statement

```python
if not
```

## Results

**Two tests running the program and the time it took**

Both tests resulted in the same time of less then 0.001 of a second. Timing programs that end up being around this time scale can be effected by other processes running on the computer

![Screenshot](http://puu.sh/nEzNw/d4035b4a79.png)
![Screenshot](http://puu.sh/nEzMT/136cf9e206.png)

## Summary/Reflection

### Gists

All of the scripts for this project were kept in public gists for the entirity of the project. This was convenient and almost like using a repo'd version of pastebin. Great for sharing and throwing up a script online quckly. 

The only issue that came up when using Gists was storing the dictionary files as a Gist. In Chrome and IE on both my computer and laptop the file would cause some sort of memory leak as the browser kept trying to render the thousands of words. This would ultimately crash the page or browser due to the size of the file. The result of this was storing the dictionary in a public dropbox and linking to it.

### Using Python

Python was used for everything in this project. The creation of the dictionary, the webscraper and the charting later. Python was very handy and perfect for creating small powerful scripts that were quick to put together and get the task done. The majority of the programming was done in Sublime Text and then later in PyCharm. I had the latest version of 3.5 installed which restricted me a litle when I later wanted to create some graphs of the running time. Other then certain libraries and packages not being available for the most upto date version (understandable) of Python there were no issues.

### Scrapped Permutations

**Originally I had gone through great lengths to find the fastest way for generating all the permutations of a nine letter algorithm. This was removed because I found a much more elegant way which didn't include generating and using multiple permutations or a word.
Implementing the checking of every permutation of a word would drastically increase the search time when finding an anagram/conundrum.
As fast as it turned out to be, it wasn't needed but moved the findings to this section to show the process.**

The conundrum must be 9 letters and fit the criteria so the factorial for nine unique letters gives 362,880 permutations. If any of the letters repeat this drastically reduces the amout of permutations. A nine letter word with two of the same letter reduces the 362,880 down to half 181,440. A good source for working out this information is [here](http://www.regentsprep.org/regents/math/algebra/apr2/LpermRep.htm)

The generating of all the permutations were done using a recursive algorithm which is widely used when generating permutations for numbers and alogrithms. I had to adapt it to the python language and make it form to fit my means. This recursive algorithm is similar to the one in class we have done. Sources for this are 

* [Site 1](http://www.toves.org/books/java/ch18-recurex/)
* [Site 2](http://www.dreamincode.net/forums/topic/188032-java-recursion-anagram/)
* [Site 3](http://www.bowdoin.edu/~ltoma/teaching/cs107/fall05/Examples/Anagram.java)

There was many more sources but they all cite the same method for anagram generation. 

Below is the adapted Python version. It's been changed to take a global set. A set was used specifically over an array because adding to it and looking up strings with a set was far superior when testing which was faster for these operations. 

```python

words = set() 

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
            
recursive(words, "", given_word)         
```

*One of the main reasons for using a set was because of the following.*
If a word with 2 repeating letters was used, for example _conundrum_. Conundrum contains two n's and two u's. The recursive method doesn't account for duplicates, it will generate them anyways. But the set only allows unique words. The more repeating letters, the less permutations.

I tried initially to create a method that checked if the word already existed in the array(when I tried using an array) but this was very slow. The more words that get added to the array, the longer the look ups take and in big O notation this is one of the worst cases. Searching through a growing space,requires more time and both of these times increase. Examples of this will be in the efficency section.

Using a set was a more elegant solution, it catches the duplicates when they are generated. This helps drastically reduce the search space *IF* the word contains letters that aren't highly used. [This site](http://www.oxforddictionaries.com/words/which-letters-are-used-most) shows the letter frequency. As you can see U C and M are lower in frequency so this kind of filtering for a word like CONUNDRUM would reduce the search space by alot. 

Here is a comparison between using an array and a set to show how the set rejects duplicates.

```python
wordArray = []
wordSet = set()

def recursive(wordArray, wordSet, prefix, word):
    i = 0
    if len(word) <= 1:
        wordArray.append(prefix + word)
        wordSet.add(prefix + word)
    else:
        while i < len(word):

            x = i + 1

            current = word[i:x]
            before = word[0:i]
            after = word[x:]
            recursive(wordArray, wordSet, prefix + current, before + after)
            i += 1


recursive(wordArray, wordSet, "", "CONUNDRUM")

print(len(wordArray))
print(len(wordSet))     
```

Here is an example of how a look up on an array mentioned above gets slower over time

```python
wordArray = []

count = 0

def recursive(wordArray, prefix, word):
    i = 0

    global count

    count += 1

    if count % 20000 is 0:
        print(count)

    if len(word) <= 1:
        if word not in wordArray:
            wordArray.append(prefix + word)
    else:
        while i < len(word):

            x = i + 1

            current = word[i:x]
            before = word[0:i]
            after = word[x:]
            recursive(wordArray,prefix + current, before + after)
            i += 1

recursive(wordArray, "", "CONUNDRUM")

print(len(wordArray))
```

It's much better to use a set, you could always iterate over the array later and remove duplicates instead of doing it when they are getting generated, doing so would still cost time. A set proved the most efficient solution across the board.

## References

**Extra Scripts created specifically for this project**

* [scraper.py](https://gist.github.com/AndyDev2013/fe94b562fef4dd14ba03)
* [names.py](https://gist.github.com/AndyDev2013/d76cdaa3ccda9cc63194)
* [removenoun.py](https://gist.github.com/AndyDev2013/d0e7b1672688a8abe26e)
* [dictionaryCleaner.py](https://gist.github.com/AndyDev2013/d4acb614edc83e5763d9)

**Dictionary Sources**

* [Oxford3000](http://www.oxfordlearnersdictionaries.com/wordlist/english/oxford3000/)
* [Theory of Algorithms in class wordlist](http://puu.sh/nfyIh/c25f4097de.txt)
* [Second year dictionary](http://puu.sh/nfzcu/a8cb82715c.txt)

**Proper Noun sources**

* [Capitals and Countries](https://www.countries-ofthe-world.com/capitals-of-the-world.html)
* [Common Male Names](http://deron.meranda.us/data/census-dist-male-first.txt)
* [Common Female Names](http://deron.meranda.us/data/census-dist-female-first.txt)
* [Months,Days,Seasons](http://www.vocabulary.cl/Basic/Days_Months_Seasons.htm)

**Read Sources**

* [Stackoverflow Generating Algorithms Permutations](http://stackoverflow.com/questions/4240080/generating-all-permutations-of-a-given-string)
* [Stackoverflow all given permutations of a string](http://stackoverflow.com/questions/361/generate-list-of-all-possible-permutations-of-a-string)
* [Java recursion example](https://sites.google.com/site/learnjav/java/recursion)
* [Java recursion algorithm](https://sites.google.com/site/learnjav/java/recursion/Anagrams.java?attredirects=0) 
* [Permutations ProgrammerInterview](http://www.programmerinterview.com/index.php/recursion/permutations-of-a-string/)
* [Permutations Princeston Java](http://introcs.cs.princeton.edu/java/23recursion/Permutations.java.html)
* [GeeksforGeeks](http://www.geeksforgeeks.org/write-a-c-program-to-print-all-permutations-of-a-given-string/)