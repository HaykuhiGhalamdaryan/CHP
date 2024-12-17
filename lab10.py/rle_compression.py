import argparse
import os

def rle_compress(data):
    compressed = []
    count = 1
    for i in range(1, len(data)):
        if data[i] == data[i - 1]:
            count += 1
        else:
            compressed.append(f"{data[i - 1]}{count}")
            count = 1
    compressed.append(f"{data[-1]}{count}")
    return ''.join(compressed)

def rle_decompress(data):
    decompressed = []
    i = 0
    while i < len(data):
        char = data[i]
        count = ''
        i += 1
        while i < len(data) and data[i].isdigit():
            count += data[i]
            i += 1
        decompressed.append(char * int(count))
    return ''.join(decompressed)

def process_file(file_path, compress=True):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File {file_path} does not exist.")
    with open(file_path, 'r') as file:
        data = file.read()
    processed_data = rle_compress(data) if compress else rle_decompress(data)
    output_file = f"{file_path}.{'compressed' if compress else 'decompressed'}"
    with open(output_file, 'w') as file:
        file.write(processed_data)
    print(f"Output saved to {output_file}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="RLE Compression/Decompression")
    parser.add_argument("filePath", help="Path to the file")
    parser.add_argument("--decompress", action="store_true", help="Decompress the file")
    args = parser.parse_args()

    process_file(args.filePath, not args.decompress)
