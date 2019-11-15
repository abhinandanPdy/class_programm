class sm:
    def java(self):
        print("Java")

class google(sm):
    def android(self):
        print("android")
class oracle(google):
    def dbms(self):
        print("sql")

object=oracle()
object.dbms()
object.java()
object.android()