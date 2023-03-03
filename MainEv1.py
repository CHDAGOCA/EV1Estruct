registro_libro={}
while True:
    menu_principal=input("Bienvenido a la biblioteca universitaria\n ¿Que accion deseas realizar? \n[1]Registrar un nuevo ejemplar \n[2]Consultas y reportes \n[3]Salir \n")
    if menu_principal== "1":
        while True:
                titulo=input("\nTitulo del libro: ")
                if titulo.strip() == '': 
                    break
                autor=input(f"Ingrese el autor de {titulo} ")
                if autor.strip() == '':
                    break
                genero=input(f"Ingrese el genero al que pertenece: ")  
                if genero.strip() == '':
                    genero=input(f"El genero del libro es un dato obligatorio ") 
                publicacion=input("Ingrese la fecha de publicación: ")
                if publicacion.strip() == '':
                    publicacion=input(f"La fecha de publicacion es un campo obligatorio ")
                isbn=input("Agregue el ISBN del libro a registrar: ")
                if isbn.strip() == '':
                    isbn=input(f"El ISBN del libro es un dato obligatorio ")
                fecha_adquisicion=input("Ingrese la fecha en la que se adquirio el libro: ")
                if fecha_adquisicion.strip() == '':
                    fecha_adquisicion=input(f"La fecha en que se adquirio el libro es un dato obligatorio ")

                if registro_libro:
                  identificador = max(registro_libro) +1
                else:
                  identificador = 1 

                registro_libro[identificador] = [autor, genero, publicacion, isbn, fecha_adquisicion]
                print(registro_libro.keys)


    elif menu_principal=="2":
        pass
    elif menu_principal=="3":
        print("Gracias por visitarnos, vuelva pronto")
        break
    else:
        print("La opcion ingresada no es correcta, elija de nuevo")
