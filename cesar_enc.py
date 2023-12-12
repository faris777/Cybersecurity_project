import string

class Caesar:
    def __init__(self, message: str, key: int) -> None:
        self.message = message.lower()  # Corrected: Added parentheses to call lower()
        self.key = key
        self.alpha = string.ascii_lowercase

    def encryption(self) -> str:
        encrypted_message = ''
        for char in self.message:
            if char in self.alpha:  # Checking if the character is in the alphabet
                char_index = (self.alpha.index(char) + self.key) % 26
                encrypted_message += self.alpha[char_index]
            else:
                encrypted_message += char  # Keep non-alphabetic characters unchanged
        return encrypted_message    
    def decryption(self) -> str:
        decypted_message = ''
        enc_message = self.encryption()
        for char in enc_message:
            if char in self.alpha:
                char_index = (self.alpha.index(char) - self.key) % 26
                decypted_message += self.alpha[char_index]
            else:
                decypted_message += char
        return decypted_message
