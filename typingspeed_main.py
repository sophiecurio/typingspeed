import tkinter as tk
import random

BG = "#152736"
FG = "#dae6f0"

### CREATE WORDLIST

words = []

# wordlist taken from https://gist.github.com/deekayen/4148741#file-1-1000-txt
with open ("1-1000.txt", "r") as file:
    for line in file:
        line = line.strip("\n")
        words.append(line)


### Functions

score = 0
# word_list = ["word1", "word2"]
def next_word():
    word = random.choice(words)
    word_list.append(word)

    word_label.config(text=word_list[-2])
    last_word.config(text=word_list[-3])
    following_word.config(text=word_list[-1])

    return word_list

def check_word(word):
    global score
    global last_word
    # need to remove the space from the end of the word
    entered_word = entry.get()[:-1]
    print(entered_word)
    print(f"{word} top")
    if entered_word == word:
        score += 1
        score_field.config(text=f"Score: {score}")
        last_word.config(fg="green")
    else:
        score = score
        last_word.config(fg="red")
    
def enter(item):
    global word_list
    check_word(word_list[-2])
    word_list = next_word()
    entry.delete(0, 'end')
    print(word_list)

def count_down(count):
    timer.config(text=f"{count}")

    if count > 0:
        window.after(1000, count_down, count-1)
    else:
        word_label.config(text=f"You type {score} words per minute!")

### UI

window = tk.Tk()
window.title("Typing speedtest")
window.geometry("600x200")
window.config(padx=20, pady=20, bg=BG)
window.grid_rowconfigure(2, weight=1)
window.grid_columnconfigure((0,1,2), uniform="equal")


last_word = tk.Label(text="last word", font=("Avenir", 26), bg=BG)
last_word.grid(column=0, row=1, sticky="n")

word_label = tk.Label(text="The word will appear here.", font=("Avenir", 30), bg=BG, fg=FG)
word_label.grid(column=1, row=1, sticky="n")

following_word = tk.Label(text="next word", font=("Avenir", 26), bg=BG, fg=FG)
following_word.grid(column=2, row=1, sticky="n")

entry = tk.Entry(width=20, bg=FG)
entry.grid(column=1, row=2)

score_field = tk.Label(text=f"Score: {score}",borderwidth=0, highlightthickness=0, font=("Avenir", 20), bg=BG, fg=FG) 
score_field.grid(column=1, row=3)

timer = tk.Label(text="timer", font=("Avenir", 20), bg=BG, fg=FG)
timer.grid(column=2, row=2)

# first word
word_list = ["", random.choice(words)]
word = next_word()
count_down(60)

# check word & select new word on each enter
window.bind('<space>', enter)

window.mainloop()
