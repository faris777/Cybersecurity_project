
def brute(enc_message: str):
    for shift in range(1, 26):
        decrypted_message = ''
        for i in enc_message:
            if i.isalpha():  # Check if the character is a letter
                temp = ord(i) - shift
                if i.islower():
                    if temp < 97:
                        temp += 26
                elif i.isupper():
                    if temp < 65:
                        temp += 26
                decrypted_message += chr(temp)
            else:
                decrypted_message += i  # Keep non-alphabetic characters unchanged
        print(f'The message with key {shift} is: {decrypted_message}')

# Example usage


brute('qhvrdfdghpb')
# m = 'hfrnboy'
# for i in m:
#     print(ord(i))