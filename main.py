logo = """           
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
"""


def encrypt(p_text, k):
    cipher_text = ""
    for i in range(len(p_text)):
        char = p_text[i]
        cipher_text += chr((ord(char) + k - 97) % 26 + 97)
    print(f"Here's your encoded result: {cipher_text}")


def decrypt(c_text, k):
    cipher_text = ""
    for i in range(len(c_text)):
        char = c_text[i]
        cipher_text += chr((ord(char) - k - 97) % 26 + 97)
    print(f"Here's your decoded result: {cipher_text}")


flag = 'yes'
print(logo)
while flag == 'yes':
    choice = input("Type 'encode' to ENCRYPT and 'decode' to DECRYPT a message:\n").lower()
    text = input("Enter Plain text:\n").lower()
    key = int(input("Enter Key:\n"))
    print("Plain Text: " + text)
    print(f"Key: {key}")
    if choice == 'encode':
        encrypt(text, key)
    elif choice == 'decode':
        decrypt(text, key)
    flag = input("Enter 'yes' to repeat or 'no' to exit:\n")
