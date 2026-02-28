
# constructor 
 #initialize attributes
# same as class name __init__

class  Car:

    def __init__(self,name,brand):

        #initialize attributes

        self.name = name

        self.brand= brand


    def start(self):

        print(self.name,"is starting")

    def accelerate(self):

        print(self.name ,"accelerate")

bmw_instance = Car("bmw","bmw")

baleno_instance = Car("baleno","maruthy")
baleno_instance.start()
baleno_instance.accelerate()

