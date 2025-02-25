def block_cipher(text, key, op):
    if len(key) != 8:
        return "Error: Key must be exactly 8 characters"
    if op not in ['encrypt', 'decrypt']:
        return "Error: Invalid operation. Use 'encrypt' or 'decrypt'"

    if op == 'encrypt':
        text += '_' * (8 - len(text) % 8)
        return " ".join("{:02x}".format(ord(x) ^ ord(y)) for x, y in zip(text, key * (len(text) // 8) + key[:len(text) % 8])).upper()
    else:
        text = "".join(chr(int(x, 16)) for x in text.split())
        return "".join(chr(ord(x) ^ ord(y)) for x, y in zip(text, key * (len(text) // 8) + key[:len(text) % 8])).rstrip('_')


def main():
    text = input("")
    key = input("")
    operation = input("")
    print(block_cipher(text, key, operation))

if __name__ == "__main__":
    main()
