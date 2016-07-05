# General MCU status for Heron transmitted from the MCU
# to higher-level software on the /sense topic.

Header header

# Voltage level of battery, in volts
float32 battery

# Instantaneous current drawn by each motor, in amps.
float32 current_left
float32 current_right

# Bitfield represents status of hobby R/C override.
uint8 RC_INRANGE=1
uint8 RC_INUSE=2
uint8 rc

# Pulse lengths received from the three R/C channels.
uint16 rc_throttle
uint16 rc_rotation
uint16 rc_enable
