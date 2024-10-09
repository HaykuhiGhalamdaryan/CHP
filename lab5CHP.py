class Crypt:
    def __init__(self, message):
        self.message = message
    
    def encode(self):
        encoded_message = ""
        i = 0
        
        while i <= len(self.message) - 1:
            count = 1
            char = self.message[i]
            j = i
            
            while j < len(self.message) - 1:
                if self.message[j] == self.message[j + 1]:
                    count += 1
                    j += 1
                else:
                    break
                
            encoded_message += chr(count) + char
            
            i = j + 1
            
        return encoded_message
    
message = ("AAAAAAAAAAAAAAAAAAAAAAABBBBCCCCCAB")
encoded = Crypt(message)
encoded_message = encoded.encode()
print(encoded_message)


