from fastapi import APIRouter
from blockchain.blockchain import Blockchain

import sys
import json

sys.path.append('../')

from blockchain_api.models.vaccine_model import VaccineRecord

router = APIRouter()

blockchain = Blockchain(4)


@router.get("/blocks")
def get_blocks():
    blocks_data = []
    for block in blockchain.blocks:
        if block.data != "Genesis Block":
            blocks_data.append(eval(block.data))
    return blocks_data

@router.get("/blocks/{username}")
def get_blocks_by_username(username):
    blocks = []
    for block in blockchain.blocks:
        if block.data != "Genesis Block" and eval(block.data)["username"] == username:
            blocks.append(eval(block.data))
    if blocks:
        return blocks
    return {"message": "Block not found", "status": 404}

@router.post("/blocks")
def add_block(vaccine_record: VaccineRecord):

    if blockchain.is_blockchain_valid() and blockchain.is_first_block_valid():
        block = blockchain.new_block(json.dumps(vaccine_record.dict()))
        print("[SERVER] New block: ", block)
        blockchain.add_block(block)
        return {"message": "Block created", "block": vaccine_record, "status": 200}

    return {"message": "Something went wrong", "status": 400}
