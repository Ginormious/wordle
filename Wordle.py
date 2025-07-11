#import library
import random
#Stuff we're gonna use later
words = ['Genius', 'Magnificent', 'Impressive', 'Splendid', 'Great', 'Phew']
tryNumber = ["first", "second", "third", "fourth", "fifth", 'sixth']
wordDictionary = {"a":[],"b":[],"c":[],"d":[],"e":[],"f":[],"g":[],"h":[],"i":[],"j":[],"k":[],"l":[],"m":[],"n":[],"o":[],"p":[],"q":[],"r":[],"s":[],"t":[],"u":[],"v":[],"w":[],"x":[],"y":[],"z":[]}
wordDictionary2 = {"a":[],"b":[],"c":[],"d":[],"e":[],"f":[],"g":[],"h":[],"i":[],"j":[],"k":[],"l":[],"m":[],"n":[],"o":[],"p":[],"q":[],"r":[],"s":[],"t":[],"u":[],"v":[],"w":[],"x":[],"y":[],"z":[]}
numlist = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
letter = []
random_word = ""
CYAN="\033[36m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
RESET = "\033[0m"
#function for betting feature
def bet(player_balance, bet_size):
    try:#check if the user input is a number and doesn't exceed their balance
        number = int(bet_size)
        if number<=0:
            print("Please enter a bet that's an integer greater than 0")
            return False
        elif number>player_balance:
            print("You're too poor lol")
            return False
        else:
            return bet_size
    except ValueError:#if it's not an integer a value error occurs, print this error message
        print("Please enter a bet size that's a positive integer")
        return False

#function for grading a word
def good_or_bad(guessWord,green_count,yellow_count,previous_words):
    #I made a program beforehand(it's called counting_letter.py in the main branch)
    #It counts all the letters in the word list we used and sorted them into a dictionary with the keys as the letters and the values being their percentage occurrence which I have set to a 2 decimal point float. Underneath is just what was returned by that code since I don't want to waste time running it every time someone plays again
    letter_frequencies = {'e': 9.31, 's': 9.03, 'a': 6.87, 'r': 5.79, 'l': 5.12, 'o': 5.12, 't': 4.72, 'i': 4.63, 'n': 3.8, 'd': 3.55, 'c': 2.97, 'u': 2.81, 'p': 2.53, 'h': 2.39, 'm': 2.17, 'g': 2.03, 'y': 1.97, 'b': 1.91, 'f': 1.66, 'k': 1.61, 'w': 1.51, 'v': 1.0, 'x': 0.26, 'z': 0.23, 'j': 0.18, 'q': 0.17}

    #additional scores based on if the letter is green or yellow.
    Green_score=7
    Yellow_score=3.5
    letter_score=0
    for i in range(len(guessWord)):#check each letter in the guess word and add up their value scores to use for later
        letter_score+=letter_frequencies[guessWord[i]]
    #the calculation to determine if a word is good or bad
    sum_score=(green_count*Green_score)+(yellow_count*Yellow_score)+letter_score
    #The grading criteria based on the max possible sum_score you can get, that being (7*5)+9.31+9.03+6.87+5.79+5.12 and then subtracting 1/5th of that to form each grading boundary
    if guessWord in previous_words:#if a word is the same as a previous word, it's automatically a horrendous word
        print("Horrendous word")
    elif sum_score >=71.14:
        print("Perfect Word")
    elif sum_score >=56.912:
        print("Great word")
    elif sum_score >=42.684:
        print("Good Word")
    elif sum_score >=28.456:
        print("Bad Word")
    elif sum_score >=14.228:
        print("Horrendous word")

#function for grading the first word the user guesses
def good_or_bad_1st(guessWord,green_count,yellow_count,gray_count):
    letter_frequencies = {'e': 9.30, 's': 9.03, 'a': 6.86, 'r': 5.78, 'l': 5.12, 'o': 5.11, 't': 4.72, 'i': 4.64,
                          'n': 3.80, 'd': 3.55, 'c': 2.97, 'u': 2.81, 'p': 2.53, 'h': 2.39, 'm': 2.18, 'g': 2.03,
                          'y': 1.97, 'b': 1.91, 'f': 1.67, 'k': 1.61, 'w': 1.51, 'v': 1.00, 'x': 0.26, 'z': 0.23,
                          'j': 0.18, 'q': 0.17}#same thing as with the regular good_or_bad function
    Green_score = 7
    Yellow_score = 3.5
    Gray_score = 5#use the gray score to heavily dilute the sum_score so that it mostly depends on how many good often occurring letters there are in the user's input
    letter_score = 0
    for i in range(len(guessWord)):
        letter_score += letter_frequencies[guessWord[i]]
    sum_score = (green_count * Green_score) + (yellow_count * Yellow_score) + (gray_count*Gray_score) + letter_score
    #there is no need to check for already inputted words because this function will only be called during the first input attempt
    if sum_score >= 71.14:
        print("Perfect Word")
    elif sum_score >= 56.912:
        print("Great word")
    elif sum_score >= 42.684:
        print("Good Word")
    elif sum_score >= 28.456:
        print("Bad Word")
    elif sum_score >= 14.228:
        print("Horrendous word")
def initializeWords():
    global wordDictionary
    with open("3000 wordle words.txt", 'r') as words:
        for i in words:
            i = i.lower()
            i = i.strip()
            firstLetter = i[0]
            wordDictionary[firstLetter].append(i)
def initializeWords2():
    global wordDictionary2
    with open("words.txt", 'r') as words:
        for i in words:
            i = i.lower()
            i = i.strip()
            firstLetter = i[0]
            wordDictionary2[firstLetter].append(i)

def getWord():
    global letter, random_word
    for i in wordDictionary.keys():
        letter.append(i)
    randomLetter = random.choice(letter)
    random_word = random.choice(wordDictionary[randomLetter])
def game():
    guessNum = 1
    guessWord = ""
    previous_words = []
    while guessNum < 7:
        print(f"{CYAN}Enter your "+"{} guess:".format(tryNumber[guessNum-1])+f"{RESET}", end = "")
        guessWord = input()
        guessWord = guessWord.lower()
        if len(guessWord) != 5 or not guessWord.isalpha():
            print('Please enter a real 5 letter word')
            continue
        if guessWord not in wordDictionary2[guessWord[0]]:
            print ('Sry bro, we cant find the word in our 5000+ words dictionary, maybe try another word')
            continue
        if guessWord == random_word:
            print(words[guessNum - 1])
            return True
        else:
            green_count = 0
            yellow_count = 0
            gray_count = 0
            if guessNum==1:
                for i in range(len(random_word)):
                    s = guessWord[i]
                    if guessWord[i] == random_word[i]:
                        print(f"{GREEN}" + s + f"{RESET}", end="")
                        green_count += 1
                    elif guessWord[i] in random_word:
                        print(f"{YELLOW}" + s + f"{RESET}", end="")
                        yellow_count += 1
                    else:
                        print(f"{RESET}" + s + f"{RESET}", end="")
                        gray_count += 1
                print()
                good_or_bad_1st(guessWord, green_count, yellow_count,gray_count)
                print()
                guessNum += 1
                previous_words.append(guessWord)
            else:
                for i in range(len(random_word)):
                    s = guessWord[i]
                    if guessWord[i] == random_word[i]:
                        print(f"{GREEN}" + s + f"{RESET}", end="")
                        green_count += 1
                    elif guessWord[i] in random_word:
                        print(f"{YELLOW}" + s + f"{RESET}", end="")
                        yellow_count += 1
                    else:
                        print(f"{RESET}" + s + f"{RESET}", end="")
                print()
                good_or_bad(guessWord, green_count, yellow_count,previous_words)
                print()
                guessNum += 1
                previous_words
    print("The word was", str(random_word))
    return False


initializeWords()
initializeWords2()
player_balance=3

while True:
    print("Your score: "+ str(player_balance))
    bet_size = input("Enter your bet size: ")
    if bet(player_balance,bet_size)!=False:
        player_balance -= int(bet_size)
        getWord()
        result=game()
        if result:
            player_balance+=int(bet_size)*2
            print("Your score has increased by {}, reach 10 to win!!".format(int(bet_size)*2))
            print(player_balance)
        if not result:
            print("Aww dang it, you just lost your bet, reach 0 and you'll LOSE!")
        if player_balance <= 0:
            print ("You lost! Womp Womp, try harder next time ;)")
            break
        if player_balance >= 10:
            print ("Yaaay you won! You're the best Wordle player in the world")
            break
    else:
        continue







