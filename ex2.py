class Actuator:
    def __init__(self, pin_number):
        self.pin_number = pin_number

class LED(Actuator):
    def turn_on(self):
        print(f"LED on pin {self.pin_number} is glowing")

class Buzzer(Actuator):
    def beep(self):
        print(f"Buzzer on pin {self.pin_number} is making sound")

#sample answer 
class Actuator:
     def __init__(self, pin):
      self.pin = pin
class LED(Actuator):
     pass
class Buzzer(Actuator):
     pass