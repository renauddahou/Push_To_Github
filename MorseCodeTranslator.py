MORSE_CODE_DICT = {'A':'.-','B':'-...', 'C':'-.-.', 'D':'-..', 'E':'.',
'F':'..-.', 'G':'--.', 'H':'....','I':'..', 'J':'.---', 'K':'-.-',
'L':'.-..', 'M':'--', 'N':'-.','O':'---', 'P':'.--.', 'Q':'--.-','R':'.-.', 'S':'...', 'T':'-',
'U':'..-', 'V':'...-', 'W':'.--','X':'-..-', 'Y':'-.--', 'Z':'--..','1':'.----', '2':'..---', '3':'...--',
'4':'....-', '5':'.....', '6':'-....','7':'--...', '8':'---..', '9':'----.','0':'-----', ', ':'--..--', '.':'.-.-.-',
'?':'..--..', '/':'-..-.', '-':'-....-','(':'-.--.', ')':'-.--.-'}
def morse_it(string, MORSE_CODE_DICT):
    string = string.upper()
    for letter in string:
        if letter in MORSE_CODE_DICT.keys():
            print(MORSE_CODE_DICT[letter])
        elif letter == " ":
            print(" ")
        else:
            print(f'the {letter} key does not exist in our dictionary')
string = input("Enter something to print out morse code:  ")
morse_it(string, MORSE_CODE_DICT)