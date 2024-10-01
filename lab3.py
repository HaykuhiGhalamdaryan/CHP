class Crypt:
    def __init__(self):
        self.alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        self.shuffled_alphabet = ['B', 'Z', 'K', 'P', 'R', 'G', 'A', 'L', 'M', 'S', 'C', 'H', 'E', 'V', 'J', 'I', 'D', 'U', 'O', 'N', 'T', 'F', 'Q', 'W', 'Y', 'X']

    def Encrypt(self, word):
        word = word.upper()
        encrypted_word = ""

        for i in range(len(word)):
            j = self.alphabet.index(word[i])
            encrypted_word += self.shuffled_alphabet[j]

        return f"Encrypt: {word} --> {encrypted_word}"

    def Decrypt(self, encrypted_word):
        encrypted_word = encrypted_word.upper()
        decrypted_word = ""

        for i in range(len(encrypted_word)):
            j = self.shuffled_alphabet.index(encrypted_word[i])
            decrypted_word += self.alphabet[j]

        return f"Decrypt: {encrypted_word} --> {decrypted_word}"

crypt = Crypt()
word = "HELLO"
encrypted_word = "ZMA"

print(crypt.Encrypt(word))
print(crypt.Decrypt(encrypted_word))