

class vehicle:

    def start(self):

        print("vehicle start method")

    def accelerate(self):

        print("vehicle accelerate method")

class innova(vehicle):

    pass

innova_instance=innova()

innova_instance.accelerate()

innova_instance.start()