import unittest
import hashlib
import json
from blockchain import Blockchain


class TestBlockchainMethods(unittest.TestCase):
    def setUp(self):
        self.blockchain = Blockchain()
        self.sender = "Santa Carlos"
        self.recipient = "Fernando"
        self.amount = 3

        self.proof = 100
        self.previous_hash = 1

    def test_genesis_block(self):
        """
        Tests the initial block of the blockchain
        """
        genesis_block = self.blockchain.last_block["index"]
        self.assertEqual(genesis_block, 1)

    def test_new_transaction_return_type(self):
        """
        return type of a transaction must be integer
        """
        transaction = self.blockchain.new_transaction(self.sender, self.recipient, self.amount)
        self.assertIsInstance(transaction, int)

    def test_new_transaction_properties_current_transactions(self):
        """
        A new transaction must have the correct properties "sender", "recipient" and "amount"
        """
        self.blockchain.new_transaction(self.sender, self.recipient, self.amount)
        self.assertEqual(self.blockchain.current_transactions[0]["sender"], self.sender)
        self.assertEqual(self.blockchain.current_transactions[0]["recipient"], self.recipient)
        self.assertEqual(self.blockchain.current_transactions[0]["amount"], self.amount)

    def test_new_block_return_type(self):
        """
        return type of function new_block(proof, previous_hash) must be dict
        """
        block = self.blockchain.new_block(self.proof, self.previous_hash)
        self.assertIsInstance(block, dict)

    def test_hash_sha256(self):
        """
        the created hash in blockchain.hash(block) from a block must be a valid hash (sha_256)
        """
        block = self.blockchain.new_block(self.proof, self.previous_hash)
        hash_ = self.blockchain.hash(block)

        self.assertIsInstance(hash_, str)
        self.assertEqual(hashlib.sha256(json.dumps(block, sort_keys=True).encode()).hexdigest(), hash_)

    def test_proof_of_work_leading_zeros(self):
        """
        tests the proof of work for 4 leading zeros started at proof 100. Next must be 35293.
        """
        proof_assumption = self.blockchain.proof_of_work(self.proof)
        self.assertIsInstance(proof_assumption, int)
        self.assertEqual(proof_assumption, 35293)


if __name__ == '__main__':
    unittest.main()
