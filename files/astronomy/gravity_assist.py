import numpy as np
import math

# constants and variables
g = 6.6743*10**-11                                                              # m^3*kg^-1*s^-2
m = 1.898*10**27                                                                # mass of Jupiter in kg
t_start = 0                                                                     # timeinterval in seconds
t_max = 200                                                                     # maximum duration
t_interval = 1

position_spacecraft_vector = np.array([1, -100000000, 1])                       # initial position vector of spacecraft
speed_spacecraft_vector = np.array([-1, 100000, -1])                             # initial speed vector of spacecraft

position_planet_vector = np.array([0, 0, 0])                                    # initial position vector of planet
speed_planet_vector = np.array([0,0,0])                                         # initial speeds vector of planet

for time in range(t_start, t_max+1, t_interval):
    distance = np.linalg.norm(position_planet_vector - position_spacecraft_vector)
    force_direction_vector = position_planet_vector - position_spacecraft_vector
    force_unit_vector = force_direction_vector / distance
    acceleration_vector = g * m / distance**2
    
    position_spacecraft_vector = position_spacecraft_vector + speed_spacecraft_vector * t_interval + 0.5 * acceleration_vector * t_interval**2
    speed_spacecraft_vector = speed_spacecraft_vector + acceleration_vector * t_interval
    
    position_planet_vector = position_planet_vector + speed_planet_vector * t_interval

    speed_spacecraft = np.linalg.norm(speed_spacecraft_vector)
    
    print(time, "\t", distance, "\t", force_direction_vector)

