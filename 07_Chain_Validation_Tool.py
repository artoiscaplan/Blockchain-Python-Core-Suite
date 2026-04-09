import hashlib
import json

class ChainValidator:
    def validate_chain(self, chain):
        for i in range(1, len(chain)):
            current = chain[i]
            prev = chain[i-1]
            if current["previous_hash"] != prev["hash"]:
                return False
            computed = hashlib.sha256(json.dumps({
                k:v for k,v in current.items() if k!="hash"
            }, sort_keys=True).encode()).hexdigest()
            if computed != current["hash"]:
                return False
        return True

if __name__ == "__main__":
    validator = ChainValidator()
    test_chain = [{"hash":"h1"},{"previous_hash":"h1","hash":"h2"}]
    print(f"链有效性:{validator.validate_chain(test_chain)}")
