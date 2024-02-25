morse_code_dic = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
    'Z': '--..',

    '0': '-----', '1': '.----', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....', '7': '--...',
    '8': '---..', '9': '----.',

    ',': '--..--', '.': '.-.-.-',
}

class The_Morse_Code:
    def __init__(self):
        self.text_to_morse = ""
        self.word_morse_code = ""
    def the_morse_code(self,the_text):
        for word in the_text:
            self.word_morse_code = ""
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

