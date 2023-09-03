"""AUTHOR : OTI """
import subprocess



to_encode = input('ENTER THE WORD TO ENCODE : ').upper()

input_to_decode = input('ENTER THE WORD TO DECODE :')
to_decode = input_to_decode.split()
  
#print(f'{to_encode} first')
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

def morse_encoder(char_list):
    encoded_list = []
    for char in char_list:
         for chrr in char:
            if chrr in morse_code_dict.keys():
                encoded_list.append(morse_code_dict.get(chrr))
                print(morse_code_dict.get(chrr))
    encoded_str = ' '.join(encoded_list)
    print(f'THE word {char_list} is decoded as {encoded_str}')

def morse_decoder(char_list):
    decoded_list = []
    for char in char_list:
         if char in reverse_morse_code_dict.keys():
            decoded_list.append(reverse_morse_code_dict.get(char))
    decoded_str = ' '.join(decoded_list)
    print(f'THE MORSE code  {char_list} is decoded as {decoded_str}')    


morse_encoder(to_encode)
morse_decoder(to_decode)