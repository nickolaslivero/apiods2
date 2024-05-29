from fastapi import APIRouter
from blockchain.vaccine_blockchain import VaccineBlockchain

import sys

sys.path.append('../')

from blockchain_api.models.vaccine_model import VaccineRecord

router = APIRouter()

blockchain = VaccineBlockchain(4)


@router.get("/blocks")
def get_blocks():
    blocks_data = []
    for block in blockchain.blocks:
        if block.data != "Genesis Block":
            blocks_data.append(eval(block.data))
    return blocks_data

@router.get("/blocks/{block_id}")
def get_block_by_id(block_id):
    for block in blockchain.blocks:
        if block.data != "Genesis Block" and eval(block.data)["unique_id"] == int(block_id):
            return eval(block.data)
    return {"message": "Block not found", "status": 404}

@router.post("/blocks")
def add_block(vaccine_record: VaccineRecord):

    if blockchain.is_blockchain_valid() and blockchain.is_first_block_valid():
        blockchain.create_vaccine_record(**vaccine_record.dict())
        return {"message": "Block created", "block": vaccine_record, "status": 200}
    
    return {"message": "Something went wrong", "status": 400}
