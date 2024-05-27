from typing import Union
from fastapi import FastAPI
from vaccineBlockchain import VaccineBlockchain
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

blockchain = VaccineBlockchain(4)


class VaccineRecord(BaseModel):
    unique_id: int
    patient_name: str
    vaccine_type: str
    vaccination_date: str


@app.get("/blocks")
def get_blocks():
    blocks_data = []
    for block in blockchain.blocks:
        if block.data != "Genesis Block":
            blocks_data.append(eval(block.data))
    return blocks_data

@app.get("/blocks/{block_id}")
def get_block_by_id(block_id):
    for block in blockchain.blocks:
        if block.data != "Genesis Block" and eval(block.data)["unique_id"] == int(block_id):
            return eval(block.data)
    return {"message": "Block not found", "status": 404}

@app.post("/blocks")
def add_block(vaccine_record: VaccineRecord):

    if blockchain.is_blockchain_valid() and blockchain.is_first_block_valid():
        blockchain.create_vaccine_record(**vaccine_record.dict())
        return {"message": "Block created", "block": vaccine_record, "status": 200}
    
    return {"message": "Something went wrong", "status": 400}
