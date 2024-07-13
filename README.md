<p align="center" widht="100%">
<img src="./docu/blockchain_logo.jpeg" alt="logo image" style="width:30%;height:30%;">
</p>
<hr>

# blockchain
This project contains a straight-forward blockchain implementation using flask as UI
to operate with the Blockchain.
Tutorial on page: https://hackernoon.com/learn-blockchains-by-building-one-117428612f46

Structure:
```
├── blockchain.py
├── LICENSE
├── main.py
├── README.md
├── requirements.txt
└── test
    └── test_blockchain.py
```

## Start the blockchain:
`python3 main.py` -> starts a local server `127.0.0.1`.

### Overview of interfaces
```
└── 127.0.0.1:5000/
    ├── mine   --> Mines a block
    ├── new    --> Creates a new transaction using CURL
    └── chain  --> Shows the total blockchain
```

### Do a transaction
Use a curl POST command or POSTMAN to do a transaction:
`127.0.0.1:5000/new`
```commandline
curl -X POST -H "Content-Type: application/json" -d '{
 "sender": "d4ee26eee15148ee92c6cd394edd974e",
 "recipient": "someone-other-address",
 "amount": 5
}' "http://localhost:5000/transactions/new"
```

### Mine a new Block of transactions
Call this address in your browser to mine a new block of the blockchain:
`127.0.0.1:5000/mine`

### Overview of the blockchain and it's blocks
Call this address in your browser to see all the blocks that have been forged
in your blockchain.
`127.0.0.1:5000/chain`

# Understanding a blockchain and the code
A blockchain is a sequential chain of records called blocks. <br>
The blocks can contain transactions, files, or any other data. <br>
These blocks are chained together using hashes. <br>

## Blockchain Class
The main file is the `blockchain.py` file which defines the class `Blockchain`. 
The constructor creates two initial empty lists. One, to store our blockchain and another to store the transactions.

### How does a Block look like?
```
block = {
    'index': 1,
    'timestamp': 1506057125.900785,
    'transactions': [
        {
            'sender': "8527147fe1f5426f9dd545de4b27ee00",
            'recipient': "a77f5cdfa2934df3954a5c7c7da5df1f",
            'amount': 5,
        }
    ],
    'proof': 324984774000,
    'previous_hash': "2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824"
}
```

<b>The crucial detail is the previous_hash. This gives the blockchain immutability.</b>

### Transactions
A transaction is, as the name indicates a movement of value between a sender and a receiver.

### Proof of Work (PoW)
Blocks are created / mined using a proof of work algorithm. The main goal of a PoW is to find a number that solves a certain problem. The number should be difficult to find but very easy to verify by anyone in the blockchain network. 

#### Example
Let's assume that we look for a result of that <i>hash(x / y)</i> must end with 0. Something like this
```
hash(x / y) = a123gdj...0
```
For this task we set `x = 5`.

Now we iterate so long over `y` until we found a result hash that ends wit 0.

In Bitcoin this is called <b>hashcash algorithm</b>.

<hr>

<p align="center" widht="100%">
<img src="./docu/blockchain_logo.jpeg" alt="logo image" style="width:30%;height:30%;">
</p>