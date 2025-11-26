class adhar:
    def __init__(self,name,adhar_number,dob,finger_print,retina):
        self.name=name
        self.adhar_number=adhar_number
        self.dob=dob
        self._finger_print=finger_print
        self.__retina=retina
    def user_data(self):
        print("\n",self.name,"\n",self.adhar_number,"\n",self.dob,"\n",self._finger_print,"\n",self.__retina)
    def getRetina(self):
        return self.__retina
user=adhar("darshan",6576787757,"26-05-2003","dgfh7","ggtdth656")
user.user_data()
print(user.getRetina())
