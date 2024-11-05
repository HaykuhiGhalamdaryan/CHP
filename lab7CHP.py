class Caesar:
    def __init__(self, shift):
        self.shift = shift
        self.alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'] 
        
    def encrypt_caesar(self, word):
        word = word.upper()
        encrypted_word = ""
        
        for i in word:
            original_index = self.alphabet.index(i)
            shifted_index = (original_index + self.shift) % len(self.alphabet)
            encrypted_word += self.alphabet[shifted_index]
            
        return encrypted_word
    
    def decrypt_caesar(self, encrypted_word):
        encrypted_word = encrypted_word.upper()
        decrypted_word = ""
        
        for i in encrypted_word:
            shifted_index = self.alphabet.index(i)
            original_index = (shifted_index - self.shift) % len(self.alphabet)
            decrypted_word += self.alphabet[original_index]
            
        return decrypted_word
    
class RowCol:
    def __init__(self, source_data):
        self.source_data = source_data
        self.num_columns = 3  

    def encrypt(self):
        encrypted_table = []
        for i in range(0, len(self.source_data), self.num_columns):
            row = []
            for char in self.source_data[i:i+self.num_columns]:
                row.append(char)
            encrypted_table.append(row)
            
        encrypted_string = ""
        for j in range(len(encrypted_table[0])): 
            for i in range(len(encrypted_table)):  
                if j < len(encrypted_table[i]):  
                    encrypted_string += encrypted_table[i][j]

        return encrypted_string

    def decrypt(self, encrypted_string):
        num_rows = (len(self.source_data) + self.num_columns - 1) // self.num_columns  
        decrypted_table = [[] for _ in range(num_rows)]
        
        index = 0
        for col in range(self.num_columns):
            for row in range(num_rows):
                if index < len(encrypted_string):
                    decrypted_table[row].append(encrypted_string[index])
                    index += 1

        decrypted_string = ""
        for row in decrypted_table:
            decrypted_string += ''.join(row)

        return decrypted_string

word = "HELLO"
    
caesar_crypt = Caesar(shift=3)
encrypted_word = caesar_crypt.encrypt_caesar(word)
print(f"Encrypt (Caesar): {word} --> {encrypted_word}")

row_col_crypt = RowCol(encrypted_word)
double_encrypted_word = row_col_crypt.encrypt()
print(f"Double Encrypt (Row Col): {encrypted_word} --> {double_encrypted_word}")

decrypted_word = row_col_crypt.decrypt(double_encrypted_word)
print(f"Decrypt (Row Col): {double_encrypted_word} --> {decrypted_word}")

double_decrypted_word = caesar_crypt.decrypt_caesar(decrypted_word)
print(f"Decrypt (Caesar): {decrypted_word} --> {double_decrypted_word}")