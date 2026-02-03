from abc import ABC, abstractmethod
class Motor(ABC):
    @abstractmethod
    def set_speed(self, rpm):
        pass

    @abstractmethod
    def stop(self):
        pass
# 2. CONCRETE IMPLEMENTATION A: Stepper Motor
class StepperMotor(Motor):
  def set_speed(self, rpm):
# Hidden complexity: Step logic
    print(f">>> [Hardware Call] Pulsing GPIO pins for {rpm} RPM.")
    print(f"Stepper Motor: Moving at {rpm} RPM.")
  def stop(self):
    print("Stepper Motor: Engaging holding torque and stopping.")
# 3. CONCRETE IMPLEMENTATION B: DC Motor
class DCMotor(Motor):
     def set_speed(self, rpm):
# Hidden complexity: PWM (Pulse Width Modulation) logic
       voltage = rpm * 0.01
       print(f">>> [Hardware Call] Setting PWM Duty Cycle to {voltage}V.")
       print(f"DC Motor: Spinning at {rpm} RPM.")
     def stop(self):
         print("DC Motor: Shorting terminals for dynamic braking.")
stepper_motor=StepperMotor()
stepper_motor.set_speed(120)
stepper_motor.stop()

dc_motor= DCMotor()
dc_motor.set_speed(123)
dc_motor.stop()