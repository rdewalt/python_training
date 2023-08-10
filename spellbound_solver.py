#  This script will output one of the potential solutions to the Penny Press/Dell Puzzles 'Spellbound' style puzzle.
# This merely iterates out potential solves.  Because it was an interesting problem.

#Each row contains a word (4-7 characters) wherein::
# No letter can be repeated.
# No letter can be used if it was in the prior word.
#They provide 11 rows with the first 1-2 characters filled in. 

import nltk
import re
import random

nltk.download('words')
from nltk.corpus import words

def csd(wordlen):
    word_list = words.words()
    return [word for word in word_list if len(word) == wordlen]

def pick_random_word(word_list):
    return random.choice(word_list)

def has_unique_letters(word):
    return len(set(word)) == len(word)

def matches_pattern(word, regex_pattern):
    return re.search(regex_pattern, word) is not None

#Does Not Contain Letters...
def ncl(word, letters_to_exclude):
    return any(letter in word for letter in letters_to_exclude)

#Find words based on regex and exclusion. That's what it stands for.
def fwbr(dictionary, regex_pattern, letters_to_exclude):
    filtered_words = [
        word for word in dictionary
        if matches_pattern(word, regex_pattern) and not ncl(word, letters_to_exclude)
    ]
    return filtered_words

u4lw = [word for word in csd(4) if has_unique_letters(word)]
u5lw = [word for word in csd(5) if has_unique_letters(word)]
u6lw = [word for word in csd(6) if has_unique_letters(word)]
u7lw = [word for word in csd(7) if has_unique_letters(word)]

print("Number of unique-letter-four-letter words:", len(u4lw))
print("Number of unique-letter-five-letter words:", len(u5lw))
print("Number of unique-letter-six-letter words:", len(u6lw))
print("Number of unique-letter-seven-letter words:", len(u7lw))

#Regex pattern is the "current word we are on"
regex_pattern = r'^m(.+)'
#For the first word, we only need the letters provided in the second word.
exclude_these_letters={'u','s'}

#Since this one is 5 letters, we use u5lw.   For six, or seven or four?  You can grok what you need to do here.
filtered_words = fwbr(u5lw, regex_pattern, exclude_these_letters)

random_word_pick = pick_random_word(filtered_words)
exclude_these_letters = set(list(set(random_word_pick)))
print(f"First Round Word:{random_word_pick}")

#Second word..
regex_pattern = r'^su(.+)'
#  The first word is stored as the "exclude" already, so all we have to add are the provided letters for the NEXT WORD. 
exclude_these_letters.add('a')
filtered_words = fwbr(u7lw, regex_pattern, exclude_these_letters)
random_word_pick = pick_random_word(filtered_words)
exclude_these_letters = set(list(set(random_word_pick)))
print(f"Second Round Word:{random_word_pick}")

# REPEAT FOR THE WHOLE PUZZLE.
regex_pattern = r'^a(.+)'
exclude_these_letters.add('f')
exclude_these_letters.add('l')
filtered_words = fwbr(u5lw, regex_pattern, exclude_these_letters)
random_word_pick = pick_random_word(filtered_words)
exclude_these_letters = set(list(set(random_word_pick)))
print(f"Third Round Word:{random_word_pick}")


regex_pattern = r'^fl(.+)'
exclude_these_letters.add('w')
exclude_these_letters.add('i')
filtered_words = fwbr(u6lw, regex_pattern, exclude_these_letters)
random_word_pick = pick_random_word(filtered_words)
exclude_these_letters = set(list(set(random_word_pick)))
print(f"Fourth Round Word:{random_word_pick}")

regex_pattern = r'^wi(.+)'
exclude_these_letters.add('m')
exclude_these_letters.add('o')
filtered_words = fwbr(u6lw, regex_pattern, exclude_these_letters)
random_word_pick = pick_random_word(filtered_words)
exclude_these_letters = set(list(set(random_word_pick)))
print(f"Fifth Round Word:{random_word_pick}")

regex_pattern = r'^mo(.+)'
exclude_these_letters.add('p')
filtered_words = fwbr(u6lw, regex_pattern, exclude_these_letters)
random_word_pick = pick_random_word(filtered_words)
exclude_these_letters = set(list(set(random_word_pick)))
print(f"Sixth Round Word:{random_word_pick}")

regex_pattern = r'^p(.+)'
exclude_these_letters.add('s')
filtered_words = fwbr(u4lw, regex_pattern, exclude_these_letters)
random_word_pick = pick_random_word(filtered_words)
exclude_these_letters = set(list(set(random_word_pick)))
print(f"Seventh Round Word:{random_word_pick}")

regex_pattern = r'^s(.+)'
exclude_these_letters.add('l')
exclude_these_letters.add('i')
filtered_words = fwbr(u5lw, regex_pattern, exclude_these_letters)
random_word_pick = pick_random_word(filtered_words)
exclude_these_letters = set(list(set(random_word_pick)))
print(f"Eighth Round Word:{random_word_pick}")

regex_pattern = r'^li(.+)'
exclude_these_letters.add('h')
filtered_words = fwbr(u6lw, regex_pattern, exclude_these_letters)
random_word_pick = pick_random_word(filtered_words)
exclude_these_letters = set(list(set(random_word_pick)))
print(f"Ninth Round Word:{random_word_pick}")

regex_pattern = r'^h(.+)'
exclude_these_letters.add('s')
filtered_words = fwbr(u5lw, regex_pattern, exclude_these_letters)
random_word_pick = pick_random_word(filtered_words)
exclude_these_letters = set(list(set(random_word_pick)))
print(f"Tenth Round Word:{random_word_pick}")

regex_pattern = r'^s(.+)'
filtered_words = fwbr(u5lw, regex_pattern, exclude_these_letters)
random_word_pick = pick_random_word(filtered_words)
exclude_these_letters = set(list(set(random_word_pick)))
print(f"Eleventh Round Word:{random_word_pick}")
