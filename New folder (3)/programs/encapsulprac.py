class android:
    def __init__(self):
        self.__updatedate()
    def insert(self):
        print("battery inserting")
    def __updatedate(self):
        print("software updated")
obj=android()
obj.insert()
