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

                    registro_libro[identificador] = [titulo.upper(), autor.upper(), genero.upper(), publicacion, fecha_adquisicion, isbn]
                    while True:
                            DatosCorrect=True
                            print("*" * 40)
                            print(f"Titulo: {titulo} \nAutor: {autor} \nGenero: {genero} \nFecha de publicacion: {publicacion} \nFecha de adquisición: {fecha_adquisicion} \nISBN: {isbn} \n") 
                            print("*" * 40)
                            confirmacion=input("¿Son correctos los datos ingresados? (SI/NO)").upper()
                            print("*" * 40)
                            if confirmacion=="SI":
                                print("*" * 40)
                                print(f"Se registro el libro\n", registro_libro[identificador])
                                print("*" * 40)
                                break
                            else: 
                                DatosCorrect=False
                                print("Vuelva a ingresar los datos")
                                if identificador in registro_libro:
                                    titulo, autor, genero, publicacion, fecha_adquisicion, isbn= registro_libro[identificador]
                                    del registro_libro[identificador]
                                break
                    if DatosCorrect==False:
                        continue   

                    break
            nuevo_registro=input("¿Deseas realizar un nuevo registro? (SI/NO)").upper()
            if nuevo_registro=="SI":
                continue 
            if nuevo_registro=="NO":
                print("*" * 40)
                print("Sus registros han quedado guardados")
                break

def consultas():
        while True:
            sub_menu=input("Consultas y Reportajes\n ¿Que accion deseas realizar? \n[1] Consulta por titulo \n[2] Reportajes \n[3] Volver al menú Principal \n")
            sub_menu = int(sub_menu)
            if sub_menu == 3:
                break
            if sub_menu == 1:
                while True:
                    consulta_titulo=input("Consulta de Titulo \n ¿Que accion deseas realizar? \n[1] Por titulo \n[2] Por ISBN \n[3] Volver al menú de consultas y reportajes \n")
                    consulta_titulo = int(consulta_titulo)
                    if consulta_titulo == 3:
                        break
                    elif consulta_titulo == 1:
                        found=False
                        titulo= input("Ingresa el titulo del libro a buscar: ")
                        regisitems=(list(registro_libro.items()))
                        tituloMayus= titulo.upper()
                        for key,value in regisitems:
                            if value[0]==tituloMayus:
                                found=True
                                print("Folio: ",key,"\nTitulo: ",registro_libro[key][0],"\nAutor: ",registro_libro[key][1],"\nGenero: ",registro_libro[key][2],"\nAño de Publicación: ",registro_libro[key][3],"\nFecha_Adquisicion: ",registro_libro[key][4],"\nISBN: ",registro_libro[key][5])
                        if found==False:
                            print("No se encontraron libros con el titulo ", tituloMayus)
                            
                    elif consulta_titulo == 2:
                        found=False
                        isbn= input("Ingresa el isbn del libro a buscar: ")
                        regisitems=(list(registro_libro.items()))
                        for key,value in regisitems:
                            if value[5]==isbn:
                                found=True
                                print("Folio: ",key,"\nTitulo: ",registro_libro[key][0],"\nAutor: ",registro_libro[key][1],"\nGenero: ",registro_libro[key][2],"\nAño de Publicación: ",registro_libro[key][3],"\nFecha_Adquisicion: ",registro_libro[key][4],"\nISBN: ",registro_libro[key][5])
                        if found==False:
                            print("No se encontraron titulos con el ISBN ",isbn)
                    else:
                        print("La opcion ingresada no es correcta, elija de nuevo") 
            if sub_menu == 2:
                while True:
                    reportajes = input("Reportajes \n ¿Que accion deseas realizar? \n[1] Catalogo Completo \n[2] Reportaje por autor \n[3] Reportaje por genero \n[4] Por año de publicacion \n [5] volver al menu de reportaje \n")
                    if reportajes=="1":
                        listareport=list(registro_libro.items())
                        if listareport:
                            print(f"Folio \t Titulo \t\t Autor \t\t\t Genero \t Año_Public \t Fecha_Adq \t ISBN")
                            print("*"*100)
                            for Clave,valor in listareport:
                                print(f'{Clave:4} \t  {valor[0]:15} \t {valor[1]:15} \t {valor[2]:10} \t {valor[3]:5} \t\t {valor[4]:5} \t {valor[5]:15} ')
                            print("*"*100)
                        else:
                            print("No se han registrado libros")

                    elif reportajes=="2":
                        foundautor=False
                        autorsel = input("Favor de introducir el autor: ")
                        mayusautorsel=autorsel.upper()
                        listareport=list(registro_libro.items())
                        print(f"Folio \t Titulo \t\t Autor \t\t\t Genero \t Año_Public \t Fecha_Adq \t ISBN")
                        print("*"*100)
                        for key,value in regisitems:
                            if value[1]==mayusautorsel:
                                foundautor=True
                                print(f'{key:4} \t  {value[0]:15} \t {value[1]:15} \t {value[2]:10} \t {value[3]:5} \t\t {value[4]:5} \t {value[5]:15}')
                        if foundautor==False:
                            print("No hay libros registrados de este autor")
                        print("*"*100)
                    elif reportajes=="3":
                        foundgen=False
                        generosel = input("Favor de introducir el genero:   ")
                        mayusgenerosel=generosel.upper()
                        listareport=list(registro_libro.items())
                        print(f"Folio \t Titulo \t\t Autor \t\t\t Genero \t Año_Public \t Fecha_Adq \t ISBN")
                        print("*"*100)
                        for key,value in regisitems:
                            if value[2]==mayusgenerosel:
                                foundgen=True
                                print(f'{key:4} \t  {value[0]:15} \t {value[1]:15} \t {value[2]:10} \t {value[3]:5} \t\t {value[4]:5} \t {value[5]:15}')
                        if foundgen==False:
                            print("No hay libros registrados de este genero")
                        print("*"*100)

                    elif reportajes=="4":
                        foundyear=False
                        añosel = input("Favor de introducir el año: ")
                        mayusañosel=añosel.upper()
                        listareport=list(registro_libro.items())
                        print(f"Folio \t Titulo \t\t Autor \t\t\t Genero \t Año_Public \t Fecha_Adq \t ISBN")
                        print("*"*100)
                        for key,value in regisitems:
                            if value[3]==mayusañosel:
                                foundyear=True
                                print(f'{key:4} \t  {value[0]:15} \t {value[1]:15} \t {value[2]:10} \t {value[3]:5} \t\t {value[4]:5} \t {value[5]:15}')
                        if foundyear==False:
                            print("No hay libros registrados de este año de publicación")

                        print("*"*100)

                    elif reportajes=="5":
                        break

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
