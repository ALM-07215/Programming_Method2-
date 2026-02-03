import random
import time

class Sensor:
    def __init__(self, name: str, offset: float = 0.5):
        self.name = name            # Public: Anyone can see/change the name
        self.__offset = offset      # Private: Only the class can change this
        self.__enabled = True       # Private: Internal state

    def enable(self):
        self.__enabled = True

    def disable(self):
        self.__enabled = False

    def calibrate(self, new_offset: float):
        """Adjusts the sensor's accuracy with safety checks."""
        if not isinstance(new_offset, (int, float)):
            raise TypeError("Offset must be numeric")
        if abs(new_offset) > 10.0:
            raise ValueError("Calibration offset out of range")
        self.__offset = new_offset

    def get_calibrated_value(self, raw_value: float) -> float:
        if not self.__enabled:
            raise RuntimeError(f"Sensor {self.name} is disabled")
        return raw_value - self.__offset

# test case 1
temp_sensor = Sensor("Main_Temp")
temp_sensor.calibrate(0.8) 
print(temp_sensor.get_calibrated_value(25.0)) # Result: 24.2
#test case 2
temp_sensor = Sensor("TMP36",offset=1.0)
temp_sensor.calibrate(1.0) 
print(temp_sensor.get_calibrated_value(30.0)) # Result: 29.2

temp_sensor = Sensor("TMP36",offset=1.0)
temp_sensor.calibrate(1.0) 
print(temp_sensor.get_calibrated_value(30.0))

