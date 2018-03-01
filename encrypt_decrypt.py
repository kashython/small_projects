'''

Encrypt a textual file by writing a function that will take an input a shift key, this will shift all the text characters
by that key, decrypt function will do the reverse and restore the text.

'''

def encrypt(file_path, shift_key):

    shift_key = int(shift_key)
    encrypted_text = ''

    with open(file_path, 'r') as file:
        text = file.read()

    for i in range(len(text)):
        encrypted_text += chr(ord(text[i]) + shift_key)

    with open(file_path, 'w') as file:
        file.write(encrypted_text)

    print("Encryption Successful")

def decrypt(shift_key):

    shift_key = int(shift_key)
    encrypted_text = ''

    with open(file_path, 'r') as file:
        text = file.read()

    for i in range(len(text)):
        encrypted_text += chr(ord(text[i]) - shift_key)

    with open(file_path, 'w') as file:
        file.write(encrypted_text)

    print("Decryption Successful")



file_path = 'encrypt_decrypt.txt'

while True:
    try:
        shift_key = input("Enter the Shift Key to Encrypt or Decrypt the file\n")
        int(shift_key)
        break
    except Exception:
        print("Please Enter an integer for Shift key\n")

e_or_d = input("Enter 'e' to encrypt and any other key to decrypt\n")
if 'e' in e_or_d:
    encrypt(file_path, shift_key)
else:
    decrypt(shift_key)
