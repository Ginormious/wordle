import random, os, math

words = ['Genius', 'Magnificent', 'Impressive', 'Splendid', 'Great', 'Phew']

wordDictionary = {"a":[],"b":[],"c":[],"d":[],"e":[],"f":[],"g":[],"h":[],"i":[],"j":[],"k":[],"l":[],"m":[],"n":[],"o":[],"p":[],"q":[],"r":[],"s":[],"t":[],"u":[],"v":[],"w":[],"x":[],"y":[],"z":[]}
letter = []
random_word = ""
CYAN="\033[36m"
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
        print(f"{CYAN}Enter your "+"{} guess:".format(str(guessNum))+f"{RESET}", end = "")
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


gameover = False
initializeWords()
while not gameover:
    getWord()
    game()
    over = input("Another Game?(y/n):")
    if(over.lower()=="n"):
        gameover = True
        break
    os.system("cls")