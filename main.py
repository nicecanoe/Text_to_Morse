from Morse_code import The_Morse_Code
from ASCII_Art import ascii_art
import tkinter

windows = tkinter.Tk()
windows.title("Text to Morse")
windows.minsize(width=500, height=500)

windows.mainloop()
#转换字符为摩斯密码


print(ascii_art)
is_go_on = True
while is_go_on:

    morse_code = The_Morse_Code()
    the_text = input("Enter the text you want to converts to morse code: ").split(" ")
    morse_code.the_morse_code(the_text)
    print(morse_code.text_to_morse)
    the_text = input("if you want to dio it again: (Y or N)")
    if the_text == "N":
        is_go_on = False