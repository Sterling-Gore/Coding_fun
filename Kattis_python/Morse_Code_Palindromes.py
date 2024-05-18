MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----'}

sample = input()
morse_string = ''
for i in sample:
    if i.isalnum():
        i = i.upper()
        morse_string += MORSE_CODE_DICT[i]

answer = True
if len(morse_string) != 0:
    i = 0
    j = len(morse_string) - 1
    while i < j:
        if morse_string[i] != morse_string[j]:
            answer = False
            break
        i += 1
        j -= 1
else:
    answer = False

if answer == True:
    print(1)
else:
    print(0)
