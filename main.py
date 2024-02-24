from Morse_code_table import morse_code_dic


#转换字符为摩斯密码
def the_morse_code(the_text):
    text_to_morse = ""
    for word in the_text:
        word_morse_code = ""
        for i in word:
            if i in [",","."]:
                if i == ",":
                    word_morse_code = word_morse_code + morse_code_dic[i] + '0000000'
                else:
                    word_morse_code = word_morse_code + morse_code_dic[i] + '000'
            else:
                morse_code = morse_code_dic[i.title()]
                word_morse_code = word_morse_code + morse_code + '000'
        text_to_morse = text_to_morse + word_morse_code + "0000"
    return text_to_morse



the_text = input("Enter the text you want to converts to morse code: ").split(" ")
the_morse = the_morse_code(the_text)

print(the_morse)

