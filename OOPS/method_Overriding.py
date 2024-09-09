# method_overriding

# rules:-    *minimum 2 class 
#            *child should have inheritance of parent 

class parent:

    def mobile(self):

        print("redmi note 10 pro")

    def bike(self):

        print("RE standard 350")

class child(parent):

    def mobile(self):

        print("iphone 16")


child_instance=child()

child_instance.mobile()     #check whether the child contain mobile and  print it
child_instance.bike()       #if child doesnot have bike then it will inherit from its parent



    