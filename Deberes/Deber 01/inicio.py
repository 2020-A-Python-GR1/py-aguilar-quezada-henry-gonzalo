import json


class Libro:
    __nombre = ""
    __isbn = ""
    __shortDescription = ""
    __categories = []
    __authors = []

    def __init__(self,color):     #self = this
        print("Empezo el constructor")
        self.color = color
    
    def setear_chasis(self, numero_chasis):
        self.__numero_chasis = numero_chasis
        return self.__calculo_chasis()

    def __calculo_chasis(self):
        return self.__numero_chasis * 1.17

    def __str__(self):
        return f"Color: {self.color} \nNumero Chasis: {self.__numero_chasis}"

class Autor:
    __authorid = ""
    __name = ""
    __workcount = 0
    __fan_count = 0
    __image_url = ""
    __about = ""
    __country = ""

    def __init__(self,item):     #self = this
        self.__authorid = item['authorid']
        self.__name = item['name']
        self.__workcount = item['workcount']
        self.__fan_count = item['fan_count']
        self.__image_url = item['image_url']
        self.__about = item['about']
        self.__country = item['country']

    def __str__(self):
        return f''' 
    ID Autor: {self.__authorid} 
    Nombre: {self.__name}
    Cantidad de libros: {self.__workcount}
    Cantidad de fans: {self.__fan_count}
    Bio: {self.__about[:100]+"..."}
    Pais: {self.__country}
                '''




#nuevo_libro = Libro("Azul")
#with open("data_file.json", "r") as read_file:
#    data = json.load(read_file)
#print(nuevo_auto.color)
#print(nuevo_auto.setear_chasis(120))
#print(nuevo_auto)