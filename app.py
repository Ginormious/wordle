import tkinter as tk
import random

# Load word dictionaries
wordDictionary = {chr(i): [] for i in range(97,123)}
wordDictionary2 = {chr(i): [] for i in range(97,123)}
with open("3000 wordle words.txt", 'r') as words:
    for word in words:
        word = word.strip().lower()
        wordDictionary[word[0]].append(word)
with open("words.txt", 'r') as words:
    for word in words:
        word = word.strip().lower()
        wordDictionary2[word[0]].append(word)

# Initial variables
words = ['Genius', 'Magnificent', 'Impressive', 'Splendid', 'Great', 'Phew']
player_balance = 3
tiles = []
guessNum = 0
current_guess = ""
keyboard_buttons = {}

# Main window
root = tk.Tk()
root.title("Wordle Bet Game")
root.config(bg="#1e1e1e")

# Frames
bet_frame = tk.Frame(root, bg="#1e1e1e")
game_frame = tk.Frame(root, bg="#1e1e1e")

# Bet UI
bet_label = tk.Label(bet_frame, text="Enter your bet:", font=("Helvetica", 14), fg="white", bg="#1e1e1e")
bet_label.pack(pady=5)
bet_entry = tk.Entry(bet_frame, font=("Helvetica", 14))
bet_entry.pack()
balance_label = tk.Label(bet_frame, text=f"Your balance: {player_balance}", font=("Helvetica", 16), fg="yellow", bg="#1e1e1e")
balance_label.pack(pady=5)
bet_msg = tk.Label(bet_frame, text="", font=("Helvetica", 12), fg="red", bg="#1e1e1e")
bet_msg.pack()
bet_button = tk.Button(bet_frame, text="Place Bet", font=("Helvetica", 14), command=lambda: validate_bet())
bet_button.pack(pady=10)
bet_frame.pack()

# Game UI setup
msg = tk.Label(game_frame, text="", font=("Helvetica", 14), bg="#1e1e1e", fg="white")
msg.pack(pady=5)

game_balance_label = tk.Label(game_frame, font=("Helvetica", 14), bg="#1e1e1e", fg="lightgreen")
game_balance_label.pack()

guess_frame = tk.Frame(game_frame, bg="#1e1e1e")
guess_frame.pack(pady=10)

kb_frame = tk.Frame(game_frame, bg="#1e1e1e")
kb_frame.pack()

enter_btn = tk.Button(game_frame, text="Enter", width=10, height=2, bg="green", fg="white", command=lambda: submit_guess())
enter_btn.pack(pady=10)

def create_grid():
    for row in range(6):
        row_tiles = []
        for col in range(5):
            tile = tk.Label(guess_frame, text="", width=4, height=2, font=("Helvetica", 24), bg="white", relief="solid", borderwidth=1)
            tile.grid(row=row, column=col, padx=4, pady=4)
            row_tiles.append(tile)
        tiles.append(row_tiles)

def create_keyboard():
    keys = ["QWERTYUIOP", "ASDFGHJKL", "ZXCVBNM"]
    for row_keys in keys:
        row = tk.Frame(kb_frame, bg="#1e1e1e")
        row.pack()
        for key in row_keys:
            btn = tk.Button(row, text=key, width=4, height=2, bg="gray", fg="white", font=("Helvetica", 14),command=lambda k=key: on_key_press(k))
            btn.pack(side="left", padx=2, pady=2)
            keyboard_buttons[key] = btn

def on_key_press(letter):
    global current_guess
    if len(current_guess) < 5:
        current_guess += letter.lower()
        update_tiles()

def update_tiles():
    for i in range(5):
        tiles[guessNum][i]['text'] = current_guess[i].upper() if i < len(current_guess) else ""

def good_or_bad(green_count, yellow_count):
    score = (green_count * 10) + (yellow_count * 8)
    if score >= 92.8:
        msg["text"] = "Perfect Word"
    elif score >= 74.24:
        msg["text"] = "Great word"
    elif score >= 55.68:
        msg["text"] = "Good Word"
    elif score >= 37.12:
        msg["text"] = "Bad Word"
    elif score >= 18.5:
        msg["text"] = "Horrendous word"

def submit_guess():
    global guessNum, current_guess, random_word, player_balance
    if len(current_guess) != 5 or current_guess not in wordDictionary2[current_guess[0]]:
        msg["text"] = "Invalid word!"
        return

    green_count = 0
    yellow_count = 0
    for i in range(5):
        if current_guess[i] == random_word[i]:
            tiles[guessNum][i]['bg'] = "green"
            green_count += 1
        elif current_guess[i] in random_word:
            tiles[guessNum][i]['bg'] = "gold"
            yellow_count += 1
        else:
            tiles[guessNum][i]['bg'] = "gray"

    good_or_bad(green_count, yellow_count)

    if current_guess == random_word:
        msg["text"] = words[guessNum]
        player_balance += bet_amount * 2
    else:
        player_balance -= bet_amount

    game_balance_label["text"] = f"Balance: {player_balance}"
    if player_balance <= 0:
        msg["text"] = "You lost! Game over."
        disable_input()
    elif player_balance >= 7:
        msg["text"] = "You won! You're amazing 🎉"
        disable_input()

    guessNum += 1
    current_guess = ""

def disable_input():
    for btn in keyboard_buttons.values():
        btn['state'] = 'disabled'
    enter_btn['state'] = 'disabled'

def validate_bet():
    global bet_amount, random_word
    try:
        val = int(bet_entry.get())
        if val <= 0:
            bet_msg["text"] = "Enter a positive bet."
        elif val > player_balance:
            bet_msg["text"] = "You're too poor lol."
        else:
            bet_amount = val
            bet_msg["text"] = ""
            random_word = random.choice(random.choice(list(wordDictionary.values())))
            bet_frame.pack_forget()
            game_balance_label["text"] = f"Balance: {player_balance}"
            game_frame.pack()
            create_grid()
            create_keyboard()
    except ValueError:
        bet_msg["text"] = "Enter a valid integer."

root.mainloop()