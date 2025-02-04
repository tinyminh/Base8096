import string
import random

# Generate a set of 8096 unique characters for base8096 encoding
# For simplicity, I'll use a combination of printable ASCII characters and some Unicode characters to create a larger set
# You can adjust this set to your needs

CHARSET = ''.join(chr(i) for i in range(32, 8096 + 32))  # Characters from ASCII and extended Unicode

# Function to encode data into base8096
def base8096_encode(data):
    # Convert data to binary
    binary_data = ''.join(format(byte, '08b') for byte in data.encode('utf-8'))
    
    # Pad binary data to make its length a multiple of 13 (log2(8096) = 13)
    padding = (13 - len(binary_data) % 13) % 13
    binary_data = '0' * padding + binary_data

    # Split binary data into chunks of 13 bits and map to the custom charset
    encoded = []
    for i in range(0, len(binary_data), 13):
        chunk = binary_data[i:i+13]
        index = int(chunk, 2)
        encoded.append(CHARSET[index])

    return ''.join(encoded)

# Function to decode data from base8096
def base8096_decode(encoded_data):
    binary_data = ''
    
    # Map characters back to their binary representation
    for char in encoded_data:
        index = CHARSET.index(char)
        binary_data += format(index, '013b')  # 13-bit binary representation for each character

    # Convert binary data back to the original string
    decoded = ''
    for i in range(0, len(binary_data), 8):
        byte = binary_data[i:i+8]
        decoded += chr(int(byte, 2))

    return decoded

# Example usage
original_message = "Hello, this is a test message for base8096!"
encoded_message = base8096_encode(original_message)
decoded_message = base8096_decode(encoded_message)

print(f"Original: {original_message}")
print(f"Encoded: {encoded_message}")
print(f"Decoded: {decoded_message}")
