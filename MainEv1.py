import datetime
registro_libro={}
def registro():
    print("-" * 40)
    print("Registro de libro")
    print("-" * 40)
    while True:
            while True:
                    while True: 
                        titulo=input("Ingresa el titulo del libro a registrar ")
                        if titulo.strip() == '': 
                            print("El titulo es un campo obligatorio ")
                        else: 
                            break
                    
                    while True:
                        autor=input(f"Ingrese el autor de {titulo} ")
                        if autor.strip() == '':
                            print("El Autor del libro es un campo obligatorio")
                        else: 
                            break

                    while True:
                        genero=input(f"Ingrese el genero al que pertenece ")
                        if genero.strip() == '':
                            print("El Genero del libro es un campo obligatorio")
                        else: 
                            break

                    while True:
                        publicacion=input(f"Ingrese el año de publicación del libro {titulo}  ")
                        fecha_procesada = datetime.datetime.strptime(publicacion, "%Y").date() 
                        fecha_actual = datetime.date.today()
                        if fecha_procesada > fecha_actual:
                            print("Esta fecha no es valida")
                        else:
                            break

                    while True:
                        fecha_adquisicion=input("Ingrese la fecha en la que se adquirio el libro (dd/mm/aaaa) ")
                        fecha2_procesada= datetime.datetime.strptime(fecha_adquisicion, "%d/%m/%Y").date() 
                        if fecha2_procesada < fecha_procesada :
                            print("La fecha de adquisicion debe ser despues de la fecha de publicacion, ingrese una fecha valida ")
                        else:
                            break

                    while True:
                        isbn=input(str(f"Ingresa la clave de ISBN del libro "))
                        if len(isbn) == 13:
                            break
                        else:
                            print("El ISBN debe tener 13 caracteres numericos, vuelva a ingresarlos ")

                    if registro_libro:
                        identificador = max(registro_libro) +1
                    else:
                        identificador = 1 

                    registro_libro[identificador] = [titulo, autor, genero, publicacion, fecha_adquisicion, isbn]
                    while True:
                            print("*" * 40)
                            print(f"Titulo: {titulo} \nAutor: {autor} \nGenero: {genero} \nFecha de publicacion: {publicacion} \nFecha de adquisición: {fecha_adquisicion} \nISBN: {isbn} \n") 
                            print("*" * 40)
                            confirmacion=input("¿Son correctos los datos ingresados? ").upper()
                            print("*" * 40)
                            if confirmacion=="SI":
                                for clave, valor in registro_libro.items():
                                    print("*" * 40)
                                    print(f"Se registro el libro\nfolio: {clave}\nDatos: {valor}")
                                    print("*" * 40)
                                break
                            else: 
                                print("Vuelva a ingresar los datos")
                                if identificador in registro_libro:
                                    titulo, autor, genero, publicacion, fecha_adquisicion, isbn= registro_libro[identificador]
                                    del registro_libro[identificador]
                                
                    break
            nuevo_registro=input("¿Deseas realizar un nuevo registro? ").upper()
            if nuevo_registro=="SI":
                continue 
            if nuevo_registro=="NO":
                print("*" * 40)
                print("Sus registros han quedado guardados")
                print(registro_libro)
                break

def consultas():
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
            
while True:
    menu_principal=input("Bienvenido a la biblioteca universitaria\n ¿Que accion deseas realizar? \n[1]Registrar un nuevo ejemplar \n[2]Consultas y reportes \n[3]Salir \n")
    if menu_principal== "1":
      registro()
    elif menu_principal=="2":
      consultas()
    elif menu_principal=="3":
      print("Gracias por visitarnos, vuelva pronto")
      break
    else:
        print("La opcion ingresada no es correcta, elija de nuevo")
