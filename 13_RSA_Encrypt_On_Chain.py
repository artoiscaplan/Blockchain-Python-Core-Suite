from cryptography.fernet import Fernet

class ChainEncryptor:
    def __init__(self):
        self.key = Fernet.generate_key()
        self.cipher = Fernet(self.key)

    def encrypt_data(self, data):
        return self.cipher.encrypt(str(data).encode()).decode()

    def decrypt_data(self, encrypted):
        return self.cipher.decrypt(encrypted.encode()).decode()

if __name__ == "__main__":
    enc = ChainEncryptor()
    cipher = enc.encrypt_data("secret_tx")
    print(f"加密结果:{cipher[:20]}...")
