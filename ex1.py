class Gripper:   
    def __init__(self):
        self.__pressure = 0
        self._max_pressure=100
    def apply_pressure(self,amount):
         if 0 <= amount <= Gripper.__max_pressure:
            self.__pressure = amount
         else:
             print("Safety Limit Exceeded!")
    def get_status(self):
         return self.__pressure
    

#sample answer
class Gripper:
    def __init__(self, pressure: int = 0, max_pressure: int = 100):
        self._pressure = pressure
        self._max_pressure = max_pressure

    def apply_pressure(self, amount):
        if 0 <= amount <= self._max_pressure:
            self._pressure = amount  # [Update] logic: Save the value!
            print(f"Pressure set to {self._pressure}")
        else:
            print("Safety Limit Exceeded")

    def get_status(self):
        print(f"Current Pressure: {self._pressure}")

# --- Test Run ---
g = Gripper()
g.apply_pressure(50)  # Works
g.apply_pressure(150) # Safety Limit Exceeded
g.get_status()        # Prints 50




