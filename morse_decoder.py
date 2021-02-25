# morse_decoder.py
'''
Your task is to decrypt the secret message using the Morse code.
The message will consist of words with 3 spaces between them and 1 space between each letter of each word.
If the decrypted text starts with a letter then you'll have to print this letter in uppercase.
'''
morse = {'.-': 'a', '-...': 'b', '-.-.': 'c', '-..': 'd', '.': 'e', '..-.': 'f', '--.': 'g', '....': 'h', '..': 'i', '.---': 'j', '-.-': 'k', '.-..': 'l', '--': 'm', '-.': 'n', 
         '---': 'o', '.--.': 'p', '--.-': 'q', '.-.': 'r', '...': 's', '-': 't', '..-': 'u', '...-': 'v', '.--': 'w', '-..-': 'x', '-.--': 'y', '--..': 'z', '-----': '0', 
         '.----': '1', '..---': '2', '...--': '3', '....-': '4', '.....': '5', '-....': '6', '--...': '7', '---..': '8', '----.': '9'}

def morse_decoder(code: str) -> str:
    decoded = []
    for word in code.split('   '):
        decoded_word = []
        for letter in word.split(' '):
            if letter in morse:
                decoded_word.append(morse[letter])
        decoded.append(''.join(decoded_word))
    return ' '.join(decoded).capitalize()

assert morse_decoder("... --- -- .   - . -..- -") == "Some text"
assert morse_decoder("..--- ----- .---- ---..") == "2018"
assert morse_decoder(".. -   .-- .- ...   .-   --. --- --- -..   -.. .- -.--") == "It was a good day"
