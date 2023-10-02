import string

def crypt(message):
    encrypted_message = ''
    for char in message:
        if char.isalpha():
            if char.islower():
                encrypted_char = chr(((ord(char) - ord('a') + 1) % 26) + ord('a'))
            else:
                encrypted_char = chr(((ord(char) - ord('A') + 1) % 26) + ord('A'))
        else:
            encrypted_char = char
        encrypted_message += encrypted_char
    return encrypted_message

# Demander à l'utilisateur de saisir un message à crypter
message = input("Entrez le message à crypter : ")

# Crypter le message
message_crypte = crypt(message)

# Afficher le message crypté
print("Message crypté : ", message_crypte)
