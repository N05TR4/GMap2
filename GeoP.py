from geopy.geocoders import Nominatim


#Creando Objeto de tipo Nominatim
lugar = input("Introduce la Calle, Avenida, Ciudad o Pais \n")
geo = Nominatim(user_agent="GMap")
localizacion = geo.geocode(lugar)
print(localizacion)
print(localizacion.latitude, localizacion.longitude)

18.4498922 -69.9716117

