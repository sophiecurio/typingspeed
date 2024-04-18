import tkinter as tk
import random

### CREATE WORDLIST

words = []

# wordlist taken from https://gist.github.com/deekayen/4148741#file-1-1000-txt
with open ("1-1000.txt", "r") as file:
    for line in file:
        line = line.strip("\n")
        words.append(line)


### Functions

score = 0

def next_word():
    word = random.choice(words)
    word_label.config(text=word)
    return word

def check_word(word):
    global score
    entered_word = entry.get()
    print(entered_word)
    print(f"{word} top")
    if entered_word == word:
        score += 1
        score_field.config(text=f"Score: {score}")
    else:
        score = score
    
def enter(item):
    global word
    check_word(word)
    word = next_word()
    entry.delete(0, 'end')

def count_down(count):
    timer.config(text=f"{count}")

    if count > 0:
        window.after(1000, count_down, count-1)
    else:
        word_label.config(text=f"You type {score} words per minute!")

### UI

window = tk.Tk()
window.title("Typing speedtest")
window.config(padx=20, pady=20)

# last_word = tk.Label(text="last word", font=("Arial", 16))
# last_word.grid(column=1, row=1)

word_label = tk.Label(text="The word will appear here.", font=("Arial", 16))
word_label.grid(column=2, row=1)

# following_word = tk.Label(text="next word", font=("Arial", 16))
# following_word.grid(column=3, row=1)

entry = tk.Entry(width=20)
entry.grid(column=2, row=2)

score_field = tk.Label(text=f"Score: {score}") 
score_field.grid(column=2, row=3)

timer = tk.Label(text="timer")
timer.grid(column=3, row=2)

# first word
word = next_word()
count_down(60)

# check word & select new word on each enter
window.bind('<Return>', enter)

window.mainloop()
