import tkinter as tk
from tkinter import messagebox
import random


# Word lists and dictionaries
words = ['Genius', 'Magnificent', 'Impressive', 'Splendid', 'Great', 'Phew']
tryNumber = ["first", "second", "third", "fourth", "fifth", 'sixth']
letter_frequencies = {
    'e': 9.30, 's': 9.03, 'a': 6.86, 'r': 5.78, 'l': 5.12, 'o': 5.11, 't': 4.72, 'i': 4.64,
    'n': 3.80, 'd': 3.55, 'c': 2.97, 'u': 2.81, 'p': 2.53, 'h': 2.39, 'm': 2.18, 'g': 2.03,
    'y': 1.97, 'b': 1.91, 'f': 1.67, 'k': 1.61, 'w': 1.51, 'v': 1.00, 'x': 0.26, 'z': 0.23,
    'j': 0.18, 'q': 0.17
}


wordDictionary = {chr(c): [] for c in range(ord('a'), ord('z')+1)}
wordDictionary2 = {chr(c): [] for c in range(ord('a'), ord('z')+1)}


# Game state
player_balance = 3
guess_num = 1
random_word = ""
previous_words = []


# Initialize dictionaries
def initializeWords():
    with open("3000 wordle words.txt", 'r') as words_file:
        for line in words_file:
            word = line.strip().lower()
            if len(word) == 5:
                wordDictionary[word[0]].append(word)


def initializeWords2():
    with open("words.txt", 'r') as words_file:
        for line in words_file:
            word = line.strip().lower()
            if len(word) == 5:
                wordDictionary2[word[0]].append(word)


def getWord():
    global random_word
    all_keys = list(wordDictionary.keys())
    random_letter = random.choice(all_keys)
    random_word = random.choice(wordDictionary[random_letter])


def good_or_bad_1st(guessWord, green_count, yellow_count, gray_count):
    score = (green_count * 7) + (yellow_count * 3.5) + (gray_count * 5)
    score += sum(letter_frequencies.get(c, 0) for c in guessWord)
    return grade_word(score)


def good_or_bad(guessWord, green_count, yellow_count):
    score = (green_count * 7) + (yellow_count * 3.5)
    score += sum(letter_frequencies.get(c, 0) for c in guessWord)
    return grade_word(score)


def grade_word(score):
    if score >= 71.14:
        return "Perfect Word"
    elif score >= 56.912:
        return "Great Word"
    elif score >= 42.684:
        return "Good Word"
    elif score >= 28.456:
        return "Bad Word"
    else:
        return "Horrendous Word"


# GUI Application
class WordleApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Wordle with Betting")
        self.balance = player_balance
        self.guess_num = 1
        self.previous_words = []


        self.setup_widgets()


    def setup_widgets(self):
        self.bet_label = tk.Label(self.root, text=f"Your balance: {self.balance}")
        self.bet_label.pack()


        self.bet_entry = tk.Entry(self.root)
        self.bet_entry.pack()
        self.bet_entry.insert(0, "Enter your bet")


        self.bet_button = tk.Button(self.root, text="Start Game", command=self.start_game)
        self.bet_button.pack()


        self.output = tk.Text(self.root, height=12, width=50, state='disabled', bg='black', fg='white')
        self.output.pack()


        self.word_entry = tk.Entry(self.root)
        self.word_entry.pack()
        self.word_entry.config(state='disabled')


        self.guess_button = tk.Button(self.root, text="Guess", command=self.process_guess)
        self.guess_button.pack()
        self.guess_button.config(state='disabled')


    def start_game(self):
        try:
            self.bet = int(self.bet_entry.get())
            if self.bet <= 0 or self.bet > self.balance:
                raise ValueError
        except ValueError:
            messagebox.showerror("Invalid Bet", "Enter a positive number within your balance.")
            return


        self.balance -= self.bet
        getWord()
        self.bet_label.config(text=f"Your balance: {self.balance}")
        self.output.config(state='normal')
        self.output.insert(tk.END, f"New game started! Make your {tryNumber[0]} guess:\n")
        self.output.config(state='disabled')
        self.word_entry.config(state='normal')
        self.guess_button.config(state='normal')


    def process_guess(self):
        guess = self.word_entry.get().lower()
        self.word_entry.delete(0, tk.END)


        if len(guess) != 5 or not guess.isalpha():
            messagebox.showwarning("Invalid Input", "Please enter a real 5-letter word.")
            return
        if guess not in wordDictionary2.get(guess[0], []):
            messagebox.showwarning("Unknown Word", "This word is not in our dictionary.")
            return
        if guess in self.previous_words:
            self.display(f"You already guessed {guess}.\n")
            return


        green_count = yellow_count = gray_count = 0
        feedback = ""


        for i, char in enumerate(guess):
            if char == random_word[i]:
                feedback += f"[{char.upper()}]"  # Green
                green_count += 1
            elif char in random_word:
                feedback += f"({char})"  # Yellow
                yellow_count += 1
            else:
                feedback += f"{char}"  # Gray
                gray_count += 1


        self.display(feedback + "\n")


        if guess == random_word:
            self.display(f"You guessed it! {words[self.guess_num - 1]}\n")
            self.balance += self.bet * 2
            self.bet_label.config(text=f"Your balance: {self.balance}")
            self.end_game(win=True)
            return


        if self.guess_num == 1:
            grade = good_or_bad_1st(guess, green_count, yellow_count, gray_count)
        else:
            grade = good_or_bad(guess, green_count, yellow_count)


        self.display(f"{grade}\n\n")


        self.previous_words.append(guess)
        self.guess_num += 1


        if self.guess_num > 6:
            self.display(f"Out of guesses. The word was: {random_word}\n")
            self.end_game(win=False)


    def end_game(self, win):
        if win and self.balance >= 10:
            messagebox.showinfo("Victory!", "You reached 10! You're the best Wordle player!")
            self.root.destroy()
        elif not win and self.balance <= 0:
            messagebox.showinfo("Game Over", "You lost! Try harder next time ;)")
            self.root.destroy()
        else:
            self.guess_button.config(state='disabled')
            self.word_entry.config(state='disabled')
            self.bet_entry.delete(0, tk.END)
            self.bet_entry.insert(0, "Enter your bet")
            self.guess_num = 1
            self.previous_words.clear()
            self.bet_button.config(state='normal')


    def display(self, text):
        self.output.config(state='normal')
        self.output.insert(tk.END, text)
        self.output.see(tk.END)
        self.output.config(state='disabled')


# Initialize and run the GUI
if __name__ == "__main__":
    initializeWords()
    initializeWords2()
    root = tk.Tk()
    app = WordleApp(root)
    root.mainloop()
