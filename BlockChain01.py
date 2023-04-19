import hashlib

class Block:
    def __init__(self, index, time, data, prev_hash):
        self.index = index
        self.time = time
        self.data = data
        self.prev_hash = prev_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        hash_data = str(self.index) + str(self.time) + str(self.data) + str(self.prev_hash)
        return hashlib.sha256(hash_data.encode()).hexdigest()


class BlockChain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]
    
    def create_genesis_block(self):
        return Block(0, "01/01/2023", "Genesis Block", "0")

    def get_latest_block(self):
        return self.chain[-1]
    
    def add_block(self, new_block):
        new_block.prev_hash = self.get_latest_block().hash
        new_block.hash = new_block.calculate_hash()
        self.chain.append(new_block)

    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            prev_block = self.chain[i-1]
            print('Current Block: ', i)
            if current_block.hash != current_block.calculate_hash():
                print('BAD BlockChain')
                return False
            if current_block.prev_hash != prev_block.hash:
                print('BAD BlockChain')
                return False

        print('BlockChain is Right !!!')
        return True

    def show_chain(self):
        for b in self.chain:
            print('--------------------------------------------------------------------')
            print("Index: ", b.index)
            print("Time: ", b.time)
            print("Data: ", b.data)
            print("Hash: ", b.hash)
            print("Prev_hash: ", b.prev_hash)




##############################
b1 = Block(1, "02/01/2023", "Block 1", "0")
b2 = Block(2, "03/01/2023", "Block 2", "0")
b3 = Block(3, "04/01/2023", "Block 3", "0")

evil_block = Block(2, "05/01/2023", "Block 2", "58eab12a22a28beb5c09d771f1dddce8c9bfe7767843bcb4d83286f8c3b96d01")



BC = BlockChain()
BC.add_block(b1)
BC.add_block(b2)
BC.add_block(b3)
BC.show_chain()
BC.is_chain_valid()

BC.chain[2] = evil_block
print(BC.show_chain())
BC.is_chain_valid()

