#Restrict the access to methods and variables
#To prevent data modify accidently

class data:
    def __init__(self):
        print("in init metho##########")
        # self.__updatedata()
    def insert(self):
        try:
            a = 5/0
        except Exception:
            print("in exception")
        print("data is inserted")
    def __withdraw(self):
        print("Data updatede....")

    @staticmethod
    def sample():
        print("in sample###")


obj=data()
obj.insert()
# data.insert(obj)

# obj.sample()
# data.sample()


# class Data2(data):
#     pass
#
# obj1 = Data2()
# obj1