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

    def new_block(self):
        """
        Creates a new block and adds it to the chain
        """
        pass

    def new_transaction(self):
        """
        Adds a new transaction to the list of transactions
        """
        pass

    @staticmethod
    def hash(block):
        """
        Hashes a block
        :param block:
        """
        pass

    @property
    def last_block(self):
        """
        Returns the last Block in the chain
        :return:
        """
        pass