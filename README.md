# Text_to_Morse

the project will complete the list:

- [x] text to morse code
- [x] morse code to text
- [x] the GUI

## text to morse

- use `.split("space")` fun split word from text
- if text have `,` or `.`: make it a group with the front word; in the back of `,`,`.` or normal str, add `space`^3; between the word, add `space`^4 (0 should use morse code)
- use class`Morse_code` package the fun

## morse code to text

- use regular expressions split the morse_word(word)，`re.split(r' {7}', the_morse_code)`, use `re.split(r' {3}', the_morse_code)` split the str of word
  > can't use `split("space^7")` fun split code from morse, the fun `split` will consider the `"space*7" = "space*1"`,
- every word's back should add a `space`

## the GUI

- [x] should complete the GUI sketch
- [x] the two button corresponds to the morse code to text/text to morse

# test code

hello, world.
`....   .   .-..   .-..   ---   --..--       .--   ---   .-.   .-..   -..   .-.-.-`
