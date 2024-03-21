from abc import ABC, abstractmethod
from entity.appointment import Appointment
from typing import List


class IHospitalService(ABC):
    
    @abstractmethod
    def getAppointmentById(self,appointmentid) -> Appointment:
        pass

    @abstractmethod
    def getAppointmentsForPatient(self,patientid) -> List[Appointment]:
        pass

    @abstractmethod
    def getAppointmentsForDoctor(self,doctorid) -> List[Appointment]:
        pass

    @abstractmethod
    def scheduleAppointment(self, appointment:Appointment) -> bool:
        pass

    @abstractmethod
    def updateAppointment(self,appointment:Appointment) -> bool:
        pass

    @abstractmethod
    def cancelAppointment(self,appointmentid) -> bool:
        pass