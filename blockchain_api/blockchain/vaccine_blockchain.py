import json
from .blockchain import Blockchain
from .block import Block
from .vaccine_record import VaccineRecord

class VaccineBlockchain(Blockchain):
    def __init__(self, difficulty):
        super().__init__(difficulty)

    def create_vaccine_record(self, patient_name, vaccine_type, vaccination_date, unique_id):
        new_record = VaccineRecord(patient_name, vaccine_type, vaccination_date, unique_id)
        new_block = self.new_block(json.dumps(new_record.to_dict()))
        self.add_block(new_block)

    def read_vaccine_record(self, unique_id):
        for block in self.blocks:
            if block.index == 0:
                continue
            record_data = json.loads(block.data)
            record = VaccineRecord.from_dict(record_data)
            if record.unique_id == unique_id:
                return record
        return None
