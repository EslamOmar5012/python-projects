alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

print(r"""           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
""")


def encode(plainText, shift):
    plainText = list(plainText)
    for i in range(len(plainText)):
        if plainText[i] in alphabet:
            idx = alphabet.index(plainText[i])
            idx += shift
            idx %= 26
            plainText[i] = alphabet[idx]
    cipher = ''.join(plainText)
    return cipher

def decode(cipher, shift):
    cipher = list(cipher)
    for i in range(len(cipher)):
        if cipher[i] in alphabet:
            idx = alphabet.index(cipher[i])
            idx -= shift
            idx %= 26
            cipher[i] = alphabet[idx]
    plainText = ''.join(cipher)
    return plainText


while True:
    choice = input("Type 'encode' to encrypt, type 'decode' to decrypt: ").lower()
    if choice == 'encode':
        plainText = input("Type your message:\n").lower()
        shift = int(input("Type the shift number: "))
        cipher = encode(plainText, shift)
        print("Here's the encoded result: " + cipher)
    elif choice == "decode":
        cipher = input("Type your message:\n").lower()
        shift = int(input("Type the shift number: "))
        plainText = decode(cipher, shift)
        print("Here's the encoded result: " + plainText)
    else:
        print("wrong answer please type the words right!")

    cont = input("Do you want to continue (y/n): ").lower()

    if cont != 'y':
        break