import random, os, math
wordDictionary = {"a":[],"b":[],"c":[],"d":[],"e":[],"f":[],"g":[],"h":[],"i":[],"j":[],"k":[],"l":[],"m":[],"n":[],"o":[],"p":[],"q":[],"r":[],"s":[],"t":[],"u":[],"v":[],"w":[],"x":[],"y":[],"z":[]}
def initializeWords():
    global wordDictionary
    with open("words.txt", 'r') as words:
        for i in words:
            i = i.lower()
            i = i.strip()
            firstLetter = i[0]
            wordDictionary[firstLetter].append(i)
initializeWords()
letter = []
for i in wordDictionary.keys():
    letter.append(i)
randomLetter = random.choice(letter)
random_word = random.choice(wordDictionary[randomLetter])

first_try = input('Enter your first guess: ')
if first_try == random_word:
    print("Genius")
    print(random_word)
    quit()
if len(first_try) != 5:
    print('Please enter a 5 character word')
else:
    for i in range(len(random_word)):
        if first_try[i] == random_word[i]:
            print(str(first_try[i]), 'Is', 'Green')
        elif first_try[i] in random_word:
            print(str(first_try[i]), 'Is', 'Yellow')
        else:
            print(str(first_try[i]), 'Is', 'Gray')

second_try = input('Enter your second guess: ')
if second_try == random_word:
    print("Magnificent")
    print(random_word)
    quit()
if len(second_try) != 5:
    print('Please enter a 5 character word')
else:
    for i in range(len(random_word)):
        if second_try[i] == random_word[i]:
            print(str(second_try[i]), 'Is', 'Green')
        elif second_try[i] in random_word:
            print(str(second_try[i]), 'Is', 'Yellow')
        else:
            print(str(second_try[i]), 'Is', 'Gray')

third_try = input('Enter your third guess: ')
if third_try == random_word:
    print("Impressive")
    print(random_word)
    quit()
if len(third_try) != 5:
    print('Please enter a 5 character word')
else:
    for i in range(len(random_word)):
        if third_try[i] == random_word[i]:
            print(str(third_try[i]), 'Is', 'Green')
        elif third_try[i] in random_word:
            print(str(third_try[i]), 'Is', 'Yellow')
        else:
            print(str(third_try[i]), 'Is', 'Gray')

fourth_try = input('Enter your fourth guess: ')
if fourth_try == random_word:
    print("Splendid")
    print(random_word)
    quit()
if len(fourth_try) != 5:
    print('Please enter a 5 character word')
else:
    for i in range(len(random_word)):
        if fourth_try[i] == random_word[i]:
            print(str(fourth_try[i]), 'Is', 'Green')
        elif fourth_try[i] in random_word:
            print(str(fourth_try[i]), 'Is', 'Yellow')
        else:
            print(str(fourth_try[i]), 'Is', 'Gray')

fifth_try = input('Enter your fifth guess: ')
if fifth_try == random_word:
    print("Great")
    print(random_word)
    quit()
if len(fifth_try) != 5:
    print('Please enter a 5 character word')
else:
    for i in range(len(random_word)):
        if fifth_try[i] == random_word[i]:
            print(str(fifth_try[i]), 'Is', 'Green')
        elif fifth_try[i] in random_word:
            print(str(fifth_try[i]), 'Is', 'Yellow')
        else:
            print(str(fifth_try[i]), 'Is', 'Gray')

sixth_try = input('Enter your sixth guess: ')
if sixth_try == random_word:
    print("Phew")
    print(random_word)
    quit()
if len(sixth_try) != 5:
    print('Please enter a 5 character word')
else:
    for i in range(len(random_word)):
        if sixth_try[i] == random_word[i]:
            print(str(sixth_try[i]), 'Is', 'Green')
        elif sixth_try[i] in random_word:
            print(str(sixth_try[i]), 'Is', 'Yellow')
        else:
            print(str(sixth_try[i]), 'Is', 'Gray')

print("The word was", str(random_word))
