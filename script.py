"""AUTHOR : OTI """
import subprocess
import sys 





# Define a dictionary for Morse code mapping
morse_code_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
    'Z': '--..',
    '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----'
 }

# Create a reverse dictionary to map Morse code back to characters
reverse_morse_code_dict = {v: k for k, v in morse_code_dict.items()}

### push to github nhnnhnhn
char = 'A'
morse_code = morse_code_dict[char]
decoded_char = reverse_morse_code_dict[morse_code]

print(f"{char} is encoded as {morse_code}")
print(f"{morse_code} is decoded as {decoded_char}")