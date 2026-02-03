class Gripper:
      def activate(self):
          print("Gripper:Closing claws")

class Vacuum:
      def activate(self):
           print("Vacuum:Suction engaged")
tools =[Gripper(),Vacuum()]
print("...Starting Robot Routine....")
for tool in tools:
     tool.activate()