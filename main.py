import uuid
import json
from textwrap import dedent
import hashlib
from flask import Flask, jsonify, request
from blockchain import Blockchain


# Using Flask as API to communicate with Blockchain
app = Flask(__name__)

# Unique address for node
node_identifier = str(uuid.uuid4()).replace("-", "")

# instantiate Blockchain
blockchain = Blockchain()


# ADD routing addresses
@app.route("/mine", methods=["GET"])
def mine():
    # Run proof of work algorithm
    last_block = blockchain.last_block
    last_proof = last_block["proof"]
    proof = blockchain.proof_of_work(last_proof)

    # We receive one coin when mined a new block
    blockchain.new_transaction(
        sender="0",
        recipient=node_identifier,
        amount=1,
    )

    # Forge the new block
    previous_hash = blockchain.hash(last_block)
    block = blockchain.new_block(proof, previous_hash)

    response = {
        "message": "New Block Forged",
        "index": block["index"],
        "transactions": block["transactions"],
        "proof": block["proof"],
        "previous_hash": block["previous_hash"],
    }
    return jsonify(response), 200


@app.route("/transactions/new", methods=["POST"])
def new_transaction():
    values = request.get_json()

    # check required fields that are POST to this function
    required = ["sender", "recipient", "amount"]
    if not all(elem in values for elem in required):
        return "Missing values", 400

    # New transaction is created
    index = blockchain.new_transaction(
        values["sender"],
        values["recipient"],
        values["amount"])

    response = {"message": f"Transaction will be added to Block {index}"}
    return jsonify(response), 201


@app.route("/chain", methods=["GET"])
def full_chain():
    response = {
        "chain": blockchain.chain,
        "length": len(blockchain.chain),
    }
    return jsonify(response), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)