from Morse_code import The_Morse_Code
from Code_to_text import code_to_text
from ASCII_Art import ascii_art
import tkinter
import re

# windows = tkinter.Tk()
# windows.title("Text to Morse")
# windows.minsize(width=500, height=500)
#
# windows.mainloop()

print(ascii_art)
is_go_on = True
while is_go_on:
    the_sele_fun = input("What do you want to do? (code/decode)\n")
    if the_sele_fun == "code":
        morse_code = The_Morse_Code()
        the_text = input("Enter the text you want to converts to morse code: ").split(" ")
        morse_code.the_morse_code(the_text)
        print(morse_code.text_to_morse)
        the_text = input("if you want to do it again: (Y or N)")
        if the_text == "N":
            is_go_on = False
    elif the_sele_fun == "decode":
        text = code_to_text()
        the_input_code = input("Enter the morse code you want to decode: ")
        the_code = re.split(r' {7}', the_input_code)
        text.the_text(the_code)
        print(text.morse_to_text)
        the_text = input("if you want to do it again: (Y or N)")
        if the_text == "N":
            is_go_on = False