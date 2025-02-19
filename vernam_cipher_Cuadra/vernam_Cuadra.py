# JUST SUBMIT ONE (2) FILES, vernam_lastname.py test_vernam_lastname.py
import random

def text_to_decimal(text: str) -> str:
    """Convert text to 3-digit decimal ASCII values with leading zeros"""
    return "".join((str(ord(char)).zfill(3) for char in text))

def decimal_to_text(decimal_str: str) -> str:
    """Convert 3-digit decimal string back to text"""
    return "".join(chr(int(decimal_str[i:i+3])) for i in range(0, len(decimal_str), 3))

def generate_key(length: int) -> str:
    """Generate random numeric key of specified length"""
    return "".join(str(random.randint(0, 9)) for _ in range(length))

def vernam_encrypt(plaintext_dec: str, key_dec: str) -> str:
    """Encrypt decimal plaintext using Vernam cipher"""
    if len(plaintext_dec) != len(key_dec):
        raise ValueError("Key length must match plaintext length")
    return "".join(str((int(p) + int(k)) % 10) for p, k in zip(plaintext_dec, key_dec))

def vernam_decrypt(ciphertext_dec: str, key_dec: str) -> str:
    """Decrypt decimal ciphertext using Vernam cipher"""
    if len(ciphertext_dec) != len(key_dec):
        raise ValueError("Key length must match ciphertext length")
    return "".join(str((int(c) - int(k)) % 10) for c, k in zip(ciphertext_dec, key_dec))

plaintext = "HELLO WORLD"

# Convert text to decimal string
decimal_plain = text_to_decimal(plaintext) 

# Generate matching key
key = generate_key(len(decimal_plain))

# Encrypt
ciphertext = vernam_encrypt(decimal_plain, key)

# Decrypt
decrypted_decimal = vernam_decrypt(ciphertext, key)
decrypted_text = decimal_to_text(decrypted_decimal)

print("plaintext\t",plaintext)
print("plaintext(dec)\t",decimal_plain)
print("Ciphertext\t",ciphertext)
print("Random Key\t",key)
print("Decrypted(dec)\t",decrypted_decimal)
print("Decrypted Text\t",decrypted_text)
