import hashlib
import json
from time import time

class Blockchain(object):
    """
    Class Blockchain

    Constructor: Creates an empty list

    Block: Each Block has:
      - index
      - timestamp
      - list of transactions
      - hash of the previous block
    """
    def __init__(self):
        self.chain = []
        self.current_transactions = []

        # Genesis Block (very fist block)
        self.new_block(previous_hash=1, proof=100)

    def new_block(self, proof: int, previous_hash: int = None):
        """
        Creates a new block and adds it to the chain
        """
        block = {
            "index": len(self.chain) + 1,
            "timestamp": time(),
            "transactions": self.current_transactions,
            "proof": proof,
            "previous_hash": previous_hash or self.hash(self.chain[-1])
        }

        # Reset current transaction list
        self.current_transactions = []

        self.chain.append(block)
        return block

    def new_transaction(self, sender: str, recipient: str, amount: int):
        """
        Adds a new transaction to the list of transactions to go into the next mined Block
        :param sender: <str> Address of the Sender
        :param recipient: <str> Address of the Recipient
        :param amount: <int> Amount
        :return: <int> The index of the Block that will hold this transaction
        """
        self.current_transactions.append({
            "sender": sender,
            "recipient": recipient,
            "amount": amount,
        })
        return self.last_block["index"] + 1

    def proof_of_work(self, last_proof):
        """

        :param last_proof:
        :return:
        """
        proof = 0
        while self.valid_proof(last_proof, proof) is False:
            proof += 1

        return proof

    @staticmethod
    def valid_proof(last_proof, proof):
        """
        Validates the proof: Does hash(last_proof, proof) contain 4 leading zeros?
        :param last_proof:
        :param proof:
        :return:
        """
        guess = f"{last_proof}{proof}".encode()
        guess_hash = hashlib.sha256(guess).hexdigest()
        valid_proof = guess_hash[:4] == "0000"

        return valid_proof

    @staticmethod
    def hash(block: dict) -> str:
        """
        Creates a SHA-256 hash of a block with source info of whole block string
        :param block: Block
        :return sha-256 str
        """
        block_string = json.dumps(block, sort_keys=True).encode()
        hash = hashlib.sha256(block_string).hexdigest()
        return hash

    @property
    def last_block(self):
        """
        Returns the last Block in the chain
        :return:
        """
        return self.chain[-1]
