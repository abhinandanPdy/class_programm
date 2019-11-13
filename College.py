class College:
    def btech(self, a=None):
        if a != None:
            print("argumentive")
        else:
            print("non argumentive")

    # This kind of concept is use to achive function overloding in python.


object = College()
object.btech()
object.btech(1000)
