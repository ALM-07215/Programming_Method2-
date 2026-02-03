
temp = int(input("choose the temperature: "))
print(f"{temp} Celsius") 
if temp > 40:
    print("the fan must turn on")
else:
    print("the fan stay off")
#OOP Python
class Coolingsystem:
    def _init_(self,threshold):
        self.threhold=threshold
        self.fan_on=False
    def check_temp(self,current_temp):
        pass
system=Coolingsystem(30)
system.check_temp(89)