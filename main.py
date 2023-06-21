import keyword
from tkinter import *
from tkinter.ttk import *
from wordsList import random_words_list, get_random_word
import time

timer_is_on = False
word_len = 0
words = 0

def trigger_timer(event=None):
    global timer_is_on
    if not timer_is_on:
        start_timer(60)
    timer_is_on = True

def start_timer(count):
    if count == 0:
        cpm = word_len
        wpm = words
        upper_box.itemconfig(cpm_text, text=cpm)
        upper_box.itemconfig(wpm_text, text=wpm)
        upper_box.itemconfig(time_left, text=00)
        bottom_box.destroy()
    else:
        upper_box.itemconfig(time_left, text=count)
        window.after(1000, start_timer, count - 1)


def create_text():
    text_box = Text(f, width=50, height=20, wrap="word")

    text_box.insert(INSERT, f"{text_to_canvas[0]} ")
    for word in text_to_canvas[1:]:
        text_box.insert(END, f"{word} ")

    text_box.pack(expand=1, fill=BOTH)

    text_box.tag_add("word", "1.0", f"1.{len(text_to_canvas[0])}")
    text_box.tag_add("rest", f"1.{len(text_to_canvas[0])}", "end")

    text_box.tag_config("word", background="green", foreground="white", font=('Arial', 15))
    text_box.tag_config("rest", font=('Arial', 15))

    text_box.place(x=300, y=300, anchor=CENTER)


def right_word(event=None):
    global word_len, words
    word_from_word_list = text_to_canvas[0]
    user_word_catch = bottom_box.get()
    user_word = user_word_catch.strip(' ')
    if user_word == word_from_word_list:
        word_len = word_len + len(text_to_canvas.pop(0))
        words = words + 1
        text_to_canvas.append(get_random_word())
        create_text()
        bottom_box.delete(0, 'end')


window = Tk()
window.title('Typing speed test')
window.geometry('600x600')

style = Style()
style.configure('My.TFrame', background='#27374D')

f = Frame(window, width=600, height=600, style='My.TFrame')
f.grid(row=0, column=0, sticky="NW")
f.grid_propagate(0)
f.update()

upper_box = Canvas(f, width=400, height=50, background='#526D82')

upper_box.create_text(100, 25, text='Corrected CPM: ')
cpm_text = upper_box.create_text(155, 25, text='?')
r1 = upper_box.create_rectangle((144, 17, 166, 33), fill="white")
upper_box.tag_lower(r1, cpm_text)

upper_box.create_text(200, 25, text='WPM: ')
wpm_text = upper_box.create_text(222, 25, text='?')
r2 = upper_box.create_rectangle((212, 17, 232, 33), fill="white")
upper_box.tag_lower(r2, wpm_text)

upper_box.create_text(300, 25, text='Time left: ')
time_left = upper_box.create_text(335, 25, text='?')
r3 = upper_box.create_rectangle((325, 17, 345, 33), fill="white")
upper_box.tag_lower(r3, time_left)

upper_box.place(x=300, y=100, anchor=CENTER)

text_to_canvas = []
for word in random_words_list:
    text_to_canvas.append(word)

create_text()

bottom_box = Entry(f, justify=CENTER, font=('Arial', 20))
bottom_box.place(x=300, y=500, anchor=CENTER, width=400, height=50)

window.bind("<space>", right_word)
window.bind('<Key>', trigger_timer)
window.mainloop()
