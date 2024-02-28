from Morse_code import morse_code_dic
import re

class code_to_text:
    def __init__(self):
        self.morse_to_text = ""
        self.word_text = ""
    def the_text(self,the_morse_code):
        for code in the_morse_code:
            self.word_text = ""
            the_morse_list = re.split(r' {3}',code)
            for morse in the_morse_list:
                for key, value in morse_code_dic.items():
                    if morse == value:
                        self.word_text += key
            self.morse_to_text = self.morse_to_text + self.word_text.title() + " "

