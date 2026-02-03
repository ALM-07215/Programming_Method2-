class Sensor:
    def __init__(self, name: str, offset: float = 0.5):
        self.name = name 
        self.__offset = offset
        self.__enabled = True

    def get_calibrated_value(self, raw_value: float) -> float:
        if not self.__enabled:
            raise RuntimeError(f"Sensor {self.name} is disabled")
        return raw_value - self.__offset
class UltrasonicSensor(Sensor):
    def __init__(self, name, pin):
      super().__init__(name) # Inherit from parent
      self.pin = pin
    def ping(self):
      return "Sending sonic pulse..."
dist_sensor = UltrasonicSensor("HC-SR04", 12)
print(dist_sensor.name) # Accessed from parent
print(dist_sensor.ping()) # Own unique method
print(dist_sensor.get_calibrated_value(100.0))
