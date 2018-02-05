# master classes
class Patient:
    def __init__(self, name):
        self.name = name

    def discharge(self):
        raise NotImplementedError("This is an abstract method and needs to be implemented in derived classes.")


# two different patient types
class EmergencyPatient(Patient):
    def __init__(self, name):
        Patient.__init__(self, name)
        self.expectedcost = 1000

    def discharge(self):
        print(self.name + " " + "Emergency Department")

class HospitalizedPatient(Patient):
    def __init__(self, name):
        Patient.__init__(self, name)
        self.expectedcost = 2000

    def discharge(self):
        print(self.name + " " + "Get Hospitalized")

# hospital class
class Hospital:
    def __init__(self):
        self.cost = 0
        self.patients = []

    def admit(self, patients):
        self.patients.append(patients) # adding patient over and over again


    def discharge_all(self):
        for patients in self.patients:
            patients.discharge()
            self.cost += patients.expectedcost


    def get_total_cost(self):
        return self.cost


# creating variables

P1 = HospitalizedPatient("P1")
P2 = HospitalizedPatient("P2")
P3 = EmergencyPatient("P3")
P4 = EmergencyPatient("P4")
P5 = EmergencyPatient("P5")

NewHospital = Hospital()

NewHospital.admit(P1)
NewHospital.admit(P2)
NewHospital.admit(P3)
NewHospital.admit(P4)
NewHospital.admit(P5)


NewHospital.discharge_all()

print(NewHospital.get_total_cost())







