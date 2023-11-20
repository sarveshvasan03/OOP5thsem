def encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            # Determine if the character is uppercase or lowercase
            is_upper = char.isupper()
            
            # Apply the Caesar Cipher shift
            char_code = ord(char) + shift
            if is_upper:
                if char_code > ord('Z'):
                    char_code -= 26
            else:
                if char_code > ord('z'):
                    char_code -= 26

            encrypted_text += chr(char_code)
        else:
            # Preserve non-alphabetic characters
            encrypted_text += char

    return encrypted_text

def decrypt(encrypted_text, shift):
    # Reverses the Caesar Cipher shift to decrypt the text
    return encrypt(encrypted_text, -shift)

# Example usage:
original_text = "Hello, World!"
shift_value = 3

# Encryption
encrypted_result = encrypt(original_text, shift_value)
print("Encrypted:", encrypted_result)

# Decryption
decrypted_result = decrypt(encrypted_result, shift_value)
print("Decrypted:", decrypted_result)
