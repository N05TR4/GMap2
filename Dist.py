from tkinter import *
from geopy.geocoders import Nominatim
from geopy.distance import distance
import geopy

global ventana
ventana = Tk()
ventana.geometry("600x500+400+125")
ventana.title("GeoB")
#ventana.iconbitmap("mini-goo.ico")
ventana.config(background="#000000")
Titulo = Label(text="GeoB", font=("Cambria", 20), bg="#24b43c", fg="white", width="500", height="2")
Titulo.pack()
Titulo1 = Label(text="Creador: N05TR@  Version: 1.0", font=("Cambria", 10), bg="#24b43c", fg="white", width="500", height="1")
Titulo1.pack()
Titulo1 = Label(text="", font=("Cambria", 15), bg="#24b43c", fg="white", width="500", height="1")
Titulo1.place(x = 0, y = 455)

# Agregandole una imagen
image = PhotoImage(file="mini-goo.gif")
image = image.subsample(2, 2)
label = Label(image=image)
label.place(x=450, y=10)

# Variable principal
lugar_Origen = StringVar()
lugar_destino = StringVar()








if __name__ == '__main__':
    ventana.mainloop()
