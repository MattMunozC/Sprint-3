import random
import re
from pprint import pprint
def validatePassword(password:str)->bool:
    mayus="[A-Z]"
    minus="[a-z]"
    num="[0-9]"
    if not bool(re.search(mayus,password)):
        return False
    if not bool(re.search(minus,password)):
        return False
    if not bool(re.search(num,password)):
        return False
    return True
def createPassword(passlen:int)->str:
    #Variable que define el rango de caracteres permitidos
    letter="qwertyuiopasdfghjklñzxcvbnm"
    #random letter es una funcion anonima que entrega una funcion de la lista utilizando random.choice
    #opciones:
    #   letter.upper() son los caracteres admisibles en mayuscula: será un caracter en la posicion aleatorio entre 0 y la longitud de letter con 1 paso de desfase
    #   letter.upper() son los caracteres admisibles en minuscula: será un caracter en la posicion aleatorio entre 0 y la longitud de letter con 1 paso de desfase
    #   un valor aleatorio entre 0 o 9
    random_letter=lambda : random.choice([letter.upper()[random.randint(0,len(letter))-1],letter.lower()[random.randint(0,len(letter)-1)],str(random.randint(0,9))])
    while 1:
        #mientras la contraseña no sea valida, creara una nueva contraseña hasta encontrar una valida
        password="".join([random_letter() for i in range(passlen)])
        if validatePassword(password):
            return password
def setUser(name:str)->dict:
    username=lambda name:"".join([name.split(" ")[0][:3:],name.split(" ")[1][:3:]])
    return {"username":username(name).replace("ñ","n").lower(),"name":name,"password":createPassword(8)}
def validate_phone(phonenumber:int)->bool:
    if len(phonenumber)!=8:
        return False
    if not phonenumber.isdigit():
        return False
    return True
def createuser(names:list)->list:
    #otorga un usuario a cada nombre
    return [setUser(user) for user in names]
if __name__=="__main__":
    names = [
        "Sofía García",
        "Alejandro Martínez",
        "Valentina López",
        "Diego Rodríguez",
        "Camila Fernández",
        "Mateo Pérez",
        "Isabella González",
        "Lucas Sánchez",
        "Valeria Ramírez",
        "Nicolás Torres"
    ]
    users=createuser(names)
    for i in users:
        phonenumber=input(f"{i['username']}. Ingrese su numero de telefono: ")
        while not validate_phone(phonenumber):
            print("numero no valido")
            phonenumber=input(f"{i['username']}. Ingrese un numero valido: ")
        i["phonenumber"]=phonenumber
