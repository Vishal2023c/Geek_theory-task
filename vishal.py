from math import *


class Distance:
    def __init__(self, lat1, long1, lat2, long2):
        self.lat1 = lat1
        self.long1 = long1
        self.lat2 = lat2
        self.long2 = long2

        lat1, long1, lat2, long2 = map(radians, [lat1, long1, lat2, long2])

        dlat = lat2-lat1
        dlong = long2-long1

        # calculate area
        area = sin(dlat/2.0)**2 + cos(lat1) * cos(lat2) * sin(dlong/2.0)**2

        # measure distance
        d = 2 * atan(sqrt(area) * sqrt(1-area))

        result = d*6371
        print(result)


lat1 = float(input("Enter start point letitude value: "))
long1 = float(input("Enter start point longitude value: "))
lat2 = float(input("Enter end point letitude value: "))
long2 = float(input("Enter end point longitude value: "))

#lat1, long1 = 22.962267, 76.050797
#lat2, long2 = 23.179300, 75.784912

dist = Distance(lat1, long1, lat2, long2)
