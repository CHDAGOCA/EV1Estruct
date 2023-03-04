registro_libro={}
while True:
    menu_principal=input("Bienvenido a la biblioteca universitaria\n ¿Que accion deseas realizar? \n[1]Registrar un nuevo ejemplar \n[2]Consultas y reportes \n[3]Salir \n")
    if menu_principal== "1":
        while True:
                titulo=input("\nTitulo del libro ")
                if titulo.strip() == '': 
                    break
                autor=input(f"Ingrese el autor de {titulo} ")
                if autor.strip() == '':
                    break
                genero=input(f"Ingrese el genero al que pertenece ")  
                if genero.strip() == '':
                    genero=input(f"El genero del libro es un dato obligatorio ") 
                publicacion=input("Ingrese la fecha de publicación")
                if publicacion.strip() == '':
                    publicacion=input(f"La fecha de publicacion es un campo obligatorio ")
                isbn=input("Agregue el ISBN del libro a registrar")
                if isbn.strip() == '':
                    isbn=input(f"El ISBN del libro es un dato obligatorio ")
                fecha_adquisicion=input("Ingrese la fecha en la que se adquirio el libro")
                if fecha_adquisicion.strip() == '':
                    fecha_adquisicion=input(f"La fecha en que se adquirio el libro es un dato obligatorio ")

                if registro_libro:
                  identificador = max(registro_libro) +1
                else:
                  identificador = 1 

                registro_libro[identificador] = [autor, genero, publicacion, isbn, fecha_adquisicion]
                print(registro_libro.keys)


    elif menu_principal=="2":
        while True:
            sub_menu=input("Consultas y Reportajes\n ¿Que accion deseas realizar? \n[1] Consulta por titulo \n[2] Reportajes \n[3] Volver al menú Principal \n")
            sub_menu = int(sub_menu)
            if sub_menu == 3:
                break
            if sub_menu == 1:
                while True:
                    consulta_titulo=input("Consulta por Titulo \n ¿Que accion deseas realizar? \n[1] Por titulo \n[2] Por ISBN \n[3] Volver al menú de consultas y reportajes \n")
                    consulta_titulo = int(consulta_titulo)
                    if consulta_titulo == 3:
                        break
                    if consulta_titulo == 1:
                        titulo= input("Ingresa el titulo del libro a buscar: ")
                    if titulo in registro_libro:
                        pass
                if consulta_titulo == 2:
                    isbn= input("Ingresa el titulo del libro a buscar: ")
                    if isbn in registro_libro:
                        pass
                else:
                    print("La opcion ingresada no es correcta, elija de nuevo") 
            if sub_menu == 2:
                reportajes = input("Reportajes \n ¿Que accion deseas realizar? \n[1] Catalogo Completo \n[2] Reportaje por autor \n[3] Reportaje por genero \n[4] Por año de publicacion \n [5] volver al menu de reportaje \n")
            else:
                print("La opcion ingresada no es correcta, elija de nuevo")
            
    elif menu_principal=="3":
        print("Gracias por visitarnos, vuelva pronto")
        break
    else:
        print("La opcion ingresada no es correcta, elija de nuevo")
