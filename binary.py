def decimal_to_binary_chunks(decimal_num):
    binary_num = bin(decimal_num)[2:]  # Convert the decimal number to its binary representation
    chunk_size = 2
    binary_num = binary_num.zfill((len(binary_num) // chunk_size) * chunk_size + chunk_size)
    chunks = [binary_num[i:i + chunk_size] for i in range(0, len(binary_num), chunk_size)]
    return chunks

# Example usage:
decimal_num = int(input("Enter a decimal number: "))
binary_chunks = decimal_to_binary_chunks(decimal_num)
print(f"The binary representation of {decimal_num} in chunks is:")
print(" ".join(binary_chunks))
