from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
import os

class JsonEncryting:

    def __init__(self) -> None:
        self.key = "6e5fa3415403d7e245e17f2ae176fe62aae6907bde0a5f37c82530811287f7d9"
       
       

    def encrypt(self, data):
        backend = default_backend()
        iv = os.urandom(16)  # Initialization Vector
        cipher = Cipher(algorithms.AES(self.key), modes.CBC(iv), backend=backend)
        encryptor = cipher.encryptor()

        padder = padding.PKCS7(algorithms.AES.block_size).padder()
        data = padder.update(data.encode()) + padder.finalize()

        ciphertext = encryptor.update(data) + encryptor.finalize()
        return iv + ciphertext

    def decrypt(self, encrypted_data):
        backend = default_backend()
        iv = encrypted_data[:16]  # Extraemos el Initialization Vector
        ciphertext = encrypted_data[16:]

        cipher = Cipher(algorithms.AES(self.key), modes.CBC(iv), backend=backend)
        decryptor = cipher.decryptor()

        decrypted_data_padded = decryptor.update(ciphertext) + decryptor.finalize()
        unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder()
        decrypted_data = unpadder.update(decrypted_data_padded) + unpadder.finalize()

        return decrypted_data.decode()