# Command thrust amount to Heron thruster,
# transmitted from higher-level software to the MCU 
# on the /cmd_drive topic.

# Thrust amount ranges from [-1.0..1.0], where 1.0 pushes Heron forward.
float32 left
float32 right
