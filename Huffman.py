import heapq
from collections import defaultdict, Counter

class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

def huffman_codes(text):
    freq = Counter(text)
    
    heap = [Node(char, freq) for char, freq in freq.items()]
    heapq.heapify(heap)
    
    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        merged = Node(None, left.freq + right.freq)
        merged.left = left
        merged.right = right
        heapq.heappush(heap, merged)
    
    root = heap[0]
    
    huffman_code = {}
    def generate_codes(node, current_code=""):
        if not node:
            return
        if node.char is not None:  
            huffman_code[node.char] = current_code
        generate_codes(node.left, current_code + "0")
        generate_codes(node.right, current_code + "1")
    
    generate_codes(root)
    return huffman_code, root

def encode_text(text, huffman_code):
    return ''.join(huffman_code[char] for char in text)

def decode_text(encoded_text, root):
    decoded_text = []
    current = root
    for bit in encoded_text:
        if bit == '0':
            current = current.left
        else:
            current = current.right
        if current.char is not None:  
            decoded_text.append(current.char)
            current = root
    return ''.join(decoded_text)

if __name__ == "__main__":
    text = "huffman coding example"
    print(f"Original text: {text}")
    
    huffman_code, root = huffman_codes(text)
    print(f"Huffman Codes: {huffman_code}")
    
    encoded_text = encode_text(text, huffman_code)
    print(f"Encoded text: {encoded_text}")
    
    decoded_text = decode_text(encoded_text, root)
    print(f"Decoded text: {decoded_text}")
