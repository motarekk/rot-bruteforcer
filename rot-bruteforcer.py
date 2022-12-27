'''
Caesar/ROT Cipher Brute-Forcer
By: Mohamed Tarek
GitHub: https://github.com/motarekk
LinkedIn: https://www.linkedin.com/in/mohamed-tarek-159a821ba/
'''
import sys

#---- INPUT ----#

#take input from user
cipher_text = ''

for arg in ' '.join(sys.argv[1:]):
    cipher_text  = cipher_text + arg

cipher_text_arr = [''] * len(cipher_text)
    
for i in range(len(cipher_text)):
    cipher_text_arr[i] = cipher_text[i]

#----------------------------------------------#
#---- PROCESS ----#

#decipher function
def decipher(key, cipher_text):
    alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

    '''
    << Example >>
    key = 3
    len(alphabet) = 26
    shiftedArr = [4-26, 0-3]
    '''

    shifted_alphabet = [''] * len(alphabet)

    #fill shiftedArr = [3-26]
    for i in range(key, len(alphabet)):
        shifted_alphabet[i-key] = alphabet[i]

    shifted_alphabet[len(alphabet)-(key):] = alphabet[:key]

    #substitution
    deciphered = [''] * len(cipher_text)
    exists = False

    for i in range(len(cipher_text)):
        for j in range(len(shifted_alphabet)):
            if cipher_text[i].casefold() == shifted_alphabet[j].casefold():
                deciphered[i] = alphabet[j]
                exists = True
                break
            else:
                exists = False

            if not exists:
                deciphered[i] = cipher_text[i]

    #put the result in a string
    result = ''
    for i in range(len(deciphered)):
        result = result + deciphered[i]

    return result

#----------------------------------------------#
#---- OUTPUT ----#

#brute-force
for i in range(1, 26):
    print(str(i) + ":", end=" ")
    print(decipher(i, cipher_text_arr))
