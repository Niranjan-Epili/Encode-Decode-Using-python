def decrypt_from_hex(hex_string):
    # Convert the hexadecimal string back to bytes
    decrypted_bytes = bytes.fromhex(hex_string)
    
    # Convert bytes back to the original string using UTF-8 decoding
    decrypted_username = decrypted_bytes.decode('utf-8')
    
    return decrypted_username

# Get the hexadecimal string input from the user
hex_string = input("Enter the hexadecimal string to decode: ")

# Decrypt the hexadecimal string back to the original username
decrypted_username = decrypt_from_hex(hex_string)

# Display the decrypted username
print(f"Decrypted username: {decrypted_username}")