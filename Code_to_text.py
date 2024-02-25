from Morse_code import morse_code_dic

class code_to_text:
    def __init__(self):
        self.morse_to_text = ""
        self.word_text = ""
    def the_text(self,the_morse_code):
        for code in the_morse_code:
            self.word_text = ""
            for i in word:
                if i in [",","."]:
                    if i == ".":
                        self.word_morse_code = self.word_morse_code + morse_code_dic[i] + " "*3
                    else:
                        self.word_morse_code = self.word_morse_code + morse_code_dic[i] + " "*3
                else:
                    self.morse_code = morse_code_dic[i.title()]
                    self.word_morse_code = self.word_morse_code + self.morse_code + " "*3
            self.text_to_morse = self.text_to_morse + self.word_morse_code + " "*4

