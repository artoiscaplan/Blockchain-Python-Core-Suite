import hashlib
import hmac

class TransactionSigner:
    def __init__(self, private_key):
        self.private_key = private_key

    def sign_transaction(self, tx_data):
        tx_str = str(tx_data).encode()
        signature = hmac.new(self.private_key.encode(), tx_str, hashlib.sha256).hexdigest()
        return signature

    def verify_signature(self, tx_data, signature, public_key):
        tx_str = str(tx_data).encode()
        calc_sig = hmac.new(public_key.encode(), tx_str, hashlib.sha256).hexdigest()
        return calc_sig == signature

if __name__ == "__main__":
    signer = TransactionSigner("test_private_key")
    tx = {"from":"addr1","to":"addr2","amount":50}
    sig = signer.sign_transaction(tx)
    check = signer.verify_signature(tx, sig, "test_public_key")
    print(f"签名验证结果:{check}")
