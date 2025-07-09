import random, os, math

words = ['Genius', 'Magnificent', 'Impressive', 'Spelndid', 'Great', 'Phew']

wordDictionary = {"a":[],"b":[],"c":[],"d":[],"e":[],"f":[],"g":[],"h":[],"i":[],"j":[],"k":[],"l":[],"m":[],"n":[],"o":[],"p":[],"q":[],"r":[],"s":[],"t":[],"u":[],"v":[],"w":[],"x":[],"y":[],"z":[]}
letter = []
random_word = ""
GREEN = "\033[32m"
YELLOW = "\033[33m"
RESET = "\033[0m"
def initializeWords():
    global wordDictionary
    with open("words.txt", 'r') as words:
        for i in words:
            i = i.lower()
            i = i.strip()
            firstLetter = i[0]
            wordDictionary[firstLetter].append(i)

def getWord():
    global letter, random_word
    for i in wordDictionary.keys():
        letter.append(i)
    randomLetter = random.choice(letter)
    random_word = random.choice(wordDictionary[randomLetter])
def game():
    guessNum = 1
    guessWord = ""
    while guessNum < 7:
        print("Enter your {} guess:".format(str(guessNum)), end = "")
        guessWord = input()
        if guessWord == random_word:
        
            print(words[guessNum - 1])
            break
        if len(guessWord) != 5:
            print('Please enter a 5 character word')
            continue
        else:
            for i in range(len(random_word)):
                if guessWord[i] == random_word[i]:
                    print(str(guessWord[i]), 'Is', 'Green')
                elif guessWord[i] in random_word:
                    print(str(guessWord[i]), 'Is', 'Yellow')
                else:
                    print(str(guessWord[i]), 'Is', 'Gray')
        guessNum += 1
    print("The word was", str(random_word))
initializeWords()
getWord()
game()
"""
first_try = input('Enter your first guess: ')


second_try = input('Enter your second guess: ')
if second_try == random_word:
    print("Magnificent")
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


"""