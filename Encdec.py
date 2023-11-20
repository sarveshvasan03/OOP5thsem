def encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            is_upper = char.isupper()
            char_code = ord(char) + shift
            if is_upper:
                if char_code > ord('Z'):
                    char_code -= 26
            else:
                if char_code > ord('z'):
                    char_code -= 26

            encrypted_text += chr(char_code)
        else:
            encrypted_text += char

    return encrypted_text

def decrypt(encrypted_text, shift):
    return encrypt(encrypted_text, -shift)
original_text = "Hello, World!"
shift_value = 3
encrypted_result = encrypt(original_text, shift_value)
print("Encrypted:", encrypted_result)
decrypted_result = decrypt(encrypted_result, shift_value)
print("Decrypted:", decrypted_result)
