import random, os, math

words = ['Genius', 'Magnificent', 'Impressive', 'Splendid', 'Great', 'Phew']
tryNumber = ["first", "second", "third", "fourth", "fifth", 'sixth']
wordDictionary = {"a":[],"b":[],"c":[],"d":[],"e":[],"f":[],"g":[],"h":[],"i":[],"j":[],"k":[],"l":[],"m":[],"n":[],"o":[],"p":[],"q":[],"r":[],"s":[],"t":[],"u":[],"v":[],"w":[],"x":[],"y":[],"z":[]}
numlist = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
letter = []
random_word = ""
CYAN="\033[36m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
RESET = "\033[0m"
def good_or_bad(guessWord,green_count,yellow_count):
    letter_frequencies = {'s': 10.4,'e': 10.3,'a': 8.9,'o': 6.7,'r': 6.5,'i': 5.9,'l': 5.5,'t': 5.2,'n': 4.5,'d': 3.9,'u': 3.8,'c': 3.3,'y': 3.1,'p': 3.1,'m': 3.0,'h': 2.7,'g': 2.5,'b': 2.5,'k': 2.1,'f': 1.8,'w': 1.5,'v': 1.1,'z': 0.6,'x': 0.5,'j': 0.4,'q': 0.2}
    Green_score=10
    Yellow_score=8
    letter_score=0
    for i in range(len(guessWord)):
        letter_score+=letter_frequencies[guessWord[i]]
    sum_score=(green_count*Green_score)+(yellow_count*Yellow_score)+letter_score
    if sum_score >=92.8:
        print("Perfect Word")
    elif sum_score >=74.24:
        print("Great word")
    elif sum_score >=55.68:
        print("Good Word")
    elif sum_score >=37.12:
        print("Bad Word")
    elif sum_score >=18.5:
        print("Horrendus word")
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
        print(f"{CYAN}Enter your "+"{} guess:".format(tryNumber[guessNum-1])+f"{RESET}", end = "")
        guessWord = input()
        if len(guessWord) != 5 or not guessWord.isalpha():
            print('Please enter a 5 character word')
            continue
        if guessWord == random_word:
            print(words[guessNum - 1])
            break
        else:
            green_count = 0
            yellow_count = 0
            for i in range(len(random_word)):
                s = guessWord[i]
                if guessWord[i] == random_word[i]:
                    print(f"{GREEN}"+s+f"{RESET}", end="")
                    green_count += 1
                elif guessWord[i] in random_word:
                    print(f"{YELLOW}"+s+f"{RESET}", end="")
                    yellow_count += 1
                else:
                    print(f"{RESET}"+s+f"{RESET}", end="")
            print()
            good_or_bad(guessWord,green_count,yellow_count)
            print()
        guessNum += 1
    print("The word was", str(random_word))


gameover = False
initializeWords()
while not gameover:
    getWord()
    game()
    over = input("Another Game?(y/n):")
    if(over.lower()=="n"):
        gameover = True
        break
