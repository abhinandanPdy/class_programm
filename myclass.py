class myclass:
    def func1(self):
        a = 10
        b = 11
        c = a + b
        print("1st function is working - ", c)

    def func2(self):
        print("2nd function is working.")


object = myclass()
object.func1()
object.func2()
