class RLE:
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
    
    def decode(self, encoded_message):
        decoded_message = ""
        i = 0
        
        while i < len(encoded_message):
            count_char = encoded_message[i]
            count = ord(count_char) 
            i += 1
            char = encoded_message[i]
            decoded_message += char * count  
            i += 1
            
        return decoded_message
    
message = ("AAAAAAAAAAAAAAAAAAAAAAABBBBCCCCCAB")
rle = RLE(message)

encoded_message = rle.encode()
print("Encoded Message:", encoded_message)

decoded_message = rle.decode(encoded_message)
print("Decoded Message:", decoded_message)