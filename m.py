class SmartFan:
    def __init__(self, threshold_temp):
        self.limit = threshold_temp

    def check_environment(self, current_temp):
        print(f"Current reading: {current_temp} Celsius")
        
        if current_temp > self.limit:
            self.turn_on()
        else:
            self.turn_off()

    def turn_on(self):
        print("ACTION: The fan must turn on")

    def turn_off(self):
        print("ACTION: The fan stays off")


my_fan = SmartFan(40)

user_input = int(input("Choose the temperature: "))

my_fan.check_environment(user_input)