import argparse

def caesar_cipher(text, shift, decrypt=False):
    if decrypt:
        shift = -shift
    result = []
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result.append(chr((ord(char) - base + shift) % 26 + base))
        else:
            result.append(char)
    return ''.join(result)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Caesar Cipher Encryption/Decryption")
    parser.add_argument("text", help="Text to encrypt/decrypt")
    parser.add_argument("shift", type=int, help="Shift value")
    parser.add_argument("--decrypt", action="store_true", help="Decrypt the text")
    args = parser.parse_args()

    output = caesar_cipher(args.text, args.shift, args.decrypt)
    print(output)
