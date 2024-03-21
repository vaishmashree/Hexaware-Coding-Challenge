class PatientIdNotFoundException(Exception):
    def __init__(self,patientId):
        super().__init__(f"Patient ID {patientId} not found.")
