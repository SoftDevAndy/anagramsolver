### Andrew Sweeney - G00237144

# Countdown Letters Game Solver

This project is created for the Theory of Algorithms module as part of a fourth year project at G.M.I.T.

**Project Outline**

You are required to create two pieces: a Python script that solves the Countdown letters game, and a document explaining how your solver works. The Countdown letters game is as detailed on Wikipedia. Esentially, you are given a list of nine random letters which contains at least three vowels and four consonants. You must find the longest possible word in the Oxford English dictionary that is an anagram of some or all of the letters in the random list. If there is more than one word of longest length, then each is as acceptable a solution as the others.

**Instructions**

Find a list of words in the Oxford English dictionary. This won't be too easy - you might need to join a few different files together. You might even try scraping the Oxford Dictionary's website. If you write any scripts to do that, include them in your submission.

Write a Python script that solves the Countdown letters game in the most efficient way you can.

Write a README file (called _about.md in above gist) about your script.

Add to your Python script a function to test your algorithm, which creates a random list of nine letters as they would be generated in Countdown.

# Contents

* Project Plan
* Words List
* Python Script
* Preprocessing
* Efficiency
* Results
* Summary/Reflection
* References

## Project Plan

**Starting Phase**

* ~~Outline requirements to be met~~
* ~~Research algorithms / Find existing examples~~
* ~~Create/Curate word dictionary file~~

**Execute Phase**

* Import words
* Rough draft of algorithm
* Fine tuned algorithm
* Alternatives
* More to come...

**Summary Phase**

* Time functions and find the best results
* Write up findings

## Words List

The first source for creating the dictionary was from from [Oxford 3000](http://www.oxfordlearnersdictionaries.com/wordlist/english/oxford3000/). I grabbed all of the words but some of them were too long or too short, contained whitespace, numbers and special characters. Most dictionaries will contain some of those things, at least in the case with special characters in words like apostrophies. Seeing the project was in Python I __created a small script__ for creating clean dictionary file from a text file of words [Dictionary Cleaner](https://gist.github.com/AndyDev2013/d4acb614edc83e5763d9).

More to come...

## Python script

## Preprocessing

## Efficiency

## Results

## Summary/Reflection

## References

**Extra Scripts created specifically for this project**

* [names.py](https://gist.github.com/AndyDev2013/d76cdaa3ccda9cc63194)
* [dictionaryCleaner.py](https://gist.github.com/AndyDev2013/d4acb614edc83e5763d9)
* [removenoun.py](https://gist.github.com/AndyDev2013/d0e7b1672688a8abe26e)

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