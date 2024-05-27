import json

class VaccineRecord:
    def __init__(self, patient_name, vaccine_type, vaccination_date, unique_id):
        self.patient_name = patient_name
        self.vaccine_type = vaccine_type
        self.vaccination_date = vaccination_date
        self.unique_id = unique_id

    def __str__(self):
        return f"{self.patient_name}, {self.vaccine_type}, {self.vaccination_date}, {self.unique_id}"

    def __repr__(self):
        return self.__str__()

    def to_dict(self):
        return {
            "patient_name": self.patient_name,
            "vaccine_type": self.vaccine_type,
            "vaccination_date": self.vaccination_date,
            "unique_id": self.unique_id
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            data["patient_name"],
            data["vaccine_type"],
            data["vaccination_date"],
            data["unique_id"]
        )
