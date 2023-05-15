import datetime
import re
import csv
import os
import openpyxl
import sqlite3
import sys
import os.path
from sqlite3 import Error
start=False
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
                            print("El a1utor del libro es un campo obligatorio")
                        elif (not bool(re.match("^[A-Za-z ñáéíóúüÑÁÉÍÓÚÜ]{1,100}$",autor))):
                            print("\nEl nombre del autor solo puede contener 100 caracteres como máximo entre letras y espacios.")
                            continue
                        else: 
                            break

                    while True:
                        genero=input(f"Ingrese el genero al que pertenece ")
                        if genero.strip() == '':
                            print("El Genero del libro es un campo obligatorio")
                        elif (not bool(re.match("^[A-Za-z ñáéíóúüÑÁÉÍÓÚÜ]{1,100}$",genero))):
                            print("\nEl genero solo puede contener 100 caracteres como máximo con solo letras y espacios.")
                            continue
                        else: 
                            break

                    while True:
                        publicacion=input(f"Ingrese el año de publicación del libro (YYYY) {titulo}  ")
                        if (not bool(re.match("^[0-9]{4}$", publicacion))):
                            print("\nEl año de publicación del libro solo pueden ser 4 caracteres númericos.")
                            continue
                        fecha_procesada = datetime.datetime.strptime(publicacion, "%Y").date() 
                        fecha_actual = datetime.date.today()
                        print(fecha_procesada)
                        if fecha_procesada > fecha_actual:
                            print("Esta fecha no es valida")
                        else:
                            break

                    while True:
                        fecha_adquisicion=input("Ingrese la fecha en la que se adquirio el libro (aaaa/mm/dd) ")
                        if (not bool(re.match("^([0-9]{4}[/]?((0[13-9]|1[012])[/]?(0[1-9]|[12][0-9]|30)|(0[13578]|1[02])[/]?31|02[/]?(0[1-9]|1[0-9]|2[0-8]))|([0-9]{2}(([2468][048]|[02468][48])|[13579][26])|([13579][26]|[02468][048])00)[/]?02[/]?29)$",fecha_adquisicion))):
                            print("\nLa fecha sigue los formatos aaaa/mm/dd y solo acepta dias posibles.")
                            continue
                        fecha2_procesada= datetime.datetime.strptime(fecha_adquisicion, "%Y/%m/%d").date() 
                        if fecha2_procesada < fecha_procesada :
                            print("La fecha de adquisicion debe ser despues de la fecha de publicacion, ingrese una fecha valida ")
                        else:
                            break

                    while True:
                        isbn=input(str(f"Ingresa la clave de ISBN del libro "))
                        if len(isbn) == 13 and (bool(re.match("^[0-9]{13}$", isbn))):
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
                            elif confirmacion=="NO": 
                                DatosCorrect=False
                                print("Vuelva a ingresar los datos")
                                if identificador in registro_libro:
                                    titulo, autor, genero, publicacion, fecha_adquisicion, isbn= registro_libro[identificador]
                                    del registro_libro[identificador]
                                break
                            else:
                                print("Introduce una de las opciones (Si/NO)")
                    if DatosCorrect==False:
                        continue   

                    break
            seleccion=False
            while True:
                nuevo_registro=input("¿Deseas realizar un nuevo registro? (SI/NO)").upper()
                if nuevo_registro=="SI":
                    seleccion=True
                    break 
                elif nuevo_registro=="NO":
                    print("*" * 40)
                    print("Sus registros han quedado guardados")
                    break
                else:
                    print("Favor de seleccionar una opcion valida.")
                    continue
            if seleccion==True:
                continue
            else:
                break

def consultas():
        while True:
            sub_menu=input("Consultas y Reportajes\n ¿Que accion deseas realizar? \n[1] Consulta por titulo \n[2] Reportajes \n[3] Volver al menú Principal \n")
            sub_menu = sub_menu
            listareport=list(registro_libro.items())
            if sub_menu == "3":
                break
            if sub_menu == "1":
                while True:
                    consulta_titulo=input("Consulta de Titulo \n ¿Que accion deseas realizar? \n[1] Por titulo \n[2] Por ISBN \n[3] Volver al menú de consultas y reportajes \n")
                    consulta_titulo = consulta_titulo
                    if consulta_titulo == "3":
                        break
                    elif consulta_titulo == "1":
                        found=False
                        if listareport:
                            print("Lista de Titulos registrados:")
                            for key,value in listareport:
                                print(value[0])
                        titulo= input("Ingresa el titulo del libro a buscar: ")
                        regisitems=(list(registro_libro.items()))
                        tituloMayus= titulo.upper()
                        for key,value in regisitems:
                            if value[0]==tituloMayus:
                                found=True
                                print("Folio: ",key,"\nTitulo: ",registro_libro[key][0],"\nAutor: ",registro_libro[key][1],"\nGenero: ",registro_libro[key][2],"\nAño de Publicación: ",registro_libro[key][3],"\nFecha_Adquisicion: ",registro_libro[key][4],"\nISBN: ",registro_libro[key][5])
                        if found==False:
                            print("No se encontraron libros con el titulo ", tituloMayus)
                            
                    elif consulta_titulo == "2":
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
            if sub_menu == "2":
                while True:
                    reportajes = input("Reportajes \n ¿Que accion deseas realizar? \n[1] Catalogo Completo \n[2] Reportaje por autor \n[3] Reportaje por genero \n[4] Por año de publicacion \n[5] volver al menu de reportaje \n")
                    listareport=list(registro_libro.items())
                    if reportajes=="1":
                        listareport=list(registro_libro.items())
                        if listareport:
                            print(f"Folio \t Titulo \t\t Autor \t\t\t Genero \t Año_Public \t Fecha_Adq \t ISBN")
                            print("*"*100)
                            for Clave,valor in listareport:
                                print(f'{Clave:4} \t  {valor[0]:15} \t {valor[1]:15} \t {valor[2]:10} \t {valor[3]:5} \t\t {valor[4]:5} \t {valor[5]:15} ')
                            print("*"*100)
                            descarga = input("¿Exportar este reporte? \n[1] Exportar el reportaje en CSV \n[2] Exportar el reportaje en Excel \n[3] No exportar el reporte \n")
                            if descarga=="1":
                                ExportArchComplt_csv()
                            elif descarga=="2":
                                ExportArchComplt_Excel()
                            else:
                                print("Reporte no exportado. \n Volviendo a menu....")
                        else:
                            print("No se han registrado libros.")
                    elif reportajes=="2":
                        foundautor=False
                        if listareport:
                            print("Lista de autores registrados:")
                            for key,value in listareport:
                                print(value[1])
                        autorsel = input("Favor de introducir el autor: ")
                        mayusautorsel=autorsel.upper()
                        listareport=list(registro_libro.items())
                        if listareport:
                            print(f"Folio \t Titulo \t\t Autor \t\t\t Genero \t Año_Public \t Fecha_Adq \t ISBN")
                            print("*"*100)
                            for key,value in listareport:
                                if value[1]==mayusautorsel:
                                    foundautor=True
                                    print(f'{key:4} \t  {value[0]:15} \t {value[1]:15} \t {value[2]:10} \t {value[3]:5} \t\t {value[4]:5} \t {value[5]:15}')
                            print("*"*100)
                            if foundautor==False:
                                print("No hay libros registrados de este autor")
                                print("*"*100)
                            else:
                                descarga = input("¿Exportar este reporte? \n[1] Exportar el reportaje en CSV \n[2] Exportar el reportaje en Excel \n[3] No exportar el reporte \n")
                                if descarga=="1":
                                    ExportArchAutores_csv(mayusautorsel)
                                elif descarga=="2":
                                    ExportArchAutores_Excel(mayusautorsel)
                                else:
                                    print("Reporte no exportado. \n Volviendo a menu....")
                        else:
                            print("No se han registrado libros por lo que no hay libros de este autor.")
                    elif reportajes=="3":
                        foundgen=False
                        if listareport:
                            print("Lista de generos registrados:")
                            for key,value in listareport:
                                print(value[2])
                        generosel = input("Favor de introducir el genero:   ")
                        mayusgenerosel=generosel.upper()
                        listareport=list(registro_libro.items())
                        if listareport:
                            print(f"Folio \t Titulo \t\t Autor \t\t\t Genero \t Año_Public \t Fecha_Adq \t ISBN")
                            print("*"*100)
                            for key,value in listareport:
                                if value[2]==mayusgenerosel:
                                    foundgen=True
                                    print(f'{key:4} \t  {value[0]:15} \t {value[1]:15} \t {value[2]:10} \t {value[3]:5} \t\t {value[4]:5} \t {value[5]:15}')
                            print("*"*100)
                            if foundgen==False:
                                print("No hay libros registrados de este genero")
                                print("*"*100)
                            else:
                                descarga = input("¿Exportar este reporte? \n[1] Exportar el reportaje en CSV \n[2] Exportar el reportaje en Excel \n[3] No exportar el reporte \n")
                                if descarga=="1":
                                    ExportArchGenero_csv(mayusgenerosel)
                                elif descarga=="2":
                                    ExportArchGenero_Excel(mayusgenerosel)
                                else:
                                    print("Reporte no exportado. \n Volviendo a menu....")
                        else:
                            print("No se han registrado libros por lo que no hay libros de este genero.")

                    elif reportajes=="4":
                        foundyear=False
                        añosel = input("Favor de introducir el año: ")
                        mayusañosel=añosel.upper()
                        listareport=list(registro_libro.items())
                        if listareport:
                            print(f"Folio \t Titulo \t\t Autor \t\t\t Genero \t Año_Public \t Fecha_Adq \t ISBN")
                            print("*"*100)
                            for key,value in listareport:
                                if value[3]==mayusañosel:
                                    foundyear=True
                                    print(f'{key:4} \t  {value[0]:15} \t {value[1]:15} \t {value[2]:10} \t {value[3]:5} \t\t {value[4]:5} \t {value[5]:15}')
                            print("*"*100)
                            if foundyear==False:
                                print("No hay libros registrados de este año de publicación")
                                print("*"*100)
                            else:
                                descarga = input("¿Exportar este reporte? \n[1] Exportar el reportaje en CSV \n[2] Exportar el reportaje en Excel \n[3] No exportar el reporte \n")
                                if descarga=="1":
                                    ExportArchAñoPublic_csv(mayusañosel)
                                elif descarga=="2":
                                    ExportArchAñoPublic_Excel(mayusañosel)
                                else:
                                    print("Reporte no exportado. \n Volviendo a menu....")
                        else:
                            print("No se han registrado libros por lo que no hay libros con este año de publicación.")

                    elif reportajes=="5":
                        break
                    else:
                        print("Favor de ingresar una respuesta aceptable.")

            else:
                print("La opcion ingresada no es correcta, elija de nuevo")

def GuardarArchivo():
    listareport=list(registro_libro.items())
    archivo = open("Registro.csv","w",newline="")
    grabador=csv.writer(archivo)
    grabador.writerow(("Clave","Titulo","Autor","Genero","f_publicacion","fecha_adquisicion","isbn"))
    grabador.writerows([(clave,datos[0],datos[1],datos[2],datos[3],datos[4],datos[5]) for clave,datos in listareport])
    archivo.close

def CargarDatos():
    file_exists = os.path.exists('Biblioteca.db')
    if not(file_exists):
        try:
            with sqlite3.connect("Biblioteca.db") as conn:
                mi_cursor=conn.cursor()
                mi_cursor.execute("CREATE TABLE IF NOT EXISTS generos (clave INTEGER PRIMARY KEY, GenNombre TEXT NOT NULL, status INTEGER NOT NULL);")
                mi_cursor.execute("CREATE TABLE IF NOT EXISTS autores (clave INTEGER PRIMARY KEY, AutNombre TEXT NOT NULL, status INTEGER NOT NULL);")
                mi_cursor.execute("CREATE TABLE IF NOT EXISTS Libros (clave INTEGER PRIMARY KEY, titulo TEXT NOT NULL, autor INTEGER NOT NULL, \
                                  genero INTEGER NOT NULL, añopublicacion INTEGER NOT NULL, ISBN TEXT NOT NULL, \
                                  fechaadq TIMESTAMP, FOREIGN KEY(clave) REFERENCES eventos(status));")
                print("Tablas creada exitosamente")
        except Error as e:
                print(e)
        except:
                print(f"Se produjo el siguiente error: {sys.exc_info()[0]}")
        finally:
                conn.close()
#    try:
        #registro_libro=dict()
        #with open("Registro.csv","r",newline="") as archivo:
            #lector=csv.reader(archivo)
            #next(lector)

            #for clave, titulo,autor,genero,f_publicacion,fecha_adq,isbn in lector:
                #registro_libro[int(clave)]=(titulo,autor,genero,f_publicacion,fecha_adq,isbn)
        #return registro_libro
#    except FileNotFoundError:
        #print("No hay registros previos en la bilbioteca")
        #registro_libro=dict()
        #return registro_libro
#    except csv.Error as fallocsv:
        #print("Ocurrió un error inesperado y no se cargaron los registros")
        #registro_libro=dict()
        #return registro_libro
#    except Exception:
        #print("Deido a un error no se han podido cargar los registros.")
        #registro_libro=dict()
        #return registro_libro

def ExportArchComplt_csv():
    listareport=list(registro_libro.items())
    nombrarch = "ReporteCompleto" + str(datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")) + ".csv"
    archivo4 = open(nombrarch,"w",newline="")
    grabador1=csv.writer(archivo4)
    grabador1.writerow(("Clave","Titulo","Autor","Genero","f_publicacion","fecha_adquisicion","isbn"))
    grabador1.writerows([(clave,datos[0],datos[1],datos[2],datos[3],datos[4],datos[5]) for clave,datos in listareport])
    archivo4.close
    ruta = os.getcwd()
    print("El archivo generado tiene por nombre ",nombrarch," y esta en la ruta ",ruta)

def ExportArchAutores_csv(autorsearch):
    listareport=list(registro_libro.items())
    nombrarch = "ReporteAutores" + str(datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")) + ".csv"
    archivo4 = open(nombrarch,"w",newline="")
    grabador1=csv.writer(archivo4)
    grabador1.writerow(("Clave","Titulo","Autor","Genero","f_publicacion","fecha_adquisicion","isbn"))
    for clave,datos in listareport:
        if datos[1]==autorsearch:
            grabador1.writerows([(clave,datos[0],datos[1],datos[2],datos[3],datos[4],datos[5])])
    archivo4.close
    ruta = os.getcwd()
    print("El archivo generado tiene por nombre ",nombrarch," y esta en la ruta ",ruta)

def ExportArchGenero_csv(generosearch):
    listareport=list(registro_libro.items())
    nombrarch = "ReporteGenero" + str(datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")) + ".csv"
    archivo4 = open(nombrarch,"w",newline="")
    grabador1=csv.writer(archivo4)
    grabador1.writerow(("Clave","Titulo","Autor","Genero","f_publicacion","fecha_adquisicion","isbn"))
    #Aqui va el codigo que filtra lo que se escribe en el archivo y que escribe en el archivo

    archivo4.close
    ruta = os.getcwd()
    print("El archivo generado tiene por nombre ",nombrarch," y esta en la ruta ",ruta)

def ExportArchAñoPublic_csv(añosearch):
    listareport=list(registro_libro.items())
    nombrarch = "ReporteAñoPublicacion" + str(datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")) + ".csv"
    archivo4 = open(nombrarch,"w",newline="")
    grabador1=csv.writer(archivo4)
    grabador1.writerow(("Clave","Titulo","Autor","Genero","f_publicacion","fecha_adquisicion","isbn"))
    #Aqui va el codigo que filtra lo que se escribe en el archivo y que escribe en el archivo

    archivo4.close
    ruta = os.getcwd()
    print("El archivo generado tiene por nombre ",nombrarch," y esta en la ruta ",ruta)

def ExportArchComplt_Excel():
    listareport=list(registro_libro.items())
    ruta = os.getcwd()
    archname = "ReporteCatalogoCompleto" + str(datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")) + ".xlsx"
    libro = openpyxl.Workbook()
    libro.iso_dates = True 
    hoja = libro["Sheet"] 
    hoja.title = "Reporte de Catalogo completo"
    hoja["B1"].value ="Folio"
    hoja["C1"].value ="Titulo"
    hoja["D1"].value ="Autor"
    hoja["E1"].value ="Genero"
    hoja["F1"].value ="Año de Publicación"
    hoja["G1"].value ="Fecha de Adquisición"
    hoja["H1"].value ="ISBN"
    for i, (clave, valor) in enumerate(listareport):
        hoja.cell(row=i+2, column=2).value = clave
        hoja.cell(row=i+2, column=3).value = valor[0]
        hoja.cell(row=i+2, column=4).value = valor[1]
        hoja.cell(row=i+2, column=5).value = valor[2]
        hoja.cell(row=i+2, column=6).value = valor[3]
        hoja.cell(row=i+2, column=7).value = valor[4]
        hoja.cell(row=i+2, column=8).value = valor[5]
    libro.save(archname)
    print("El reporte ", archname ," fue creado exitosamente y esta en ",ruta)

def ExportArchAutores_Excel(autorsearch):
    listareport=list(registro_libro.items())
    ruta = os.getcwd()
    archname = "ReporteAutores" + str(datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")) + ".xlsx"
    libro = openpyxl.Workbook()
    libro.iso_dates = True 
    hoja = libro["Sheet"] 
    hoja.title = "Reporte de Autores"
    hoja["B1"].value ="Folio"
    hoja["C1"].value ="Titulo"
    hoja["D1"].value ="Autor"
    hoja["E1"].value ="Genero"
    hoja["F1"].value ="Año de Publicación"
    hoja["G1"].value ="Fecha de Adquisición"
    hoja["H1"].value ="ISBN"
    for i, (clave, valor) in enumerate(listareport):
        if valor[1]==autorsearch:
            hoja.cell(row=i+2, column=2).value = clave
            hoja.cell(row=i+2, column=3).value = valor[0]
            hoja.cell(row=i+2, column=4).value = valor[1]
            hoja.cell(row=i+2, column=5).value = valor[2]
            hoja.cell(row=i+2, column=6).value = valor[3]
            hoja.cell(row=i+2, column=7).value = valor[4]
            hoja.cell(row=i+2, column=8).value = valor[5]
    libro.save(archname)
    print("El reporte ", archname ," fue creado exitosamente y esta en ",ruta)

def ExportArchGenero_Excel(generosearch):
    listareport=list(registro_libro.items())
    ruta = os.getcwd()
    archname = "ReporteGenero" + str(datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")) + ".xlsx"
    libro = openpyxl.Workbook()
    libro.iso_dates = True 
    hoja = libro["Sheet"] 
    hoja.title = "Reporte de Genero"
    hoja["B1"].value ="Folio"
    hoja["C1"].value ="Titulo"
    hoja["D1"].value ="Autor"
    hoja["E1"].value ="Genero"
    hoja["F1"].value ="Año de Publicación"
    hoja["G1"].value ="Fecha de Adquisición"
    hoja["H1"].value ="ISBN"
    for i, (clave, valor) in enumerate(listareport):
        if valor[2]==generosearch:
            hoja.cell(row=i+2, column=2).value = clave
            hoja.cell(row=i+2, column=3).value = valor[0]
            hoja.cell(row=i+2, column=4).value = valor[1]
            hoja.cell(row=i+2, column=5).value = valor[2]
            hoja.cell(row=i+2, column=6).value = valor[3]
            hoja.cell(row=i+2, column=7).value = valor[4]
            hoja.cell(row=i+2, column=8).value = valor[5]
    libro.save(archname)
    print("El reporte ", archname ," fue creado exitosamente y esta en ",ruta)

def ExportArchAñoPublic_Excel(añosearch):
    listareport=list(registro_libro.items())
    ruta = os.getcwd()
    archname = "ReporteAñoPublicacion" + str(datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")) + ".xlsx"
    libro = openpyxl.Workbook()
    libro.iso_dates = True 
    hoja = libro["Sheet"] 
    hoja.title = "Reporte de Año de Publicacion"
    hoja["B1"].value ="Folio"
    hoja["C1"].value ="Titulo"
    hoja["D1"].value ="Autor"
    hoja["E1"].value ="Genero"
    hoja["F1"].value ="Año de Publicación"
    hoja["G1"].value ="Fecha de Adquisición"
    hoja["H1"].value ="ISBN"
    for i, (clave, valor) in enumerate(listareport):
        if valor[3]==añosearch:
            hoja.cell(row=i+2, column=2).value = clave
            hoja.cell(row=i+2, column=3).value = valor[0]
            hoja.cell(row=i+2, column=4).value = valor[1]
            hoja.cell(row=i+2, column=5).value = valor[2]
            hoja.cell(row=i+2, column=6).value = valor[3]
            hoja.cell(row=i+2, column=7).value = valor[4]
            hoja.cell(row=i+2, column=8).value = valor[5]
    libro.save(archname)
    print("El reporte ", archname ," fue creado exitosamente y esta en ",ruta)


def CrearTablas():
    print("A")


while True:
    if start==False:
        registro_libro=CargarDatos()
        start=True
    menu_principal=input("Bienvenido a la biblioteca universitaria\n ¿Que accion deseas realizar? \n[1]Registrar un nuevo ejemplar \n[2]Consultas y reportes \n[3]Salir \n")
    if menu_principal== "1":
      registro()
    elif menu_principal=="2":
      consultas()
    elif menu_principal=="3":
      print("Gracias por visitarnos, vuelva pronto")
      if registro_libro:
        GuardarArchivo()
      break
    else:
        print("La opcion ingresada no es correcta, elija de nuevo")