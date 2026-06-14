# =========================
# blockchain.py (FINAL)
# =========================

import hashlib
import pickle

blockchain = []

def create_hash(model):
    return hashlib.sha256(pickle.dumps(model)).hexdigest()

def add_block(hash_value):
    block = {
        "index": len(blockchain),
        "hash": hash_value
    }
    blockchain.append(block)
    print("Block added:", block)