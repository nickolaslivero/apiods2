from pydantic import BaseModel


class VaccineRecord(BaseModel):
    unique_id: int
    patient_name: str
    vaccine_type: str
    vaccination_date: str