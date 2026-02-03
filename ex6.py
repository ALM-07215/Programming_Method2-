dist=0.8
emergency_stop=False
print ("ESTOP")
emergency_stop=True
if dist<0.5:
    print("Collision")
elif 0.5<dist<1.5:
    print("Warning")
else:
    print("Normal")