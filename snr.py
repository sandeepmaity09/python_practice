#snr.py

import math
signal_power=9.0
noise_power=10.0
ratio=signal_power/noise_power
decibels=10*math.log10(ratio)
print decibels