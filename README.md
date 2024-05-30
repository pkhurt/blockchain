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

# Understanding a blockchain
A blockchain is a sequential chain of records called blocks.
The blocks can contain transactions, files, or any other data.
These blocks are chained together using hashes.


