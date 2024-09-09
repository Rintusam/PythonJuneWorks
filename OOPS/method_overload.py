class operations:

    def perform_add(self,*args):

        # total=0

        # for arg in args:

        #     if isinstance(arg,(int,float)):

        #         total=total+arg
        
        # return total


                                    # 0R

                                    
    
        total=sum([arg for arg in args if isinstance(arg,(int,float))])
    
        return total
    

maths=operations()

print(maths.perform_add(22,24,"hello"))