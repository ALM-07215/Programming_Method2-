def send_motor_command(rpm: float, motor_id: int = 0) -> tuple[int, float]:
    """Sends a speed command to a specific motor with safety checks."""
    if rpm > 1000:
        raise ValueError(f"Safety Limit Exceeded: {rpm} RPM is too high!")
    
    return (motor_id, rpm)

commands_to_test = [500, 1200,1000,100,1500]

for cmd in commands_to_test:
    try:
        m_id, speed = send_motor_command(cmd, motor_id=1)
        print(f"SUCCESS: Motor {m_id} set to {speed} RPM")
    except ValueError as e:
        print(f"CRITICAL ALERT: {e}")