import string

def crypt(message, pas):
    if pas < 1 or pas > 9:
        return "Le pas doit être compris entre 1 et 9."

    encrypted_message = ''
    for char in message:
        if char.isalpha():
            if char.islower():
                encrypted_char = chr(((ord(char) - ord('a') + pas) % 26) + ord('a'))
            else:
                encrypted_char = chr(((ord(char) - ord('A') + pas) % 26) + ord('A'))
        else:
            encrypted_char = char
        encrypted_message += encrypted_char

    encrypted_message += str(pas) 
    return encrypted_message
message = input("Entrez le message à crypter : ")
pas = int(input("Entrez le pas (entre 1 et 9) : "))
message_crypte = crypt(message, pas)
print("Message crypté : ", message_crypte)
