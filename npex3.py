import numpy as np
import math

def wind_magnitude(u, v):
    """Function to read horizontal zonal
    and meridional wind data and calculate
    total magnitude"""
    raw_magnitude = (u**2 + v**2)**0.5

    # threshold for data to be distinguised from noise is 0.1 m/s
    # so set data < 0.1 m/s so be equal to 0.1
    processed_magnitude = np.where(raw_magnitude < 0.1, 0.1, raw_magnitude)

    return processed_magnitude

# Main code
print("Test 1:")
u1 = np.array([[4,5,6],[2,3,4]])
v1 = np.array([[2,2,2],[1,1,1]])

print(wind_magnitude(u1,v1))

print("\nTest 2:")
u2 = np.array([[4,5,0.01],[2,3,4]])
v2 = np.array([[2,2,0.03],[1,1,1]])

print(wind_magnitude(u2,v2))
