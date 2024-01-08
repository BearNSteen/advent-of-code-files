import datetime
import math

def calculate_distance_to_mars(date_time):
    # Constants
    AU = 149597870700  # 1 AU in meters (average distance from Earth to Sun)
    MARS_ORBIT_ECCENTRICITY = 0.0933958  # Mars' orbit eccentricity
    MARS_ORBIT_SEMI_MAJOR_AXIS = 227939100000  # Mars' orbit semi-major axis in meters
    MARS_ORBIT_PERIHELION_DISTANCE = 207732000000  # Mars' perihelion distance in meters

    # Calculate Julian Date from input date and time
    
    ordinal_date = datetime.datetime.toordinal(date_time)
    julian_date = ordinal_date + 2451545.0



    # Calculate mean anomaly of Mars (M)
    M = (julian_date - 2451545.0) * 360.0 / 365.242191

    # Calculate eccentric anomaly (E)
    E = math.sqrt(MARS_ORBIT_ECCENTRICITY) * math.sin(M * math.pi / 180.0)

    # Calculate true anomaly (f)
    f = 2.0 * math.arctan(math.sqrt((1.0 + MARS_ORBIT_ECCENTRICITY) / (1.0 - MARS_ORBIT_ECCENTRICITY) * math.tan(E * math.pi / 180.0)))

    # Calculate distance from Earth to Mars in AU
    distance_au = MARS_ORBIT_SEMI_MAJOR_AXIS * (1.0 - MARS_ORBIT_ECCENTRICITY * math.cos(f * math.pi / 180.0))

    # Convert distance to meters
    distance_m = distance_au * AU

    # Account for Mars' perihelion distance
    distance_m += MARS_ORBIT_PERIHELION_DISTANCE - MARS_ORBIT_SEMI_MAJOR_AXIS

    return distance_m

# Test the function
date_time = datetime.datetime(2023, 3, 20, 12, 0, 0)  # March 20, 2023, 12:00:00 UTC
distance = calculate_distance_to_mars(date_time)
print(f"Distance from Earth to Mars on {date_time}: {distance:.2f} meters")