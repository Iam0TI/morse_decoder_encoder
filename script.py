"""AUTHOR : OTI """
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

def morse_encoder():
    to_encode = input('ENTER THE WORD TO ENCODE : ').upper()
    encoded_list = []
    for chars in to_encode:
         for char in chars:
            if char in morse_code_dict.keys():
                encoded_list.append(morse_code_dict.get(char))
                print(morse_code_dict.get(char))
    encoded_str = ' '.join(encoded_list)
    print(f'THE word {to_encode} is decoded as {encoded_str}')

def morse_decoder():
    input_to_decode = input('ENTER THE WORD TO DECODE :')
    to_decode = input_to_decode.split()
    decoded_list = []
    for chars in to_decode:
         if chars in reverse_morse_code_dict.keys():
            decoded_list.append(reverse_morse_code_dict.get(chars))
    decoded_str = ' '.join(decoded_list)
    print(f'THE MORSE code  {to_decode} is decoded as {decoded_str}')    
