def encrypt_to_hex(username):
    username_bytes = username.encode('utf-8')

    hex_encrypted = username_bytes.hex()

    return hex_encrypted

username = input("Enter youiner username  : ")

encrypted_username = encrypt_to_hex(username)

print(f"Encrypted username : {username}")
print(f"Encreypted username : {encrypted_username}")