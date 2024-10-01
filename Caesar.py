class Caesar:
    def __init__(self, shift):
        self.shift = shift
        self.alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        
    def encrypt(self, word):
        word = word.upper()
        encrypted_word = ""
        
        for i in word:
            original_index = self.alphabet.index(i)
            shifted_index = (original_index + self.shift) % len(self.alphabet)
            encrypted_word += self.alphabet[shifted_index]
            
        return f"Encrypt (Caesar): {word} --> {encrypted_word}"
    
    def decrypt(self, encrypted_word):
        encrypted_word = encrypted_word.upper()
        decrypted_word = ""
        
        for i in encrypted_word:
            shifted_index = self.alphabet.index(i)
            original_index = (shifted_index - self.shift) % len(self.alphabet)
            decrypted_word += self.alphabet[original_index]
            
        return f"Decrypt (Caesar): {encrypted_word} --> {decrypted_word}"
    
caesar_crypt = Caesar(shift=3)
word = "HELLO"
encrypted_word = caesar_crypt.encrypt(word)
decrypted_word = caesar_crypt.decrypt(encrypted_word.split(" --> ")[1]) 

print(encrypted_word)
print(decrypted_word)