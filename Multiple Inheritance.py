class sm:
    def java(self):
        print("Java")

class google:
    def android(self):
        print("android")
class oracle(google,sm):
    def dbms(self):
        print("sql")

object=oracle()
object.dbms()
object.java()
object.android()