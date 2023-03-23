import hashlib
from Crypto.Cipher import AES

# Pad the input text to a multiple of 16 bytes
input_text = input().encode('utf-8')
padded_input = input_text + b"\0" * (AES.block_size - len(input_text) % AES.block_size)

# Generate a 256-bit encryption key from a passphrase using SHA-256
key = hashlib.sha256("my secret passphrase".encode('utf-8')).digest()

# Create an AES cipher object with the key
cipher = AES.new(key, AES.MODE_ECB)

# Encrypt the padded input text
encrypted = cipher.encrypt(padded_input)

# Print the encrypted text in hexadecimal format
print(encrypted.hex())
