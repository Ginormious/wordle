from collections import Counter
import string

def count_letters():
    with open("3000 wordle words.txt", 'r') as words:#read all the words
        text = words.read()
    letter_counts = Counter(text.lower())#use the Counter function on the lowercase text which returns a dictionary
    total_letters = sum(letter_counts.values())#Need for later calculations
    #calculate percentage of each letter occurring and then rounding to the nearest 2 decimal places
    letter_freq = {letter: round((letter_counts.get(letter, 0) / total_letters) * 100, 2) for letter in string.ascii_lowercase}
    #sorts the dictionary based on which letter occurred the most often by using the sorted function
    sort_dictionary= dict(sorted(letter_freq.items(), key=lambda value: value[1], reverse=True))
    #prints and returns the sorted dictionary
    print(sort_dictionary)
    return sort_dictionary

count_letters()