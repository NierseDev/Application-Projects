def vigenere_encrypt(plaintext, key, alphabet):
    # Validate alphabet
    if len(alphabet) < 1:
        raise ValueError("Alphabet must contain at least one character")
    if len(alphabet) != len(set(alphabet)):
        raise ValueError("Alphabet must contain only unique characters")

    # Validate key
    if len(key) == 0:
        raise ValueError("Key cannot be an empty string")
    
    # Validate input
    invalid_chars_plaintext = [c for c in plaintext if c not in alphabet]
    invalid_chars_key = [c for c in key if c not in alphabet]
    
    if len(invalid_chars_plaintext) > 0 or len(invalid_chars_key) > 0:
        raise ValueError(f"Invalid characters!\nin plaintext: {', '.join(invalid_chars_plaintext)}\nin keys: {', '.join(invalid_chars_key)}\nare not in alphabet")

    # Encrypt
    ciphertext = ""
    for i, c in enumerate(plaintext):
        key_char = key[i % len(key)]
        ciphertext_char = alphabet[(alphabet.index(c) + alphabet.index(key_char)) % len(alphabet)]
        ciphertext += ciphertext_char
    
    return ciphertext


