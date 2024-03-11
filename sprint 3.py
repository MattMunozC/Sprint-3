import random
import re
from pprint import pprint
def createPassword(passlen:int)->str:
    letter="qwertyuiopasdfghjklñzxcvbnm"
    random_letter=lambda : random.choice([letter.upper()[random.randint(0,len(letter))-1],letter.lower()[random.randint(0,len(letter)-1)],str(random.randint(0,9))])
    return "".join([random_letter() for i in range(passlen)])
def setUser(name:str)->dict:
    username=lambda name:"".join([name.split(" ")[0][:3:],name.split(" ")[1][:3:]])
    return {"username":username(name).replace("ñ","n").lower(),"name":name,"password":createPassword(8)}
def validate_phone(phonenumber:int)->bool:
    if len(phonenumber)!=8:
        return False
    if not phonenumber.isdigit():
        return False
    return True

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
    users=[]
    for user in names:
        users.append(setUser(user))
    for i in users:
        phonenumber=input(f"{i['username']}. Ingrese su numero de telefono: ")
        while not validate_phone(phonenumber):
            print("numero no valido")
            phonenumber=input(f"{i['username']}. Ingrese un numero valido: ")
        i["phonenumber"]=phonenumber