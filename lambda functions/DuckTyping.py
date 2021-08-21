class PyCharm:

    def execute(self):
        print("Compiling")
        print("Running")

class Laptop:

    def code(self, ide):
        ide.execute()


lap1 = Laptop()
pyCharm = PyCharm()
lap1.code(pyCharm)
