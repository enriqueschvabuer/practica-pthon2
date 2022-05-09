sw = True




def write():
    names = []
    with open("./archivos/name.txt", "w" , encoding="utf-8") as f:
        for name in names:
            f.write(name)
            f.write('\n')




def agregar_nombre():
    nombre = input("Ingrese el nombre a agregar: ")
    with open("./archivos/name.txt", "a" , encoding="utf-8") as f:
        f.write(nombre)
        f.write("\n")




def read():
    names = []
    with open("./archivos/name.txt", "r", encoding="utf-8") as f:
        for line in f: 
            if len(line.strip()) > 0:
                names.append(line.strip())
    if len(names)> 0:
        print(names)
    else:
        print("Archivo vacio")




def borrar_nombre():
    nombre = input("Ingrese el nombre a borrar : ")
    names = []
    with open("./archivos/name.txt", "r", encoding="utf-8") as f:
        for line in f: 
            if len(line.strip()) > 0 and line.strip()!= nombre:
                names.append(line.strip())
    with open("./archivos/name.txt", "w" , encoding="utf-8") as f:
        for name in names:
            f.write(name)
            f.write('\n')
    print(names)




def exit():
    global sw
    sw= False
    print("Programa Terminado!")




def error():
    print("Error seleccione una opcion correcta")




def run():
    switch_options = {
        1: write,
        2: agregar_nombre,
        3: read,
        4: borrar_nombre,
        5: exit  
    }
    while sw:
            print("""  
----------------------------------------------------------------------
        Seleccione un numero:
        1. Crear un nuevo archivo 
        2. Agregar nombre
        3. Listar nombre
        4. Borrar nombre
        5. Salir del programa
----------------------------------------------------------------------
        """)
            n = int(input("Ingrese una opcion :   "))
            # if n == 1:
            #     write()
            # elif n == 2:
            #     nombre = input("Ingrese el nombre a agregar: ")
            #     agregar_nombre(nombre)
            # elif n == 3:
            #     read()
            # elif n == 4:
            #     nombre = input("Ingrese el nombre a borrar : ")
            #     borrar_nombre(nombre)
            # elif n ==5:
            #     sw = False
            #     print("Programa Terminado!")
            switch_options.get(n, error)()

                


if __name__ == '__main__':
    run()