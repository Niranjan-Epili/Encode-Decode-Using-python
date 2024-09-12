from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import os
import streamlit as st

# Function to encrypt the username using AES
def encrypt_to_hex_aes(username, key):
    iv = os.urandom(16)
    cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    username_bytes = username.encode('utf-8')
    encrypted_bytes = encryptor.update(username_bytes) + encryptor.finalize()
    hex_encrypted = (iv + encrypted_bytes).hex()
    return hex_encrypted

# Function to decrypt the hex string back to the original username
def decrypt_from_hex_aes(hex_string, key):
    encrypted_bytes_with_iv = bytes.fromhex(hex_string)
    iv = encrypted_bytes_with_iv[:16]
    encrypted_bytes = encrypted_bytes_with_iv[16:]
    cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    decrypted_bytes = decryptor.update(encrypted_bytes) + decryptor.finalize()
    decrypted_username = decrypted_bytes.decode('utf-8')
    return decrypted_username

# Streamlit UI
st.title("Advanced Username Encryption and Decryption")

key = os.urandom(32)  # Generate a 32-byte (256-bit) key

username = st.text_input("Enter your username")

if username:
    encrypted_username = encrypt_to_hex_aes(username, key)
    st.write(f"Encrypted username (hex): {encrypted_username}")

    hex_string = st.text_input("Enter the encrypted hex string to decrypt")

    if hex_string:
        try:
            decrypted_username = decrypt_from_hex_aes(hex_string, key)
            st.write(f"Decrypted username: {decrypted_username}")
        except Exception as e:
            st.write(f"Error decrypting: {e}")
