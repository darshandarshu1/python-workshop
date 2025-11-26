class Application:
    def __init__(self,appliation_name,catogary,company,app_sze,no_of_users,ratings):
        self.appliation_name=appliation_name
        self.catogary=catogary
        self.company=company
        self.app_sze=app_sze
        self.no_of_users=no_of_users
        self.ratings=ratings
    def  signup(self):
        print(f"signup done, {self.appliation_name}")
    def login(self):
        print(f"welcome to application {self.appliation_name}")
    def logout(self):
        print("thank you for using")
    def info(self):
        print("application information:\n",self.appliation_name,"\n",self.catogary,"\n",self.company,"\n",self.app_sze,"\n",self.no_of_users,"\n",self.ratings)
app1=Application("instagram","social media","meta",42.47,1000,4.4)
app2=Application("facebook","social media","meta",45,2000,4)
app3=Application("whatsapp","social media","meta",50,5000,5)
app1.signup()
app1.login()
app1.logout()
app1.info()