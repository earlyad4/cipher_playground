# Vigenere Cipher Demo
def vigenere(message, key, direction=1):
    key_index = 0
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    final_message = ''
    key = key.lower()

    for char in message.lower():
        if not char.isalpha():
            final_message += char
        else:
            key_char = key[key_index % len(key)]
            key_index += 1
            offset = alphabet.index(key_char)
            index = alphabet.index(char)
            new_index = (index + offset * direction) % len(alphabet)
            final_message += alphabet[new_index]
    return final_message

def encrypt(message, key):
    return vigenere(message, key)

def decrypt(message, key):
    return vigenere(message, key, -1)

# Demo with a sample
sample_text = "this is a secret"
custom_key = "python"

print("=== Vigenere Cipher Demo ===")
print(f"Plaintext: {sample_text}")
print(f"Key: {custom_key}")

encrypted = encrypt(sample_text, custom_key)
decrypted = decrypt(encrypted, custom_key)

print(f"Encrypted: {encrypted}")
print(f"Decrypted: {decrypted}")

# Now let the user try
print("\nNow it’s your turn.")
user_phrase = input("Enter a phrase to encrypt: ")
user_key = input("Enter a key: ")

user_encrypted = encrypt(user_phrase, user_key)
user_decrypted = decrypt(user_encrypted, user_key)

print(f"\nYour phrase: {user_phrase}")
print(f"Key: {user_key}")
print(f"Encrypted: {user_encrypted}")
print(f"Decrypted back: {user_decrypted}")
