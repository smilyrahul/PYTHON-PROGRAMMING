def encrypt(text, shift):
    result = ""

    for char in text:
        if char.isalpha():
            ascii_offset = 65 if char.isupper() else 97
            result += chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
        else:
            result += char

    return result

def decrypt(text, shift):
    result = ""

    for char in text:
        if char.isalpha():
            ascii_offset = 65 if char.isupper() else 97
            result += chr((ord(char) - ascii_offset - shift) % 26 + ascii_offset)
        else:
            result += char

    return result

# Get user input
text = input("Enter the text to encrypt: ")
shift = int(input("Enter the shift value (1-5): "))
print()

# Encrypt the text
encrypted_text = encrypt(text, shift)
print("Encrypted text:", encrypted_text)

# Decrypt the text
decrypted_text = decrypt(encrypted_text, shift)
print("Decrypted text:", decrypted_text)
