import hashlib
import time

class Block:
    def __init__(self, index, timestamp, previous_hash, data):
        self.index = index
        self.timestamp = timestamp
        self.previous_hash = previous_hash
        self.data = data
        self.nonce = 0
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        txt = f"{self.index}{self.timestamp}{self.previous_hash}{self.data}{self.nonce}"
        return hashlib.sha256(txt.encode()).hexdigest()

    def __str__(self):
        return f"Block #{self.index} [previous_hash: {self.previous_hash}, timestamp: {time.ctime(self.timestamp)}, data: {self.data}, hash: {self.hash}]"
