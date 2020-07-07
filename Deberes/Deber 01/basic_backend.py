# basic_backend.py
import mvc_exceptions as mvc_exc
from inicio import Autor,Libro
import json

items = list()  # global variable where we keep the data
typeof = ""
pathFile = {
    'autores' : "authorD.json",
    'libros' : "librosJ.json"
}

def create_item(name):
    global items
    if (typeof == 'autores'):
        results = list(filter(lambda x: x['name'] == name, items))
    else:
        results = list(filter(lambda x: x['title'] == name, items))

    if results:
        raise mvc_exc.ItemAlreadyStored('"{}" ya almacenado!'.format(name))
    else:

        if (typeof == 'autores'):
            nuevo = {
                'authorid' : len(items)+1,
                'name' : name,
                'workcount' : 0,
                'fan_count' : 0,
                'image_url' : 0,
                'about' : input("Bio: "),
                'country' : input("Pais: ")
            }
        else:
            nuevo = {
                'id' : len(items)+1,
                'title' : name,
                'authors' : input("Ingresa los autores separados por comas")
            }

        items.append(nuevo)
        try:
            with open(pathFile[typeof],'w') as filehandle: #a -> append
                json.dump(items,filehandle,indent=2, separators=(',', ': '))
                filehandle.close()
        except Exception as Error:
            print("Error leyendo archivo")


def create_items(tipo, autor):
    global items
    global typeof
    typeof = tipo
    #for item in app_items:
    #    items.append(Autor(item))
    if (tipo == 'autores'):
        with open(pathFile[tipo], "r") as read_file:
                data = json.load(read_file)
    else:
        with open("librosJ.json", "r") as read_file:
            dataBooks = json.load(read_file)
        data = list(filter(lambda x: autor in x['authors'], dataBooks))
    items = data


def read_item(name):
    global items
    myitems = list(filter(lambda x: x['name'] == name, items))
    if myitems:
        return myitems[0]
    else:
        raise mvc_exc.ItemNotStored(
            'No puedes obtener nada de "{}" porque no existen registros'.format(name))


def read_items():
    global items
    return [item for item in items]


def update_item(name):
    global items
    # Python 3.x removed tuple parameters unpacking (PEP 3113), so we have to do it manually (i_x is a tuple, idxs_items is a list of tuples)
    idxs_items = list(
        filter(lambda i_x: i_x[1]['name'] == name, enumerate(items)))
    if idxs_items:
        i, item_to_update = idxs_items[0][0], idxs_items[0][1]
        items[i] = {'authorid' : items[i]['authorid'],
                    'name' : input("Ingresa el nuevo nombre: "),
                    'workcount' : 0,
                    'fan_count' : 0,
                    'image_url' : 0,
                    'about' : input("Ingresa la nueva bio: "),
                    'country' : input("Ingresa el nuevo pais: ")
                    }
        try:
            with open(pathFile,'w') as filehandle: #a -> append
                json.dump(items,filehandle,indent=2, separators=(',', ': '))
                filehandle.close()
        except Exception as Error:
            print("Error leyendo archivo")
        print(items[i])
    else:
        raise mvc_exc.ItemNotStored(
            'No se puede actualizar "{}" porque no existen registros'.format(name))


def delete_item(name):
    global items
    # Python 3.x removed tuple parameters unpacking (PEP 3113), so we have to do it manually (i_x is a tuple, idxs_items is a list of tuples)
    idxs_items = list(
        filter(lambda i_x: i_x[1]['name'] == name, enumerate(items)))
    if idxs_items:
        i, item_to_delete = idxs_items[0][0], idxs_items[0][1]
        del items[i]
        try:
            with open(pathFile,'w') as filehandle: #a -> append
                json.dump(items,filehandle,indent=2, separators=(',', ': '))
                filehandle.close()
        except Exception as Error:
            print("Error leyendo archivo")
    else:
        raise mvc_exc.ItemNotStored(
            'No se puede borrar "{}" porque no existen registros'.format(name))


def main():

   

    # CREATE
    create_item('beer', price=3.0, quantity=15)
    # if we try to re-create an object we get an ItemAlreadyStored exception
    # create_item('beer', price=2.0, quantity=10)

    # READ
    print('READ items')
    print(read_items())
    # if we try to read an object not stored we get an ItemNotStored exception
    # print('READ chocolate')
    # print(read_item('chocolate'))
    print('READ bread')
    print(read_item('bread'))

    # UPDATE
    print('UPDATE bread')
    update_item('bread', price=2.0, quantity=30)
    print(read_item('bread'))
    # if we try to update an object not stored we get an ItemNotStored exception
    # print('UPDATE chocolate')
    # update_item('chocolate', price=10.0, quantity=20)

    # DELETE
    print('DELETE beer')
    delete_item('beer')
    # if we try to delete an object not stored we get an ItemNotStored exception
    # print('DELETE chocolate')
    # delete_item('chocolate')

    print('READ items')
    print(read_items())

if __name__ == '__main__':
    main()