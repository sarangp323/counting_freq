class Patient_manager():
    def __init__(self):
        self.__patient={}

    def _add_patient(self,patient_id,data):
        self.__patient[patient_id]=data

    def _get_patient(self,patient_id):
        return self.__patient[patient_id]

class Access_manager(Patient_manager):

    def __init__(self,fm):
        self.fm=fm

    def add_patient(self, patient_id,data,password):
        if password == 'sudo':
            self.fm._add_patient(patient_id,data)
        else:
            print("not Accessible")

    def get_patient(self, patient_id,password):
        if password == 'sudo':
            return self.fm._get_patient(patient_id)
        else:
            print("Only doctor can access  this data")

am = Access_manager(Patient_manager())

am.add_patient('dassy',['pneumonia 23-03-2020'],'sudo')

print(am.get_patient('dassy','sudo'))
        

