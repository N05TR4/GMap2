from geopy.geocoders import Nominatim
from geopy.distance import distance
import geopy

# Calular la distancia entre un lugar y otro
geo = Nominatim(user_agent="GMap")
lugar_Origen = input("Ingresa la ciudad o pais de Origen \n")
lugar_Destino = input("Ingresa la ciudad o pais de de Destino \n")
ciudad1 = geo.geocode(lugar_Origen)
ciudad2 = geo.geocode(lugar_Destino)

coord1 = (ciudad1.longitude, ciudad1.latitude)
coord2 = (ciudad2.longitude, ciudad2.latitude)

print(coord1)
print(coord2)

dist = geopy.distance.distance(coord1, coord2)
print(format(f"La distancia entre {lugar_Origen} y {lugar_Destino} es de: ") + str(dist))
