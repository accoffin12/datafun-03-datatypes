"""Alexandra Coffin
Data Analytics Fundementals
1/29/2023
Formula 1 team list
track_miles in km rounded to nearest intiger"""

import math
import statistics
import decimal
import numbers as np


ytrack_km = [5.412, 6.17, 5.27, 6.003, 5.412, 4.909, 3.337, 4.675, 4.361, 4.318, 5.891, 4.381, 7.004, 4.259, 5.793, 5.063, 5.807, 5.38, 5.513, 4.304, 4.309, 5.281]
print("track_km:", ytrack_km)
print()

"""Times conversted from (min., sec.) to seconds."""
#times will not appear without proper notation
fastest_lap_rec = [78.6, 78, 72, 85.8, 78.6, 69, 70.8, 70.8, 67.8, 63.6, 76.2, 70.2, 87.6, 66.6, 72.6, 85.2, 78.6, 73.8, 81.6, 70.8, 66.6, 75.6]
x_times = [59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80]

"""List Statistics"""
mean = statistics.mean((fastest_lap_rec))
print("mean:", (mean))
print()
median = statistics.median((fastest_lap_rec))
print("median:", (median))
print()
mode = statistics.mode(fastest_lap_rec)
print("mode:", (mode))

asc_track_list: sorted(ytrack_km)
desc_track_list: sorted(ytrack_km, reverse=True)
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------#
"""Corellation, Standard Deviation, Variance"""
correlationxy = statistics.correlation(x_times, ytrack_km)
stdev = statistics.stdev(ytrack_km)
variance = statistics.variance(ytrack_km)
print()
print("Correlation:", (correlationxy))
print( "Standard Deviation:", (stdev))
print("Variance:", (variance))
print()
slope, intercept = statistics.linear_regression(x_times, ytrack_km)
print("slope:", (slope))
print()
#---------------------------------------------------------------------------------------------------------------------------------------------------#
"""Time Functions"""
x_max = max(fastest_lap_rec)
new_mx = x_max * 15
new_y = slope * new_mx * intercept
print("x_max:", (x_max)) 
print("new x max after 15:", (new_mx))
print( "new y:", (new_y))

len_times = len(fastest_lap_rec)
print("Length of time list:", (len_times))

#----------------------------------------------------------------------------------------------------------------------------------------------------#
"""Track Functions"""
sum_lap_km = sum(ytrack_km)
len_lap_km = len(ytrack_km)
average_track = sum_lap_km / len_lap_km

print("Sum of km per lap for all tracks:", (sum_lap_km), \
    "number of tracks:", (len_lap_km), \
        "average number of km per track:", (average_track))
print()
#-----------------------------------------------------------------------------------------------------------------------------------------------------#
if __name__ == "__main__":
    x_year = [2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019]
    y_winner_points = [172, 498, 650, 460, 596, 701, 703, 765, 688, 655, 739]
    x_year.append([2020, 2021, 2022])

    y_winner_points.extend([650, 498, 172])
    print("New list of years", (x_year), "and extended points", (y_winner_points))
    
    """Inserting and removing a new year."""
    i = 6
    new_value = 500
    y_winner_points.insert(i, new_value)
    
    item_removal = 500
    y_winner_points.remove(item_removal)

    """Count and Sort"""
    ct_of_700 = y_winner_points.count(700)
    asc_points = sorted(y_winner_points)
    desc_points = sorted(y_winner_points, reverse=True)

    print("Ascending Points:", (asc_points), \
        \
            "Descending points:", (desc_points), \
                \
            "Count of 700:", (ct_of_700))
    #--------------------------------------------------------------------------------------------------------------------------------------------------------------#
    """Filtering Points"""
    Points_under_600 = [map(lambda x: x < 600, y_winner_points)]
    print(Points_under_600)
    print()
    def is_odd(x):
        """Returns only if x is odd."""
        return x % 2 !=0
    list_odd = list(filter(is_odd, y_winner_points))
    print("List of odd Points entries", (list_odd))

    """Cube Root and Area of a Cube."""
    cube_root = [(x, x**(1./3)) for x in y_winner_points]
    area_cube = [(x, x **3) for x in y_winner_points]

    print("Cube Root:", (cube_root))
    print()
    print()
    print("Area of Cube:", (area_cube))
    print()



    #---------------------------------------------------------------------------------------------------------------------------------------------------------------#
""" Copying lists"""
new_track_km = ytrack_km.copy()
# Copy track_km

first = new_track_km.pop(0)
last = new_track_km.pop(-1)

"""Converting km to mi"""
#1 km = 0.621371

miles = list(map(lambda x: x* 0.621371, new_track_km))
print("Track length km - mi conversion", (miles))
