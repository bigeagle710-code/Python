class myClass :
    __privateVar = 27
    def __privMeth(self):
        print("I am in my house")
    def hello(self):
         print("Private Variable value:", myClass.__privateVar)
f = myClass()            
f.hello()
f.__privMeth()