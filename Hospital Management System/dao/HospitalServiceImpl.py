import pyodbc
from dao.IHospitalService import IHospitalService
from entity.appointment import Appointment
from exception.patientException import PatientIdNotFoundException
from util.DBConnection import DBConnection
from typing import List

class HospitalServiceImpl(IHospitalService):
    def __init__(self):
        self.conn = DBConnection.getConnection()
        self.cursor = self.conn.cursor() 
    
    def __del__(self):
        self.conn.close()

    def getAppointmentById(self, appointmentid) -> Appointment:
        self.cursor.execute("select * from appointment where appointmentid=?", (appointmentid,))
        result = self.cursor.fetchone()
        if result:
            appointment = Appointment(*result)
            return appointment
        return None

    def getAppointmentsForPatient(self, patientId) -> List[Appointment]:
        try:
            self.cursor.execute("select * from appointment where patientid=?", (patientId,))
            result = self.cursor.fetchall()
            if not result:
                raise PatientIdNotFoundException(patientId)
            appointments = [Appointment(*row) for row in result]
            return appointments
        except PatientIdNotFoundException as err:
            print(f"Exception: {err}")
            return []
        except Exception as e:
            print(f"Unexpected exception: {e}")
            return []

    def getAppointmentsForDoctor(self, doctorid) -> List[Appointment]:
        self.cursor.execute("select * from appointment where doctorid=?", (doctorid,))
        result = self.cursor.fetchall()
        appointments = [Appointment(*row) for row in result]
        return appointments

    def scheduleAppointment(self, appointment: Appointment) -> bool:
        try:
            self.cursor.execute("""insert into appointment (appointmentid, patientid, doctorid, appointmentdate, description)
                                   values (?, ?, ?, ?, ?)""",
                                (appointment.getAppointmentId(), appointment.getPatientId(),
                                 appointment.getDoctorId(), appointment.getAppointmentDate(),
                                 appointment.getDescription()))
            self.conn.commit()
            return True
        except pyodbc.Error as err:
            print(f"Error scheduling appointment: {err}")
            return False

    def updateAppointment(self, appointment: Appointment) -> bool:
        try:
            self.cursor.execute("""update appointment set patientid=?, doctorid=?, appointmentdate=?,
                                description=? where appointmentid=?""",
                                (appointment.getPatientId(), appointment.getDoctorId(),
                                 appointment.getAppointmentDate(), appointment.getDescription(),
                                 appointment.getAppointmentId()))
            self.conn.commit()
            return True
        except pyodbc.Error as err:
            print(f"Error updating appointment: {err}")
            return False

    def cancelAppointment(self, appointmentid) -> bool:
        try:
            self.cursor.execute("""delete from appointment where appointmentid=?""", (appointmentid,))
            self.conn.commit()
            return True
        except pyodbc.Error as err:
            print(f"Error canceling appointment: {err}")
            return False
