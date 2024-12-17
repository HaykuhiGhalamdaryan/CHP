import math

class Cipher:
    def encrypt(self, text: str) -> str:
        raise NotImplementedError("Encrypt method must be implemented by subclasses.")

    def decrypt(self, cipher: str) -> str:
        raise NotImplementedError("Decrypt method must be implemented by subclasses.")


class CesarCipher(Cipher):
    def __init__(self, shift: int):
        self.shift = shift

    def encrypt(self, text: str) -> str:
        return ''.join(chr(ord(c) + self.shift) for c in text)

    def decrypt(self, cipher: str) -> str:
        return ''.join(chr(ord(c) - self.shift) for c in cipher)


class RowColumnCipher(Cipher):
    def _fill_square_matrix(self, text: str) -> list:
        n = math.ceil(math.sqrt(len(text)))
        matrix = [[' ' for _ in range(n)] for _ in range(n)]
        k = 0
        for i in range(n):
            for j in range(n):
                if k < len(text):
                    matrix[i][j] = text[k]
                    k += 1
        return matrix

    def _fill_square_matrix_decryption(self, text: str) -> list:
        n = math.ceil(math.sqrt(len(text)))
        matrix = [[' ' for _ in range(n)] for _ in range(n)]
        k = 0
        for j in range(n):
            for i in range(n):
                if k < len(text):
                    matrix[i][j] = text[k]
                    k += 1
        return matrix

    def _transpose_matrix(self, matrix: list) -> list:
        return list(map(list, zip(*matrix)))

    def encrypt(self, text: str) -> str:
        matrix = self._fill_square_matrix(text)
        transposed = self._transpose_matrix(matrix)
        return ''.join(''.join(row) for row in transposed)

    def decrypt(self, cipher: str) -> str:
        matrix = self._fill_square_matrix_decryption(cipher)
        return ''.join(''.join(row).strip() for row in matrix)


class DoubleCipher(Cipher):
    def __init__(self, cesar_shift: int):
        self.cesar_cipher = CesarCipher(cesar_shift)
        self.row_column_cipher = RowColumnCipher()

    def encrypt(self, text: str) -> str:
        cesar_encrypted = self.cesar_cipher.encrypt(text)
        return self.row_column_cipher.encrypt(cesar_encrypted)

    def decrypt(self, cipher: str) -> str:
        row_column_decrypted = self.row_column_cipher.decrypt(cipher)
        return self.cesar_cipher.decrypt(row_column_decrypted)


if __name__ == "__main__":
    text = input("Enter text: ")
    cesar_shift = int(input("Enter cesar shift: "))

    double_cipher = DoubleCipher(cesar_shift)

    encrypted_text = double_cipher.encrypt(text)
    print("Encrypted Text:", encrypted_text)

    decrypted_text = double_cipher.decrypt(encrypted_text)
    print("Decrypted Text:", decrypted_text)
