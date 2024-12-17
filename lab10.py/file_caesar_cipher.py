import argparse
import os

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

def process_file(file_path, shift, decrypt=False):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File {file_path} does not exist.")
    with open(file_path, 'r') as file:
        data = file.read()
    processed_data = caesar_cipher(data, shift, decrypt)
    output_file = f"{file_path}.{'decrypted' if decrypt else 'encrypted'}"
    with open(output_file, 'w') as file:
        file.write(processed_data)
    print(f"Output saved to {output_file}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="File Caesar Cipher Encryption/Decryption")
    parser.add_argument("filePath", help="Path to the file")
    parser.add_argument("shift", type=int, help="Shift value")
    parser.add_argument("--decrypt", action="store_true", help="Decrypt the file")
    args = parser.parse_args()

    process_file(args.filePath, args.shift, args.decrypt)
