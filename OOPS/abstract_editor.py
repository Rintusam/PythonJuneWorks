from abc import ABC,abstractmethod

class editor(ABC):

    @abstractmethod
    def open(self):
        pass

    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def debug(self):
        pass

class vscode(editor):

    def open(self):
        print("vscode open method")

    def execute(self):
        print("vscode close method")

    def debug(self):
        print("vscode debug method")

vscode_instance=vscode()

vscode_instance.open()
vscode_instance.execute()
vscode_instance.debug()



