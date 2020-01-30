class human:
    species="h.sapiens"
    def _init_(self,name):
        self.name=name
        self.age=0
    def say(self,msg):
        print("{name}:{message}".format(name=self.name,message=msg))
        
        
    
