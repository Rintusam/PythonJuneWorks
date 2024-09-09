class operations:

    def perform_add(self,*args):

        return sum(args)
    
    def get_max_num(self,*args):

        return max(args)
    

maths=operations()

print(maths.get_max_num(10,23,56,44))

print(maths.perform_add(22,24))


