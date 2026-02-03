class PressureSensor:
    def __init__(self, sensor_id: str):
        self.id = sensor_id
        self._pressure = 0.0

    def update_reading(self, value: float):
        if not 0.0 <= value <= 10.0:
            raise ValueError(f"Pressure out of safety limits: {value}")
        self._pressure = value

    @property
    def pressure(self):
        return self._pressure

# Simulation Logic
my_sensor = PressureSensor("PS-01")
sensor_log = []
raw_inputs = [2.5, 4.8, 11.0]

for val in raw_inputs:
    try:
        my_sensor.update_reading(val)
        status = "OK"
    except ValueError as e:
        print(f"Warning: {e}")
        status = "ERROR"
    
    sensor_log.append({"id": my_sensor.id, "val": val, "status": status})

print(f"Final Log: {sensor_log}")