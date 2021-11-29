import hashlib

# print(hashlib.sha256("Sam Codes".encode()).hexdigest())

NOUNCE_LIMIT = 100000000000

# sets limit of proceeding zeros
# the more zeros, the more difficult it is to find the hash
zeros = 5

def mining(block_number, transactions, previous_hash):
    for nonce in range(NOUNCE_LIMIT):
        base_text = str(block_number) + transactions + previous_hash + str(nonce)
        hash_find = hashlib.sha256(base_text.encode()).hexdigest()
        if hash_find.startswith('0' * zeros):
            print(f"Found Hash with nonce: {nonce}")
            return hash_find
    return -1


# test data 
block_number = 55
transactions = "837492739vd837"
previous_hash = "8348762094us9"

mining(block_number, transactions, previous_hash)

combo_text = str(block_number) + transactions + previous_hash + str(88352)
print(hashlib.sha256(combo_text.encode()).hexdigest())