from dao.HospitalServiceImpl import HospitalServiceImpl
from entity.appointment import Appointment

class MainModule:
    def __init__(self):
        self.hospital_service = HospitalServiceImpl()

    def switch(self, choice):
        switcher = {
            1: self.get_appointment_by_id,
            2: self.get_appointments_for_patient,
            3: self.get_appointments_for_doctor,
            4: self.schedule_appointment,
            5: self.update_appointment,
            6: self.cancel_appointment,
            7: exit
        }
        func = switcher.get(choice, lambda: print("Invalid choice"))
        func()

    def get_appointment_by_id(self):
        try:
            appointment_id = int(input("Enter Appointment ID: "))
            appointment = self.hospital_service.getAppointmentById(appointment_id)
            if appointment:
                print("Appointment Details:")
                print(appointment)
            else:
                print("Appointment not found.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
        except Exception as e:
            print(f"Error: {e}")

    def get_appointments_for_patient(self):
        try:
            patient_id = int(input("Enter Patient ID: "))
            appointments = self.hospital_service.getAppointmentsForPatient(patient_id)
            if appointments:
                print("Appointments for Patient:")
                for appointment in appointments:
                    print(appointment)
            else:
                print("No appointments found for the patient.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
        except Exception as e:
            print(f"Error: {e}")

    def get_appointments_for_doctor(self):
        try:
            doctor_id = int(input("Enter Doctor ID: "))
            appointments = self.hospital_service.getAppointmentsForDoctor(doctor_id)
            if appointments:
                print("Appointments for Doctor:")
                for appointment in appointments:
                    print(appointment)
            else:
                print("No appointments found for the doctor.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
        except Exception as e:
            print(f"Error: {e}")

    def schedule_appointment(self):
        try:
            appointment_id = int(input("Enter Appointment ID: "))
            patient_id = int(input("Enter Patient ID: "))
            doctor_id = int(input("Enter Doctor ID: "))
            appointment_date = input("Enter Appointment Date (YYYY-MM-DD): ")
            description = input("Enter Appointment Description: ")
            appointment = Appointment(appointment_id, patient_id, doctor_id, appointment_date, description)
            success = self.hospital_service.scheduleAppointment(appointment)
            if success:
                print("Appointment scheduled successfully.")
            else:
                print("Unable to schedule the appointment.")
        except ValueError:
            print("Invalid input. Please enter valid information.")
        except Exception as e:
            print(f"Error: {e}")

    def update_appointment(self):
        try:
            appointment_id = int(input("Enter Appointment ID to update: "))
            new_patient_id = int(input("Enter updated Patient ID: "))
            new_doctor_id = int(input("Enter updated Doctor ID: "))
            new_description = input("Enter updated Appointment Description: ")
            new_appointment_date = input("Enter updated Appointment Date (YYYY-MM-DD): ")
            
            appointment = Appointment(appointment_id, new_patient_id, new_doctor_id, new_appointment_date, new_description)
            
            success = self.hospital_service.updateAppointment(appointment)
            
            if success:
                print("Appointment updated successfully.")
            else:
                print("Unable to update the appointment.")
        except ValueError:
            print("Invalid input. Please enter valid information.")
        except Exception as e:
            print(f"Error: {e}")

    def cancel_appointment(self):
        try:
            appointment_id = int(input("Enter Appointment ID to cancel: "))
            success = self.hospital_service.cancelAppointment(appointment_id)
            if success:
                print("Appointment canceled successfully.")
            else:
                print("Unable to cancel the appointment.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main_module = MainModule()
    while True:
        print("\n1. Get Appointment by ID")
        print("2. Get Appointments for Patient")
        print("3. Get Appointments for Doctor")
        print("4. Schedule Appointment")
        print("5. Update Appointment")
        print("6. Cancel Appointment")
        print("7. Exit")
        choice = int(input("Enter your choice: "))
        main_module.switch(choice)
