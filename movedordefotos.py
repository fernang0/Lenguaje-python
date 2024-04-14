import os

num = str(input("Ingresa el ultimo numero de la foto que quieres mover: "))
while num != "":
    os.system("mv IMG_"+num+".JPG /home/ven0m/Imágenes/");
    num = str(input("Ingresa el ultimo numero de la foto que quieres mover: "))
