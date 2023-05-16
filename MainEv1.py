from datetime import date, datetime
import re
import csv
import os
import openpyxl
import sqlite3
import sys
import os.path
from sqlite3 import Error
start=False

def conectar_db():
    conexion = None
    try:
        conexion = sqlite3.connect("biblioteca.db")
        cursor = conexion.cursor()
        return conexion, cursor
    except sqlite3.Error as error:
        print("Error al conectar a la base de datos:", error)
        if conexion:
            conexion.close()
        return None, None

def cerrar_db(conexion):
    if conexion:
        conexion.close()

def obtener_autores(cursor):
    cursor.execute("SELECT nombre FROM autores")
    autores = [autor[0] for autor in cursor.fetchall()]
    return autores

def obtener_generos(cursor):
    cursor.execute("SELECT nombre FROM generos")
    generos = [genero[0] for genero in cursor.fetchall()]
    return generos

def guardar_libro(cursor, titulo, autor, genero, publicacion, dia, mes, anio, isbn):
    try:
        cursor.execute("INSERT INTO libros (titulo, autor, genero, publicacion, dia_adquisicion, mes_adquisicion, anio_adquisicion, isbn) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                       (titulo, autor, genero, publicacion, dia, mes, anio, isbn))
        conexion.commit()
        print("El libro se ha registrado exitosamente en la base de datos.")
    except sqlite3.Error as error:
        print("Error al guardar el libro en la base de datos:", error)

def registro():
    print("-" * 40)
    print("Registro de libro")
    print("-" * 40)

    conexion, cursor = conectar_db()
    if not conexion or not cursor:
        return

    autores = obtener_autores(cursor)
    generos = obtener_generos(cursor)

    while True:
        titulo = input("Ingresa el título del libro a registrar: ")
        if titulo.strip() == '':
            print("El título es un campo obligatorio.")
            continue

        autor = input(f"Ingrese el autor de '{titulo}': ")
        if autor.strip() == '':
            print("El autor del libro es un campo obligatorio.")
            continue
        elif autor not in autores:
            print("El autor no está registrado. Por favor, elija uno de los autores existentes.")
            continue

        genero = input(f"Ingrese el género al que pertenece '{titulo}': ")
        if genero.strip() == '':
            print("El género del libro es un campo obligatorio.")
            continue
        elif genero not in generos:
            print("El género no está registrado. Por favor, elija uno de los géneros existentes.")
            continue

        while True:
            publicacion = input(f"Ingrese el año de publicación del libro '{titulo}' (YYYY): ")
            if not bool(re.match("^[0-9]{4}$", publicacion)):
                print("\nEl año de publicación del libro debe tener 4 caracteres numéricos.")
                continue
            anio_actual = datetime.datetime.now().year
            if int(publicacion) > anio_actual:
                print("El año de publicación no puede ser mayor al año actual.")
                continue
            break

        while True:
            fecha_adquisicion = input("Ingrese la fecha en la que se adquirió el libro (aaaa/mm/dd): ")
            try:
                fecha_adquisicion = datetime.datetime.strptime(fecha_adquisicion, "%Y/%m/%d").date()
                dia = fecha_adquisicion.day
                mes = fecha_adquisicion.month
                anio = fecha_adquisicion.year

                anio_actual = datetime.datetime.now().year
                if anio > anio_actual:
                    print("El año de adquisición no puede ser mayor al año actual.")
                    continue

                if len(str(anio)) != 4:
                    print("El año de adquisición debe tener 4 dígitos.")
                    continue

                break
            except ValueError:
                print("La fecha ingresada no es válida. Por favor, ingrese una fecha en el formato correcto (aaaa/mm/dd).")
                continue

        while True:
              isbn = input(f"Ingrese la clave de ISBN del libro '{titulo}': ")
              if len(isbn) == 13 and bool(re.match("^[0-9]{13}$", isbn)):
                  break
              else:
                  print("El ISBN debe tener 13 caracteres numéricos. Vuelva a ingresarlo.")

def consultas():
    while True:
        try:
            sub_menu=int(input("Consultas y Reportajes\n ¿Que accion deseas realizar? \n[1] Consulta por titulo \n[2] Reportajes \n[3] Volver al menú Principal \n"))
        
            if sub_menu == 3:
                break
            if sub_menu == 1:
                while True:
                    consulta = int(input("Consulta de Título \n ¿Qué acción deseas realizar? \n[1] Por título \n[2] Por ISBN \n[3] Volver al menú de consultas y reportajes \n"))

                    if consulta == 3:
                        break
                    if consulta == 1:
                        try:
                            with sqlite3.connect("Biblioteca.db") as conn:
                                mi_cursor = conn.cursor()

                                mi_cursor.execute("SELECT titulo FROM Libros")
                                registros = mi_cursor.fetchall()

                                if registros:
                                    print("**********Lista de Títulos*********")
                                    for titulo in registros:
                                        print(titulo[0])

                                buscar_titulo = input("¿Qué título quieres buscar? ")
                                valores = {"titulo": buscar_titulo}

                                datos = "SELECT Libros.clave, Libros.titulo, autores.AutNombre, autores.AutApellidos, generos.GenNombre, Libros.añopublicacion, Libros.ISBN, Libros.Fechaadq \
                                        FROM Libros \
                                        JOIN autores ON Libros.autor = autores.clave \
                                        JOIN generos ON Libros.genero = generos.clave \
                                        WHERE Libros.titulo = :titulo"

                                mi_cursor.execute(datos, valores)
                                registros2 = mi_cursor.fetchall()

                                if registros2:
                                    print("**********Resultados de la búsqueda*********")
                                    for fila in registros2:
                                        print("Clave: ", fila[0])
                                        print("Título: ", fila[1])
                                        print("Autor: ", fila[2], fila[3])
                                        print("Género: ", fila[4])
                                        print("Año de publicacion: ", fila[5])
                                        print("ISBN: ", fila[6])
                                        print("Fecha en la que se adquirio: ", fila[7])
                                else:
                                    print("No se encontró el libro")

                        except Error as e:
                            print(e)
                        except Exception:
                            print(f"Se produjo el siguiente error: {sys.exc_info()[0]}")
                        finally:
                            conn.close()
        except Error as e:
            print(e)
        except Exception:
            print(f"Se produjo el siguiente error: {sys.exc_info()[0]}")

            if sub_menu == 2:
                try:
                    with sqlite3.connect("test2.db") as conn:
                        mi_cursor = conn.cursor()

                        mi_cursor.execute("SELECT ISBN FROM Libros")
                        registros = mi_cursor.fetchall()

                        if registros:
                            print("**********Lista de ISBN*********")
                            for isbn in registros:
                                print(isbn[0])

                        buscar_isbn = input("¿Qué título quieres buscar? ")
                        valores2 = {"isbn": buscar_isbn}

                        datos = "SELECT Libros.clave, Libros.titulo, autores.AutNombre, autores.AutApellidos, generos.GenNombre, Libros.añopublicacion, Libros.ISBN, Libros.Fechaadq \
                                    FROM Libros \
                                    JOIN autores ON Libros.autor = autores.clave \
                                    JOIN generos ON Libros.genero = generos.clave \
                                    WHERE Libros.ISBN = :isbn"

                        mi_cursor.execute(datos, valores2)
                        registros2 = mi_cursor.fetchall()

                        if registros2:
                            print("**********Resultados de la búsqueda*********")
                            for fila in registros2:
                                print("Clave: ", fila[0])
                                print("Título: ", fila[1])
                                print("Autor: ", fila[2], fila[3])
                                print("Género: ", fila[4])
                                print("Año de publicacion: ", fila[5])
                                print("ISBN: ", fila[6])
                                print("Fecha en la que se adquirio: ", fila[7])
                        else:
                            print("No se encontró el libro")

                except Error as e:
                    print(e)
                except Exception:
                    print(f"Se produjo el siguiente error: {sys.exc_info()[0]}")


def GuardarArchivo():
    listareport=list(registro_libro.items())
    archivo = open("Registro.csv","w",newline="")
    grabador=csv.writer(archivo)
    grabador.writerow(("Clave","Titulo","Autor","Genero","f_publicacion","fecha_adquisicion","isbn"))
    grabador.writerows([(clave,datos[0],datos[1],datos[2],datos[3],datos[4],datos[5]) for clave,datos in listareport])
    archivo.close

def CrearTablas():
    file_exists = os.path.exists('Biblioteca.db')
    if not(file_exists):
        try:
            with sqlite3.connect("Biblioteca.db") as conn:
                mi_cursor=conn.cursor()
                mi_cursor.execute("CREATE TABLE IF NOT EXISTS generos (clave INTEGER PRIMARY KEY, GenNombre TEXT NOT NULL);")
                mi_cursor.execute("CREATE TABLE IF NOT EXISTS autores (clave INTEGER PRIMARY KEY, AutNombre TEXT NOT NULL, AutApellidos TEXT NOT NULL);")
                mi_cursor.execute("CREATE TABLE IF NOT EXISTS Libros (clave INTEGER PRIMARY KEY, titulo TEXT NOT NULL, autor INTEGER NOT NULL, \
                                  genero INTEGER NOT NULL, añopublicacion timestamp, ISBN TEXT NOT NULL, \
                                  fechaadq TIMESTAMP, FOREIGN KEY(autor) REFERENCES autores(clave), FOREIGN KEY(genero) REFERENCES genero(clave));")
                print("Tablas creada exitosamente")
        except Error as e:
                print(e)
        except:
                print(f"Se produjo el siguiente error: {sys.exc_info()[0]}")
        finally:
                conn.close()
    else:
        print("Archivo db existente.")

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
    for clave,datos in listareport:
        if datos[2]==generosearch:
            grabador1.writerows([(clave,datos[0],datos[1],datos[2],datos[3],datos[4],datos[5])])
    archivo4.close()
    ruta = os.getcwd()
    print("El archivo generado tiene por nombre ",nombrarch," y esta en la ruta ",ruta)


def ExportArchAñoPublic_csv(añosearch):
    listareport = list(registro_libro.items())
    nombrarch = "ReporteAñoPublicacion" + str(datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")) + ".csv"
    archivo4 = open(nombrarch, "w", newline="")
    grabador1 = csv.writer(archivo4)
    grabador1.writerow(("Clave", "Titulo", "Autor", "Genero", "f_publicacion", "fecha_adquisicion", "isbn"))
    
    for clave, datos in listareport:
        año = datos[3].split("/")[-1]  
        if año == añosearch:
            grabador1.writerows([(clave, datos[0], datos[1], datos[2], datos[3], datos[4], datos[5])])
    
    archivo4.close()
    ruta = os.getcwd()
    print("El archivo generado tiene por nombre ", nombrarch, " y esta en la ruta ", ruta)


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


def GuardarLibros(titulo,autor,genero,añopub,isbn,fechadqdia,fechadqmes,fechañodq):
    try:
        with sqlite3.connect("Biblioteca.db") as conn:
            mi_cursor=conn.cursor()
            valores = (titulo,autor,genero,datetime.datetime(añopub,1,1),isbn,datetime.datetime(fechañodq,fechadqmes,fechadqdia))
            mi_cursor.execute("INSERT INTO Libros (titulo,autor,genero,añopublicacion,ISBN,fechaadq) VALUES(?,?,?,?,?,?)", valores)
        print("Registros agregado exitosamente.")
    except Error as e:
        print(e)
    except:
        print(f"Se produjo el siguiente error: {sys.exc_info()[0]}")
    finally:
        conn.close()

def GuardarAutores(nombre,apellidos):
    try:
        with sqlite3.connect("Biblioteca.db") as conn:
            mi_cursor=conn.cursor()
            valores = (nombre,apellidos)
            mi_cursor.execute("INSERT INTO autores (AutNombre,AutApellidos) VALUES(?,?)", valores)
        print("Autor agregado exitosamente.")
    except Error as e:
        print(e)
    except:
        print(f"Se produjo el siguiente error: {sys.exc_info()[0]}")
    finally:
        conn.close()

def GuardarGeneros(genero):
    try:
        with sqlite3.connect("Biblioteca.db") as conn:
            mi_cursor=conn.cursor()
            valores = (genero)
            mi_cursor.execute("INSERT INTO generos (GenNombre) VALUES(?)", valores)
        print("Genero agregado exitosamente.")
    except Error as e:
        print(e)
    except:
        print(f"Se produjo el siguiente error: {sys.exc_info()[0]}")
    finally:
        conn.close()

def registro_autores():
    while True:
        out=False
        autor=""
        apellidos=""
        while True:
            autor=input(f"Favor de ingresar el nombre del autor a registrar ")
            if autor.strip() == '':
                print("Favor de no dejar el espacio vacio.")
            elif (not bool(re.match("^[A-Za-z ñáéíóúüÑÁÉÍÓÚÜ]{1,100}$",autor))):
                print("\nEl nombre del autor solo puede contener 100 caracteres como máximo entre letras y espacios.")
                continue
            else: 
                break
        while True:
            apellidos=input(f"Favor de ingresar los apellidos del autor a registrar ")
            if apellidos.strip() == '':
                print("Favor de no dejar el espacio vacio.")
            elif (not bool(re.match("^[A-Za-z ñáéíóúüÑÁÉÍÓÚÜ]{1,100}$",apellidos))):
                print("\nLos apellidos del autor solo pueden contener 100 caracteres como máximo entre letras y espacios.")
                continue
            else: 
                break

        GuardarAutores(autor,apellidos)
        while True:
            salida=input("Introduzca 1 para registrar otro autor\nIntroduzca 2 para salir de la seccion de registro de autores")
            if salida=="1":
                out=False
                break
            elif salida=="2":
                out=True
                break
            else:
                print("Seleccion introducida no valida.")
        if out==True:
            break

def registro_generos():
    while True:
        out=False
        while True:
            genero=input(f"Favor de ingresar el genero a registrar ")
            if genero.strip() == '':
                print("Favor de no dejar el espacio vacio.")
            elif (not bool(re.match("^[A-Za-z ñáéíóúüÑÁÉÍÓÚÜ]{1,100}$",genero))):
                print("\nEl nombre del genero solo puede contener 100 caracteres como máximo entre letras y espacios.")
                continue
            else: 
                break
            
        GuardarGeneros(genero)
        while True:
            salida=input("Introduzca 1 para registrar otro genero\nIntroduzca 2 para salir de la seccion de registro de generos")
            if salida=="1":
                out=False
                break
            elif salida=="2":
                out=True
                break
            else:
                print("Seleccion introducida no valida.")
        if out==True:
            break

def HayAutores():
    Existen=False
    try:
        with sqlite3.connect("Biblioteca.db") as conn:
            mi_cursor = conn.cursor()
            mi_cursor.execute("SELECT * FROM autores ORDER BY clave")
            registros = mi_cursor.fetchall()

        #Procedemos a evaluar si hay registros en la respuesta
            if registros:
                Existen=True
        #Si no hay registros en la respuesta
            else:
                Existen=False
    except Error as e:
        print (e)
    except Exception:
        print(f"Se produjo el siguiente error: {sys.exc_info()[0]}")
    finally:
        conn.close()
        return Existen

def HayGeneros():
    Existen=False
    try:
        with sqlite3.connect("Biblioteca.db") as conn:
            mi_cursor = conn.cursor()
            mi_cursor.execute("SELECT * FROM generos ORDER BY clave")
            registros = mi_cursor.fetchall()

        #Procedemos a evaluar si hay registros en la respuesta
            if registros:
                Existen=True
        #Si no hay registros en la respuesta
            else:
                Existen=False
    except Error as e:
        print (e)
    except Exception:
        print(f"Se produjo el siguiente error: {sys.exc_info()[0]}")
    finally:
        conn.close()
        return Existen

def HayLibros():
    Existen=False
    try:
        with sqlite3.connect("Biblioteca.db") as conn:
            mi_cursor = conn.cursor()
            mi_cursor.execute("SELECT * FROM Libros ORDER BY clave")
            registros = mi_cursor.fetchall()

        #Procedemos a evaluar si hay registros en la respuesta
            if registros:
                Existen=True
        #Si no hay registros en la respuesta
            else:
                Existen=False
    except Error as e:
        print (e)
    except Exception:
        print(f"Se produjo el siguiente error: {sys.exc_info()[0]}")
    finally:
        conn.close()
        return Existen

def ConsultaLibro_TAG(titulo,autor,genero):
    try:
        with sqlite3.connect("Biblioteca.db") as conn:
            mi_cursor = conn.cursor()
            mi_cursor.execute("SELECT * FROM Libros ORDER BY clave")
            registros = mi_cursor.fetchall()
        #Procedemos a evaluar si hay registros en la respuesta
            if registros:
                if titulo==1:
                    print("titulos")
                    print("*" * 30)
                    for claves, titulos, autores, generos,añopub, isbn,fecha in registros:
                        print(f"{titulos:^16}")
        #Si no hay registros en la respuesta
            else:
                print("No hay libros registrados.")

            mi_cursor.execute("SELECT * FROM autores ORDER BY clave")
            registros = mi_cursor.fetchall()
        #Procedemos a evaluar si hay registros en la respuesta
            if registros:
                if autor==1:
                    print("nombre\tapellidos")
                    print("*" * 30)
                    for claves, nombreaut,apellaut in registros:
                        print(f"{nombreaut:^16}\t{apellaut}")
        #Si no hay registros en la respuesta
            else:
                print("No hay libros registrados.")
            
            mi_cursor.execute("SELECT * FROM generos ORDER BY clave")
            registros = mi_cursor.fetchall()
        #Procedemos a evaluar si hay registros en la respuesta
            if registros:
                if genero==1:
                    print("generos")
                    print("*" * 30)
                    for claves, generonom in registros:
                        print(f"{generonom:^16}")
        #Si no hay registros en la respuesta
            else:
                print("No hay libros registrados.")
    except Error as e:
        print (e)
    except Exception:
        print(f"Se produjo el siguiente error: {sys.exc_info()[0]}")
    finally:
        conn.close()
    

CrearTablas()
while True:
    if start==False:
        registro_libro={}
        start=True
    menu_principal=input("Bienvenido a la biblioteca universitaria\n ¿Que accion deseas realizar? \n[1]Registrar un nuevo ejemplar \n[2]Consultas y reportes \n\
                         [3]Registrar un genero\n[4]Registrar un autor\n[5]Salir")
    if menu_principal== "1":
        if HayAutores()==False and HayGeneros()==False:
            print("No hay autores, ni generos registrados por lo que no se pueden registrar libros.\nVolviendo a menu principal....")
        elif HayGeneros()==False:
            print("No hay generos registrados, por lo que no se pueden registrar libros.\nVolviendo a menu principal....")
        elif HayAutores()==False:
            print("No hay autores registrados, por lo que no se pueden registrar libros.\nVolviendo a menu principal....")
        else:
            registro()
    elif menu_principal=="2":
        if HayLibros()==False:
            print("No hay libros registrados, por lo que no hay libros para consultar o reportar.\nVolviendo a menu principal....")
        else:
            consultas()
    elif menu_principal=="5":
        print("Gracias por visitarnos, vuelva pronto")
        break
    elif menu_principal=="3":
        registro_generos()
    elif menu_principal=="4":
        registro_autores()
    else:
        print("La opcion ingresada no es correcta, elija de nuevo")