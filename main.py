import uuid
from flask import Flask, jsonify, request, render_template
from blockchain import Blockchain


# Using Flask as API to communicate with Blockchain
app = Flask(__name__)

# Unique address for node
node_identifier = str(uuid.uuid4()).replace("-", "")

# instantiate Blockchain
blockchain = Blockchain()

# Add routing addresses
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/transaction_form")
def transaction_form():
    return render_template("transaction.html")

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


@app.route("/submit-form", methods=["POST", "GET"])
def new_transaction_post():
    sender = request.form["sender"]
    receiver = request.form["receiver"]
    amount = int(request.form["amount"])

    # New transaction is created
    index = blockchain.new_transaction(
        sender,
        receiver,
        amount)

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
    app.run(host="127.0.0.1", port=5000)