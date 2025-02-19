def encrypt_decrypt(text, shift_keys, ifdecrypt):
    result = []
    shift_keys = list(map(int, shift_keys.split()))
    key_length = len(shift_keys)
    
    for i, char in enumerate(text):
        if 32 <= ord(char) <= 126:
            shift = shift_keys[i % key_length]
            if ifdecrypt:
                shift = -shift
            new_char = chr((ord(char) - 32 + shift) % 95 + 32)
            result.append(new_char)
            print(f"{i} {char} {shift} {new_char}", end=' ')
        else:
            result.append(char)
            print(f"{i} {char} 0 {char}", end=' ')
    
    print("\n----------")
    return ''.join(result)

# Test the function
text = "Hello world"
shift_keys = "2 4 3 22 -5"
encrypted = encrypt_decrypt(text, shift_keys, False)
decrypted = encrypt_decrypt(encrypted, shift_keys, True)

print("Text:", text)
print("Shift keys:", shift_keys)
print("Cipher:", encrypted)
print("Decrypted text:", decrypted)
