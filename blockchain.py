import hashlib
from urllib.parse import urlparse
import json
from time import time


class Blockchain(object):
    """
    This class is responsible for managing the blockchain by storing transactions and the functions to create new blocks.
    Constructor: 
        Creates two empty lists 
         1: to store our blockchain
         2: to store the transactions

    Block: Each Block has:
      - index
      - timestamp
      - list of transactions
      - hash of the previous block
    """
    def __init__(self):
        self.chain = []
        self.current_transactions = []
        self.nodes = set()  # register neighboring nodes

        # Genesis Block (very fist block)
        self.new_block(previous_hash=1, proof=100)

    def register_node(self, address: str = "Address of node") -> None:
        """
        Add a new node to the list of nodes
        :param address:
        :return:
        """
        parsed_url = urlparse(address)
        self.nodes.add(parsed_url.netloc)

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

    def proof_of_work(self, last_proof: int) -> str:
        """
        Takes the last_proof of the last block and returns the proof of the current block
        by running a proof of work algorithm. The proof of work algorithm will be solved
        in the valid_proof method. 
        General concept: The proof is a number that is difficult to find but easy to verify.
        
        :param last_proof: <int> Previous Proof of the previous block
        :return: <int> Current Proof of the current block
        """
        proof = 0
        while self.valid_proof(last_proof, proof) is False:
            proof += 1

        return proof

    @staticmethod
    def valid_proof(last_proof: int, proof: int) -> bool:
        """
        Validates the proof: Does hash(last_proof, proof) contain 4 leading zeros?
        Steps:
        - Attaching the last_proof and proof in a string and encode it to bytes
        - Hash the string with SHA-256
        - Check if the hash has 4 leading zeros

        :param last_proof: <int> Previous Proof
        :param proof: <int> Current Proof
        :return: <bool> True if correct, False if not.
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




