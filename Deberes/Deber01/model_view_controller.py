# model_view_controller.py
import basic_backend
import mvc_exceptions as mvc_exc
import json
import inicio


class ModelBasic(object):

    def __init__(self, tipo, autor = ""):
        self._item_type = tipo
        self.create_items(tipo, autor)

    @property
    def item_type(self):
        return self._item_type

    @item_type.setter
    def item_type(self, new_item_type):
        self._item_type = new_item_type

    def create_item(self, nuevoAutor):
        basic_backend.create_item(nuevoAutor)

    def create_items(self, tipo, autor):
        basic_backend.create_items(tipo, autor)

    def read_item(self, name):
        return basic_backend.read_item(name)

    def read_items(self):
        return basic_backend.read_items()

    def update_item(self, name):
        basic_backend.update_item(name)

    def delete_item(self, name):
        basic_backend.delete_item(name)

class View(object):

    @staticmethod
    def show_bullet_point_list(item_type, items):
        print('--- {} LIST ---'.format(item_type.upper()))
        for item in items:
            print(f''' 
    ID Autor: {item.authorid} 
    Nombre: {item.name}
    Cantidad de libros: {item.workcount}
    Cantidad de fans: {item.fan_count}
    Bio: {item.about[:100]+"..."}
    Pais: {item.country}
                ''')

    @staticmethod
    def show_number_point_list(item_type, items):
        print('--- {} LIST ---'.format(item_type.upper()))
        if (item_type == 'autores'):
            for i, item in enumerate(items):
                print(f''' 
    ID Autor: {item['authorid']} 
    Nombre: {item['name']}
    Cantidad de libros: {item['workcount']}
    Cantidad de fans: {item['fan_count']}
    Bio: {item['about'][:100]+"..."}
    Pais: {item['country']}
                ''')
        elif item_type == 'libros':
            for i, item in enumerate(items):
                print(f''' 
    ID Libro: {item['id']} 
    Titulo libro: {item['title']}
    Autores: {item['authors']}
                ''')

    @staticmethod
    def show_item(item_type, item, item_info):
        print('//////////////////////////////////////////////////////////////')
        print('Buenas noticias, si tenemos algo de {}!'.format(item.upper()))
        print('{} INFO:'.format(item_type.upper()))
        if (item_type == 'autores'):
            print(f''' 
    ID Autor: {item_info['authorid']} 
    Nombre: {item_info['name']}
    Cantidad de libros: {item_info['workcount']}
    Cantidad de fans: {item_info['fan_count']}
    Bio: {item_info['about'][:100]+"..."}
    Pais: {item_info['country']}
                ''')
        elif item_type == 'libros':
            print(f''' 
    ID Libro: {item_info['id']} 
    Titulo libro: {item_info['title']}
    Autores: {item_info['authors']}
                ''')        
        print('//////////////////////////////////////////////////////////////')

    @staticmethod
    def display_missing_item_error(item, err):
        print('**************************************************************')
        print('Lo sentimos, no tenemos a {}!'.format(item.upper()))
        print('{}'.format(err.args[0]))
        print('**************************************************************')

    @staticmethod
    def display_item_already_stored_error(item, item_type, err):
        print('**************************************************************')
        print('Hey! Ya tenemos a {} en nuestra lista de {}!'
              .format(item.upper(), item_type))
        print('{}'.format(err.args[0]))
        print('**************************************************************')

    @staticmethod
    def display_item_not_yet_stored_error(item, item_type, err):
        print('**************************************************************')
        print('No tenemos nada de {} en nuestra lista de {}. Se el primero en agregar algo!'
              .format(item.upper(), item_type))
        print('{}'.format(err.args[0]))
        print('**************************************************************')

    @staticmethod
    def display_item_stored(item, item_type):
        print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
        print('Felicidades! Acaba de agregar informacion de {} a nuestra lista de {}!'
              .format(item.upper(), item_type))
        print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')

    @staticmethod
    def display_change_item_type(older, newer):
        print('---   ---   ---   ---   ---   ---   ---   ---   ---   ---   --')
        print('Cambiando el tipo de "{}" a "{}"'.format(older, newer))
        print('---   ---   ---   ---   ---   ---   ---   ---   ---   ---   --')

    @staticmethod
    def display_item_updated(item, o_price, o_quantity, n_price, n_quantity):
        print('---   ---   ---   ---   ---   ---   ---   ---   ---   ---   --')
        print('Cambiada bio de {} de: {} --> {}'
              .format(item, o_price, n_price))
        print('Cambiado pais de {} de: {} --> {}'
              .format(item, o_quantity, n_quantity))
        print('---   ---   ---   ---   ---   ---   ---   ---   ---   ---   --')

    @staticmethod
    def display_item_deletion(name, item_type):
        print('--------------------------------------------------------------')
        print('Se acaba de remover {} de la lista de {}'.format(name, item_type))
        print('--------------------------------------------------------------')

class Controller(object):

    def __init__(self, model, view):
        self.model = model
        self.view = view

    def show_items(self, bullet_points=False):
        items = self.model.read_items()
        item_type = self.model.item_type
        if bullet_points:
            self.view.show_bullet_point_list(item_type, items)
        else:
            self.view.show_number_point_list(item_type, items)

    def show_item(self):
        entrada = {
            'autores' : "A quien deseas buscar? : ",
            'libros' : "Que libro deseas buscar? : "
        }
        item_name = input(entrada[self.model.item_type])
        try:
            item = self.model.read_item(item_name)
            item_type = self.model.item_type
            self.view.show_item(item_type, item_name, item)
        except mvc_exc.ItemNotStored as e:
            self.view.display_missing_item_error(item_name, e)
        return item_name

    def insert_item(self):
        item_type = self.model.item_type
        print(f"CREANDO nuevo {item_type.upper()}\n")
        name = input("Nombre: ")
        try:
            self.model.create_item(name)
            self.view.display_item_stored(name, item_type)
        except mvc_exc.ItemAlreadyStored as e:
            self.view.display_item_already_stored_error(name, item_type, e)

    def update_item(self):
        item_type = self.model.item_type
        if item_type == "autores":
            name = input("A quien deseas actualizar? : ")
        else:
            name = input("Que libro deseas actualizar? : ")

        try:
            older = self.model.read_item(name)
            self.model.update_item(name)
            #self.view.display_item_updated
            # (name, older['price'], older['quantity'], price, quantity)
        except mvc_exc.ItemNotStored as e:
            self.view.display_item_not_yet_stored_error(name, item_type, e)
            # if the item is not yet stored and we performed an update, we have
            # 2 options: do nothing or call insert_item to add it.
            # self.insert_item(name, price, quantity)

    def update_item_type(self, new_item_type):
        old_item_type = self.model.item_type
        self.model.item_type = new_item_type
        self.view.display_change_item_type(old_item_type, new_item_type)

    def delete_item(self):
        item_type = self.model.item_type
        if item_type == "autores":
            name = input("A quien deseas borrar? : ")
        else:
            name = input("Que libro deseas borrar? : ")
        try:
            self.model.delete_item(name)
            self.view.display_item_deletion(name, item_type)
        except mvc_exc.ItemNotStored as e:
            self.view.display_item_not_yet_stored_error(name, item_type, e)


def inicializarLibros(autorElegido):
    controllerBooks = Controller(ModelBasic("libros",autorElegido), View())
    accionesAutor = {
    '1' : controllerBooks.show_item,
    '2' : controllerBooks.insert_item,
    '3' : controllerBooks.update_item,
    '4' : controllerBooks.delete_item,
    '5' : controllerBooks.show_items
    }
    return controllerBooks, accionesAutor


# c.show_items()
# # c.show_item(input("Ingrese el nombre a buscar : ")) #no hay choocolate READY
# # c.show_item('Stephen King')  #si hay bread READY
# # c.insert_item() # pero ya hay bread READY
# c.insert_item() #no hay chocolate READY
# c.show_item(input("De quien deseas buscar? : ")) #READY
# c.update_item(input("De quien deseas actualizar? : ")) #READY
# c.delete_item(input("A quien deseas borrar? : ")) #no hay fish

controllerAuthors = Controller(ModelBasic("autores"), View())

acciones = {
    '1' : controllerAuthors.show_item,
    '2' : controllerAuthors.insert_item,
    '3' : controllerAuthors.update_item,
    '4' : controllerAuthors.delete_item,
    '5' : controllerAuthors.show_items
}


controllerAuthors.show_items()

opcionesAutor = '''
    Ingresa un numero para:
    1. Ver un autor
    2. Agregar un autor a la lista
    3. Actualizar un autor de la lista
    4. Borrar un autor de la lista
    5. Desplegar todos los autores
  ->'''
opcionesLibros = '''
    Ingresa un numero para:
    1. Buscar un libro del autor
    2. Agregar libros al autor
    3. Actualizar un libro del autor
    4. Borrar un libro del autor
    5. Desplegar todos los libros del autor
    6. Volver
  ->'''

while(1):
    seleccionMenu1 = input(opcionesAutor)
    if (int(seleccionMenu1) < 6 and int(seleccionMenu1) > 0):
        autorElegido = acciones[seleccionMenu1]()
        if (int(seleccionMenu1) == 1):

            controllerBooks, accionesAutor = inicializarLibros(autorElegido)
            controllerBooks.show_items()
            while (1):
                seleccion = input(opcionesLibros)
                if (int(seleccion) < 6 and int(seleccion) > 0):
                    accionesAutor[seleccion]()
                elif ( int(seleccion) == 6 ):
                    break
                else:
                    print("Error debes elegir un numero del 1 al 6")
    else:
        print("Error debes elegir un numero del 1 al 5")

