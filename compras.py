dic = {
    "Frutas":{
        "uva":1800,
        "manzanas":2500,
        "platanos":1200,
        "fresas":3000,
        "piñas":2000
        },
    "Verduras":{
        "zanahorias":1500,
        "tomates":2000,
        "espinacas":2500,
        "cebollas":1800,
        "pepinos":1700
        },
    "Cereales":{
        "arroz":2500,
        "avena":3000,
        "maiz":2000,
        "quinua":6000,
        "trigo":3500
        },
    "Carnes":{
        "pollo":8000,
        "res":12000,
        "cerdo":10000,
        "pescado":15000,
        "tofu":5000
        }
       }
for key in dic:
    print(key, end=":\n")
    for a in dic[key]:
        print("\t",a,":",dic[key][a])