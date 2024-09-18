alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
shuffled_alphabet = ['B', 'Z', 'K', 'P', 'R', 'G', 'A', 'L', 'M', 'S', 'C', 'H', 'E', 'V', 'J', 'I', 'D', 'U', 'O', 'N', 'T', 'F', 'Q', 'W', 'Y', 'X']

def Encrypt(word):
    
    encrypted_word = ""
    
    for i in range(len(word)):
        j = alphabet.index(word[i])
        encrypted_word += shuffled_alphabet[j]
        
    return f"Encrypt: {word} --> {encrypted_word}"

def Decrypt(encrypted_word):
    
    decrypted_word = ""
    
    for i in range(len(encrypted_word)):
        j = shuffled_alphabet.index(encrypted_word[i])
        decrypted_word += alphabet[j]
        
    return f"Decrypt: {encrypted_word} --> {decrypted_word}"

word = "HELLO"
encrypted_word = "ZMA"

print(Encrypt(word))
print(Decrypt(encrypted_word))