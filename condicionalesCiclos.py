

""" PUNTO 3 """




hemoglobina = float(input("Digite el nivel de hemoglobina en sangre: "))
tiempo = input("Digite su edad acompañado de la palabra meses o años segun corresponda ")
tiempo= tiempo.split(" ")
edad = int(tiempo[0])
sexo = input("Digite su sexo: ")
anemia = False

if tiempo[1]== "meses":
    if edad <=1 and edad >=0 and hemoglobina <13:
        anemia = True
    elif edad >1 and edad <=6 and hemoglobina <10:
        anemia = True
    elif edad >6 and edad <=12 and hemoglobina <11:
        anemia = True
elif tiempo[1]== "años":
    if edad >1 and edad <=5 and hemoglobina <11.5:
        anemia = True 
    elif edad >5 and edad <=10 and hemoglobina <12.6:
        anemia = True 
    elif edad >10 and edad <=15 and hemoglobina <13:
        anemia = True 
    elif edad > 15:
        if sexo == "mujer" and hemoglobina<12:
            anemia = True
        elif sexo =="hombre" and hemoglobina <14:
            anemia = True

if (anemia):
    print("Usted tiene anemia")
else:
    print("Usted NO  tiene anemia")






