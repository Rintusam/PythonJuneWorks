class Editors:

    def __init__(self,name,vendor):

        self.name=name

        self.vendor=vendor

    def open(self):

        print(f"{self.name} open")

    def execute(self):

        print(f"{self.execute} execute")

class Vscode(Editors):

    def __init__(self, name, vendor):

        super().__init__(name, vendor)

class PyCharm(Editors):

    def __init__(self,name,vendor):

        super().__init__(name,vendor)


Vscode_instance=Vscode("VisualStudioCode","vscvendor")
Vscode_instance.open()

pyc_instance=PyCharm("Pycharm","jetbarins") 
pyc_instance.open()




