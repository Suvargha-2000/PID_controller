import numpy as np
import matplotlib.pyplot as plt

class Controllers:
    def __init__(self , Kp , Ki , Kd, reference) -> None:
        self.reference = reference
        self.Kp = Kp
        self.Ki = Ki 
        self.Kd = Kd
        self.Intval = 0
        self.propVal = 0
        self.derError = 0 
    def pidController(self) -> None :
        pass
    def proportionalOnly(self , val , Kp = 0):
        if Kp == 0 :
            Kp = self.Kp
        self.propVal = val
        error = self.reference - val
        return error*self.Kp
    def integralController(self , val , Ki = 0):
        if Ki == 0 :
            Ki = self.Ki
        error = self.reference - val
        self.Intval = error*Ki + self.Intval
        return self.Intval
    
    def derivativeController(self , val , Kd = 0):
        if Kd == 0 :
            Kd = self.Kd
        
        error = self.reference - val 
        output = Kd*(error - self.derError)
        self.derError = error 
        return output

    def propIntController(self, val):
        return self.integralController(val) + self.proportionalOnly(val)
    def propDerController(self, val):
        return self.derivativeController(val) + self.proportionalOnly(val)
    
    def PIDcontroller(self , val):
        return self.derivativeController(val) + self.proportionalOnly(val) + self.integralController(val)


def simulation() :
    # time = np.arange(0, 50, 0.1) 
    # Y = np.sin(time)
    X = [i for i in range(100)]
    Y = [0 for i in range(30)]
    Y = Y + [1 for i in range(30)]
    Y = Y + [0 for i in range(40)]
    

    controllers = Controllers(1 , 0.2 , 0.8 , 0)
    # values = list(map(controllers.proportionalOnly , Y))
    # Ivalues = list(map(controllers.propIntController, Y))
    # Dvalues = list(map(controllers.derivativeController, Y))
    # PDValues = list(map(controllers.propDerController, Y))
    pidValues = list(map(controllers.PIDcontroller, Y))

    # plt.plot(time, values)
    plt.step(X , Y)
    # plt.plot(Ivalues)
    plt.plot(X , pidValues)

    
    plt.show()

simulation()