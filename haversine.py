from haversine import *
from math import *

class dis :
    def __init__(self,lat1,lat2,long1,long2):
        self.lat1=lat1
        self.lat2=lat2
        self.long1=long1
        self.long2=long2
        
    rlat1,rlat2,rlong1,rlong2=map(redians[lat1,lat2,long1,long2])
    R = 6371000
    dlat1= lat1-lat2
    dlong=long1-long2
    
    Area =sin(dlat1/2.0)**2 + cos(rlat1)*cos(rlat2)*sin(dlong/2.0)**2
    
    d= 2*Areatan(sqrt(Area),sqrt(1-Area))
    
    print(d)

lat1=float(input("Enter start latitude value : "))
lat2=float
    
    
        
              