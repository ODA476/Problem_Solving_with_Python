"""*3.3 (Geography: estimate areas) Find the GPS locations for Atlanta, Georgia; Orlando, Florida; Savannah,
Georgia; and Charlotte, North Carolina from www.gps-data-team.com/map/ and compute the estimated area enclosed by
these four cities. (Hint: Use the formula in Programming Exercise 3.2 to compute the distance between two cities.
Divide the polygon into two triangles and use the formula in Programming Exercise 2.14 to compute the area of a
triangle.)
"""

import math

# Example GPS coordinates (in degrees) for Atlanta, GA
atlanta_lat = 33.7490
atlanta_lon = -84.3880

# Example GPS coordinates (in degrees) for Orlando, FL
orlando_lat = 28.5383
orlando_lon = -81.3792

# Example GPS coordinates (in degrees) for Savannah, GA
savannah_lat = 32.0836
savannah_lon = -81.0998

# Example GPS coordinates (in degrees) for Charlotte, NC
charlotte_lat = 35.2271
charlotte_lon = -80.8431

# Earth's radius in kilometers
earth_radius_km = 6371.01

# Calculate distances between cities using haversine formula

# distance_atlanta_savannah
side1 = earth_radius_km * math.acos(math.sin(atlanta_lat) * math.sin(savannah_lat) + math.cos(atlanta_lat) * math.cos(savannah_lat) * math.cos(atlanta_lon - savannah_lon))

# distance_atlanta_orlando
side2 = earth_radius_km * math.acos(math.sin(atlanta_lat) * math.sin(orlando_lat) + math.cos(atlanta_lat) * math.cos(orlando_lat) * math.cos(atlanta_lon - orlando_lon))

# distance_savannah_orlando
side3 = earth_radius_km * math.acos(math.sin(savannah_lat) * math.sin(orlando_lat) + math.cos(savannah_lat) * math.cos(orlando_lat) * math.cos(savannah_lon - orlando_lon))

# distance_savannah_charlotte
side4 = earth_radius_km * math.acos(math.sin(savannah_lat) * math.sin(charlotte_lat) + math.cos(savannah_lat) * math.cos(charlotte_lat) * math.cos(savannah_lon - charlotte_lon))

# distance_charlotte_atlanta
side5 = earth_radius_km * math.acos(math.sin(charlotte_lat) * math.sin(atlanta_lat) + math.cos(charlotte_lat) * math.cos(atlanta_lat) * math.cos(charlotte_lon - atlanta_lon))

side6 = side1

# compute triangle_1 (atlanta, savannah, orlando) area
s1 = (side1 + side2 + side3) / 2.0
area_1 = math.sqrt(s1 * (s1 - side1) * (s1 - side2) * (s1 - side3))

# compute triangle_2 (atlanta, savannah, charlotte) area
s2 = (side4 + side5 + side6) / 2.0
area_2 = math.sqrt(s2 * (s2 - side4) * (s2 - side5) * (s2 - side6))

# display the result
print('triangle_1 (atlanta, savannah, orlando) area is', area_1)
print('triangle_2 (atlanta, savannah, charlotte) area is', area_2)
