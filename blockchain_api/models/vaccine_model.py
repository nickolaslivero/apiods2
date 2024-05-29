from pydantic import BaseModel


class VaccineRecord(BaseModel):
    id: str
    username: str
    vaccine_name: str
    date: str
    end_date: str
