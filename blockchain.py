import time
from block import Block

class Blockchain:
    def __init__(self, difficulty):
        self.difficulty = difficulty
        self.blocks = []
        genesis_block = Block(0, int(time.time()), "0", "Genesis Block")
        genesis_block.nonce = 0
        genesis_block.hash = genesis_block.calculate_hash()
        self.blocks.append(genesis_block)

    def new_block(self, data):
        latest_block = self.get_latest_block()
        return Block(latest_block.index + 1, int(time.time()), latest_block.hash, data)

    def get_latest_block(self):
        return self.blocks[-1]

    def add_block(self, new_block):
        new_block.nonce = 0
        new_block.hash = new_block.calculate_hash()
        self.blocks.append(new_block)

    def is_blockchain_valid(self):
        if not self.is_first_block_valid():
            return False
        for i in range(1, len(self.blocks)):
            current_block = self.blocks[i]
            previous_block = self.blocks[i - 1]
            if not self.is_valid_new_block(current_block, previous_block):
                return False
        return True

    def is_first_block_valid(self):
        first_block = self.blocks[0]
        if first_block.index != 0:
            return False
        if first_block.previous_hash != "0":
            return False
        if first_block.calculate_hash() != first_block.hash:
            return False
        return True

    def is_valid_new_block(self, new_block, previous_block):
        if previous_block.index + 1 != new_block.index:
            return False
        if previous_block.hash != new_block.previous_hash:
            return False
        if new_block.calculate_hash() != new_block.hash:
            return False
        return True

    def __str__(self):
        return "\n".join([str(block) for block in self.blocks])
