dist = 0.8
emergency_stop = False

if emergency_stop:
    safety_mode = "ESTOP"
elif dist < 0.5:
    safety_mode = "COLLISION"
elif 0.5 <= dist <= 1.5:
    safety_mode = "WARNING"
else:
    safety_mode = "NORMAL"

led_color = "RED" if safety_mode != "NORMAL" else "GREEN"
print(f"System: {safety_mode}, LED: {led_color}")