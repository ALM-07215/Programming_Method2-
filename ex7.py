voltage=[12.6,12.5,12.2,11.8,11.5,10.8,10.2]
for minute in enumerate(voltage):
    print(f"Minute{minute}:V")
v=12.0
while True:
    print(f"Current Level:{v}V ")
    v=-0.5
    if v<10.5:
        print("Low Battery!")
        break
for reading in voltage:
    if reading>12.0:
        continue
    if reading<11.0:
        break
    print(reading)
print ("Filter Readings ")
for reading in voltage:
    if v>12.0:continue
    if v<11.0:break
    print(reading)