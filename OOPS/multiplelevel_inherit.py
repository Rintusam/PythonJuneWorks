class GrandParent:

    def m1(self):

        print("GrandParent class m1 method")

class parent(GrandParent):

    def m2(self):

        print("parent class m2 method")

class child(parent,GrandParent):

    def m3(self):

        print("parent class m3 method")

child_instance=child()
child_instance.m3()

child_instance.m2()

child_instance.m1()