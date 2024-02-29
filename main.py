from Morse_code import The_Morse_Code
from Code_to_text import code_to_text
from ASCII_Art import ascii_art
import tkinter
import re

def generate_morse():
    morse_code = The_Morse_Code()
    the_text = the_text_input.get().split()
    morse_code.the_morse_code(the_text)
    the_morse_input.delete(0, tkinter.END)
    the_morse_input.insert(0,morse_code.text_to_morse)


def decode_morse():
    text = code_to_text()
    the_input_code = the_morse_input.get()
    the_code = re.split(r' {7}', the_input_code)
    text.the_text(the_code)
    the_text_input.delete(0, tkinter.END)
    the_text_input.insert(0,text.morse_to_text)




windows = tkinter.Tk()
windows.title("Text to Morse")
windows.config(padx=50,pady=50)

canvas = tkinter.Canvas(width=200, height=200,highlightthickness=0)
code_logo = tkinter.PhotoImage(file="logo.png")
canvas.create_image(100,100,image=code_logo)
canvas.grid(column=1,row=0)

#text plain
the_text_plain = tkinter.Label(text="TEXT")
the_text_plain.grid(column=0,row=1)

the_text_input = tkinter.Entry(width=21)
the_text_input.grid(column=1,row=1)

#morse code
the_morse = tkinter.Label(text="MORSE")
the_morse.grid(column=0,row=2)

the_morse_input = tkinter.Entry(width=21)
the_morse_input.grid(column=1,row=2)

#button
generate_morse_code = tkinter.Button(text="Generate Morse",command=generate_morse)
generate_morse_code.grid(row=1,column=2)
decode_morse_code = tkinter.Button(text="Decode Morse",command=decode_morse)
decode_morse_code .grid(row=2,column=2)

windows.mainloop()



