class LZ77:
    def __init__(self, window_size=20):
        self.window_size = window_size

    def compress(self, data):
        compressed_data = []
        i = 0

        while i < len(data):
            match_length = 0
            match_distance = 0
            search_start = max(0, i - self.window_size)

            for j in range(search_start, i):
                length = 0
                while (i + length < len(data) and data[j + length] == data[i + length]):
                    length += 1
                    if j + length >= i:
                        break
                if length > match_length:
                    match_length = length
                    match_distance = i - j
                    
            next_char = data[i + match_length] if i + match_length < len(data) else None    

            if match_length == 0:
                compressed_data.append((0, 0, data[i]))
                i += 1
            else:
                compressed_data.append((match_distance, match_length, next_char))
                i += match_length + 1

        return compressed_data

    def decompress(self, compressed_data):
        decompressed_data = []
        for distance, length, next_char in compressed_data:
            if distance == 0 and length == 0:
                decompressed_data.append(next_char)
            else:
                start = len(decompressed_data) - distance
                for _ in range(length):
                    decompressed_data.append(decompressed_data[start])
                    start += 1
                    
                if next_char is not None:
                    decompressed_data.append(next_char)   
                         
        return ''.join(decompressed_data)


if __name__ == "__main__":
    text = "hellooo"
    print(f"Original text: {text}")

    compressor = LZ77(window_size=10)

    compressed = compressor.compress(text)
    print(f"Compressed: {compressed}")

    decompressed = compressor.decompress(compressed)
    print(f"Decompressed: {decompressed}")

    print(f"Compression successful: {text == decompressed}")
