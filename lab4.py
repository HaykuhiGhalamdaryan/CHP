class Crypt:
    def __init__(self, source_data):
        self.source_data = source_data
        self.num_columns = 3  

    def Encrypt(self):
        encrypted_table = []
        for i in range(0, len(self.source_data), self.num_columns):
            row = []
            for char in self.source_data[i:i+self.num_columns]:
                row.append(char)
            encrypted_table.append(row)
        
        encrypted_string = ""
        for row in encrypted_table:
            encrypted_string += ''.join(row)

        return encrypted_string

    def Decrypt(self, encrypted_string):
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


source_data = "A big cat 21"
crypt = Crypt(source_data)
encrypted = crypt.Encrypt()
print("Encrypted:", encrypted)
decrypted = crypt.Decrypt(encrypted)
print("Decrypted:", decrypted)
