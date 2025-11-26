class notification:
    def get_notification(self):
        pass
class instagram(notification):
    def get_notification(self):
        print("notification from instagram")
class facebook(notification):
    def get_notification(self):
        print("notification from facebook")
obj=facebook()
obj.get_notification()
obj1=instagram()
obj1.get_notification()

