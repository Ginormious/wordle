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
def initializeWords(): # initiallize the dictionary that holds the letter that we choose the word to guesss from
    global wordDictionary # declare global so the program know wordDictionary is not a local variable
    with open("3000 wordle words.txt", 'r') as words: # open text file in read mode
        for i in words:
            i = i.lower() #read the text file and make them all lowercase
            i = i.strip()
            firstLetter = i[0] #sorting them by alphabet 
            wordDictionary[firstLetter].append(i) #adding the word to dictionary
def initializeWords2(): #initialize our word bank to make sure the word the user entered is a valid word
    global wordDictionary2 
    with open("words.txt", 'r') as words: # same as above
        for i in words:
            i = i.lower()
            i = i.strip()
            firstLetter = i[0]
            wordDictionary2[firstLetter].append(i)

def getWord(): #get a random word from wordDictionary
    global letter, random_word #declare global so other functions can use it
    for i in wordDictionary.keys():
        letter.append(i) #get all the letters 
    randomLetter = random.choice(letter) #get an alphabet to choose the word from
    random_word = random.choice(wordDictionary[randomLetter]) # get a word from the list containing all the words starting with randomLetter
def game(): # where the magic happens
    guessNum = 1 #variable to keep track of guesses 
    guessWord = "" #the word to guess for
    previous_words = [] #what the previous guesses by the user is 
    while guessNum < 7:
        print(f"{CYAN}Enter your "+"{} guess:".format(tryNumber[guessNum-1])+f"{RESET}", end = "") #change the font color to cyan cuz why not and ask the user for an input(guess)
        guessWord = input()
        guessWord = guessWord.lower() #make all inputs lowercase to prevent errors in program
        if len(guessWord) != 5 or not guessWord.isalpha(): #make sure the input is 5 letters long and not a number or special character
            print('Please enter a real 5 letter word')
            continue
        if guessWord not in wordDictionary2[guessWord[0]]: #make sure the input is a valid 5 letter word and not something random like asdfs
            print ('Sry bro, we cant find the word in our 5000+ words dictionary, maybe try another word')
            continue
        if guessWord == random_word: # check to see if the guess is correct
            print(words[guessNum - 1]) #this is the respons users get depending on which guess they got the word correct
            return True # word is guessed, break out of loop
        else: #if the word is valid and not the right word
            green_count = 0
            yellow_count = 0 
            gray_count = 0
            if guessNum==1:#first guess
                for i in range(len(random_word)): #loop through the word
                    s = guessWord[i]
                    if guessWord[i] == random_word[i]: #check if the letter is on the right spot
                        print(f"{GREEN}" + s + f"{RESET}", end="") #set font color to green and back to white after printing the letter
                        green_count += 1
                    elif guessWord[i] in random_word: #check if the letter is in the random word
                        print(f"{YELLOW}" + s + f"{RESET}", end="") #print letter in yellow and back to white after
                        yellow_count += 1
                    else:
                        print(f"{RESET}" + s + f"{RESET}", end="") # letter not in random word 
                        gray_count += 1
                print() #skip a line after
                good_or_bad_1st(guessWord, green_count, yellow_count,gray_count) #call on the function to determine how good the guess is.
                print() #skip a line
                guessNum += 1 # move on to next guess
                previous_words.append(guessWord) # add current guess to the list
            else:
                for i in range(len(random_word)): #same as above
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
                good_or_bad(guessWord, green_count, yellow_count,previous_words) #this time its not the first guess, so it calls on the function that determine how good it is based on previous guesses and the correct word.
                print()
                guessNum += 1
                previous_words
    print("The word was", str(random_word))
    return False #user lost(ran out of tries)

#int main()
initializeWords()
initializeWords2() #call on function to initialize dictionary
player_balance=3

while True:
    print("Your score: "+ str(player_balance)) #the score/bet system
    bet_size = input("Enter your bet size: ")
    if bet(player_balance,bet_size)!=False:
        player_balance -= int(bet_size) #remove bet from balance
        getWord() # get the random word
        result=game() #play game and see if user guessed the correct word
        if result:
            player_balance+=int(bet_size)*2 # when won add the points back with bonus
            print("Your score has increased by {}, reach 10 to win!!".format(int(bet_size)*2))
            print(player_balance)
        if not result:
            print("Aww dang it, you just lost your bet, reach 0 and you'll LOSE!") #when did not guess the word
        if player_balance <= 0:
            print ("You lost! Womp Womp, try harder next time ;)") #lose condition points <0
            break
        if player_balance >= 10: #win condition, points >10
            print ("Yaaay you won! You're the best Wordle player in the world")
            break
    else:
        continue






