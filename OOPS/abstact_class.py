from abc import ABC,abstractmethod


class car(ABC):

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def accelerate(self):
        pass

    @abstractmethod
    def stop(self):
        pass


class swift(car):

    def start(self):
        print("swift start method")

    def accelerate(self):
        print("swift accelerate method")

    def stop(self):
        print("swift stop method")

swift_instance=swift()

swift_instance.start()
swift_instance.accelerate()
swift_instance.stop()
