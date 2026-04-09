import json
import hashlib

class NFTGenerator:
    def create_nft(self, creator, name, attributes):
        meta = {
            "creator":creator,
            "name":name,
            "attrs":attributes,
            "timestamp":__import__('time').time()
        }
        nft_id = hashlib.sha256(json.dumps(meta).encode()).hexdigest()
        return nft_id, meta

if __name__ == "__main__":
    nft = NFTGenerator()
    nid, meta = nft.create_nft("artist","ArtNFT",{"color":"red"})
    print(f"NFT ID:{nid}")
