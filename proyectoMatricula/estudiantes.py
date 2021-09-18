from componentes import Menu,Valida
from helpers import borrarPantalla,gotoxy
from crudArhivos import Archivo
from entidadesUnemi import *
from datetime import date
import time

# Procesos de las Opciones del Menu Mantenimiento


#Esta funcion agrega las carrera dado su descricion y se genera automaticamente su id secuencialmente
# es decir que si no hay nada en el archivo se pone id = 1  y asi sucesivamente.
def carreras():
   borrarPantalla()     
   gotoxy(20,2);print("MANTENIMIENTO DE CARRERAS")
   gotoxy(15,5);print("Descripcion Carrera: ")
   gotoxy(37,5)

   
   descarrera = input()
   archiCarrera = Archivo("./datos/carrera.txt",";")
   carreras = archiCarrera.leer()
   if carreras : idSig = int(carreras[-1][0])+1
   else: idSig=1
   carrera = Carrera(idSig,descarrera)
   datos = carrera.getCarrera()
   datos = ';'.join(datos)
   archiCarrera.escribir([datos],"a")
   gotoxy(15,6); print("Codigo de la Carrera :"+str(idSig))
   time.sleep(2)

#Materias es muy parecido a carreras ya que agrega una descripcion y un id secuencialmente y muestra su id
# brevemente por algunos segundos es posible mejorarlo con os.system("pause")
def materias():

   borrarPantalla()     
   gotoxy(20,2);print("MANTENIMIENTO DE MATERIAS")
   
   gotoxy(15,5);print("Descripcion Materia: ")
   gotoxy(37,5)

   descarrera = input()
   archiCarrera = Archivo("./datos/materia.txt",";")
   carreras = archiCarrera.leer()
   if carreras : idSig = int(carreras[-1][0])+1
   else: idSig=1
   carrera = Materia(idSig,descarrera)
   datos = carrera.getMateria()
   datos = ';'.join(datos)
   archiCarrera.escribir([datos],"a")
   gotoxy(15,6); print("Codigo de la materia :"+str(idSig))
   time.sleep(2)


#Periodo pide 3  cosas un codigo mediante un # esto seria util al consultar 
#se pide tambien una descripcion y al final por breves segundo se muestra el id secuencial del periodo
#Se puede mejorar con un system("pause") y la libreria import os
def periodos():

   borrarPantalla()     
   gotoxy(20,2);print("MANTENIMIENTO DE PERIODOS")
   gotoxy(15,4);print("Codigo: ")
   gotoxy(15,5);print("Descripcion del Periodo : ")
   gotoxy(42,4)
   per = input(" ")
   gotoxy(42,5)

   desPeriodo = input()
   archiPeriodo = Archivo("./datos/periodo.txt",";")
   periodo = archiPeriodo.leer()
   if periodo : idSig = int(periodo[-1][0])+1
   else: idSig=1

   periodo = Periodo(idSig,per,desPeriodo)
   datos = periodo.getPeriodo()
   datos = ';'.join(datos)
   archiPeriodo.escribir([datos],"a")    
   gotoxy(15,6); print("Codigo del Periodo :"+str(idSig))
   time.sleep(2)

#La funcion profesores recibe varios datos de su entidad (Nombre , cedula ..) y
#confirma el id de carrera segun el archivo carrera.txt
def profesores():
   borrarPantalla()
   validar = Valida()     
   gotoxy(20,2);print("INGRESO DE PROFESORES")
   gotoxy(15,4);print("Nombre  : ")
   gotoxy(15,5);print("Cedula: : ")
   gotoxy(15,6);print("Titulo: : ")
   gotoxy(15,7);print("Telefono: ")
   gotoxy(15,8);print("Carrera ID[    ]: ")
   gotoxy(25,4);nom = input()
   gotoxy(25,5);ced = input()
   gotoxy(25,6);tit = input()
   tel=validar.solo_numeros("Error: Solo numeros",25,7)
   lisCarrera,entCarrera = [],None
   while not lisCarrera:
      gotoxy(27,8);id = input().upper()
      archiCarrera = Archivo("./datos/carrera.txt")
      lisCarrera = archiCarrera.buscar(id)
      if lisCarrera:
          entCarrera = Carrera(lisCarrera[0],lisCarrera[1]) 
          gotoxy(33,8);print(entCarrera.descripcion)
      else: 
         gotoxy(33,8);print("No existe Carrera con ese codigo[{}]:".format(id))
         time.sleep(1);gotoxy(33,8);print(" "*40)
   gotoxy(15,10);print("Esta seguro de Grabar El registro(s/n):")
   gotoxy(54,10);grabar = input().lower()
   if grabar == "s":
        archiProfesor = Archivo("./datos/profesor.txt")
        lisProfesores = archiProfesor.leer()
        if lisProfesores : idSig = int(lisProfesores[-1][0])+1
        else: idSig=1
        entProfesor = Profesor(idSig,nom,ced,entCarrera,tit,tel)
        datos = entProfesor.getProfesor()
        datos = ';'.join(datos)
        archiProfesor.escribir([datos],"a")                 
        gotoxy(15,11);input("Registro Grabado Satisfactoriamente\n Presione una tecla para continuar...")
   else:
       gotoxy(15,11);input("Registro No fue Grabado\n presione una tecla para continuar...")     

#Estudiantes es muy parecido a profesores pero este en vez aqui no hay confirmar nada con otro archivo
#ya que solo se agrega un estudiante a los posibles  a matricular a una carrera
def estudiantes():
   borrarPantalla()
   validar = Valida()     
   gotoxy(20,2);print("INGRESO DE ESTUDIANTES")
   gotoxy(15,4);print("Nombre  : ")
   gotoxy(15,5);print("Cedula: : ")
   gotoxy(15,6);print("Dirección: ")
   gotoxy(15,7);print("Telefono: ")
  
   gotoxy(25,4);nom = input()
   gotoxy(25,5);ced = input()
   gotoxy(25,6);direccion = input()
   tel=validar.solo_numeros("Error: Solo numeros",25,7)


   gotoxy(15,10);print("Esta seguro de Grabar El registro(s/n):")
   gotoxy(54,10);grabar = input().lower()

   if grabar == "s":
        archiProfesor = Archivo("./datos/estudiantes.txt")
        lisProfesores = archiProfesor.leer()
        if lisProfesores : idSig = int(lisProfesores[-1][0])+1
        else: idSig=1
        entProfesor = Estudiante(idSig,nom,ced,direccion,tel)
        datos = entProfesor.getEstudiante()
        datos = ';'.join(datos)
        archiProfesor.escribir([datos],"a")                 
        gotoxy(15,11);input("Registro Grabado Satisfactoriamente\n Presione una tecla para continuar...")
   else:
       gotoxy(15,11);input("Registro No fue Grabado\n presione una tecla para continuar...")      

#Matriculacion

#Aqui la primera funcion divertida ya que debe confirmar los id de tres archivos diferentes o si no , no dejara
#pasar , tiene verificacion de que exita en el archivo y tambien el valor debe ser confimado como decimales porque
#en el mundo real nunca es numero exacto :)
def matriculaciones():
   borrarPantalla()
   validar = Valida()     
   gotoxy(20,2);print("MATRICULACIÓN")
   gotoxy(15,4);print("Periodo ID[    ]: ")
   gotoxy(15,5);print("Estudiante ID[    ]: ")
   gotoxy(15,6);print("Carrera ID[    ]: ")
   gotoxy(15,7);print("Valor: ")

   lisPeriodo,entPeriodo = [],None
   while not lisPeriodo:
      gotoxy(27,4);id = input().upper()
      archiPeriodo = Archivo("./datos/periodo.txt")
      lisPeriodo = archiPeriodo.buscar(id)
      if lisPeriodo:
          entPeriodo = Periodo(lisPeriodo[0],lisPeriodo[1],lisPeriodo[2]) 
          gotoxy(35,4);print(entPeriodo.descripcion)
      else: 
         gotoxy(35,4);print("No existe Periodo con ese codigo[{}]:".format(id))
         time.sleep(1);gotoxy(33,4);print(" "*40)


   lisEstudiante,entEstudiante = [],None
   while not lisEstudiante:
      gotoxy(30,5);id = input().upper()
      archiEstudiante = Archivo("./datos/estudiantes.txt")
      lisEstudiante = archiEstudiante.buscar(id)
      if lisEstudiante:
          
          entEstudiante = Estudiante(lisEstudiante[0],lisEstudiante[1],lisEstudiante[2],lisEstudiante[3],lisEstudiante[4]) 
          gotoxy(35,5);print(entEstudiante.nombre)
      else: 
         gotoxy(35,5);print("No existe Estudiante con ese codigo[{}]:".format(id))
         time.sleep(1);gotoxy(36,5);print(" "*40)


   lisCarrera,entCarrera = [],None
   while not lisCarrera:
      gotoxy(27,6);id = input().upper()
      archiCarrera = Archivo("./datos/carrera.txt")
      lisCarrera = archiCarrera.buscar(id)
      if lisCarrera:
          
          entCarrera = Carrera(lisCarrera[0],lisCarrera[1])
          gotoxy(35,6);print(entCarrera.descripcion)
      else: 
         gotoxy(35,6);print("No existe Carrera con ese codigo[{}]:".format(id))
         time.sleep(1);gotoxy(33,6);print(" "*40)



   valor = validar.solo_decimales("Error: Solo decimales",35,7)
   gotoxy(15,10);print("Esta seguro de Grabar El registro(s/n):")
   gotoxy(54,10);grabar = input().lower()


   if grabar == "s":
        archiMatricula = Archivo("./datos/matriculas.txt")
        lisMatriculas = archiMatricula.leer()
        if lisMatriculas : idSig = int(lisMatriculas[-1][0])+1
        else: idSig=1
        entMatricula = Matricula(idSig,entPeriodo,entEstudiante,entCarrera,valor)
        datos = entMatricula.getEstudiante()
        datos = ';'.join(datos)
        archiMatricula.escribir([datos],"a")                 
        gotoxy(15,11);input("Registro Grabado Satisfactoriamente\n Presione una tecla para continuar...")
   else:
       gotoxy(15,11);input("Registro No fue Grabado\n presione una tecla para continuar...")        


#Agregar Notas

#Notas es otra funcion intersante ya que para poder agregar una nota de un estudiante se pide hasta  4 ides
#diferentes para poder agregar las notas de los dos parciales de un estudiante , las notas tienen un 
#Verificador mas ya que estos deben estar en un rango dado use el de la unemi de  0 a 100 :)
def notas():
   borrarPantalla()
   validar = Valida()     
   gotoxy(20,2);print("MATRICULACIÓN")
   gotoxy(15,4);print("Periodo ID[    ]: ")
   gotoxy(15,5);print("Estudiante ID[    ]: ")
   gotoxy(15,6);print("Materia ID[    ]: ")
   gotoxy(15,7);print("Profesor ID[    ]: ")
   gotoxy(15,8);print("Nota #1 [0-100]: ")
   gotoxy(15,9);print("Nota #2 [0-100]: ")

   lisPeriodo,entPeriodo = [],None
   while not lisPeriodo:
      gotoxy(27,4);id = input().upper()
      archiPeriodo = Archivo("./datos/periodo.txt")
      lisPeriodo = archiPeriodo.buscar(id)
      if lisPeriodo:
          entPeriodo = Periodo(lisPeriodo[0],lisPeriodo[1],lisPeriodo[2]) 
          gotoxy(35,4);print(entPeriodo.descripcion)
      else: 
         gotoxy(35,4);print("No existe Periodo con ese codigo[{}]:".format(id))
         time.sleep(1);gotoxy(33,4);print(" "*40)


   lisEstudiante,entEstudiante = [],None
   while not lisEstudiante:
      gotoxy(30,5);id = input().upper()
      archiEstudiante = Archivo("./datos/estudiantes.txt")
      lisEstudiante = archiEstudiante.buscar(id)
      if lisEstudiante:
          
          entEstudiante = Estudiante(lisEstudiante[0],lisEstudiante[1],lisEstudiante[2],lisEstudiante[3],lisEstudiante[4]) 
          gotoxy(35,5);print(entEstudiante.nombre)
      else: 
         gotoxy(35,5);print("No existe Estudiante con ese codigo[{}]:".format(id))
         time.sleep(1);gotoxy(36,5);print(" "*40)


   lismateria,entmateria = [],None
   while not lismateria:
      gotoxy(27,6);id = input().upper()
      archimateria = Archivo("./datos/materia.txt")
      lismateria = archimateria.buscar(id)
      if lismateria:
          
          entmateria = Materia(lismateria[0],lismateria[1])
          gotoxy(35,6);print(entmateria.descripcion)
      else: 
         gotoxy(35,6);print("No existe materia con ese codigo[{}]:".format(id))
         time.sleep(1);gotoxy(33,6);print(" "*40)

   lisProfesor,entProfesor = [],None
   while not lisProfesor:
      gotoxy(29,7);id = input().upper()
      archiProfesor = Archivo("./datos/profesor.txt")
      lisProfesor = archiProfesor.buscar(id)
      if lisProfesor:
          
          entProfesor = Profesor(lisProfesor[0],lisProfesor[1],lisProfesor[2],lisProfesor[3],lisProfesor[4],lisProfesor[5]) 
          gotoxy(35,7);print(entProfesor.nombre)
      else: 
         gotoxy(35,7);print("No existe Profesor con ese codigo[{}]:".format(id))
         time.sleep(1);gotoxy(36,5);print(" "*40)

   nota1 = -1
   nota2 = -1
   while(nota1<0 or nota1>100):
    nota1 = validar.solo_decimales("Error: Solo decimales",35,8)
    if nota1 <0 or nota1 >100:
       gotoxy(35,8); print("Nota salida del rango [0-100]")
       time.sleep(1)
       gotoxy(35,8);print("  "*40)        

   while(nota2<0 or nota2>100):
    nota2 = validar.solo_decimales("Error: Solo decimales",35,9)

    if nota2 <0 or nota2 >100:
       time.sleep(1)
       gotoxy(35,9);print("  "*40)

   gotoxy(15,10);print("Esta seguro de Grabar El registro(s/n):")
   gotoxy(54,10);grabar = input().lower()


   if grabar == "s":
        archtnotas = Archivo("./datos/notas.txt")
        listnotas = archtnotas.leer()
        if listnotas : idSig = int(listnotas[-1][0])+1
        else: idSig=1
        entnotas = Notas(idSig,entPeriodo,entEstudiante,entmateria,entProfesor,nota1,nota2)
        datos = entnotas.getEstudiante()
        datos = ';'.join(datos)
        archtnotas.escribir([datos],"a")                 
        gotoxy(15,11);input("Registro Grabado Satisfactoriamente\n Presione una tecla para continuar...")
   else:
       gotoxy(15,11);input("Registro No fue Grabado\n presione una tecla para continuar...") 

# Menu Principal
#Aqui el menu principal para poder elegir entre las diferentes opciones 
opc=''
while opc !='4':  
    borrarPantalla()      
    menu = Menu("Menu Principal",["1) Mantenimiento","2) Matriculacion","3) Notas","4) Salir"],20,10)
    opc = menu.menu()
    if opc == "1":
        opc1 = ''
        while opc1 !='6':
            borrarPantalla()    
            menu1 = Menu("Menu Mantenimiento",["1) Carrera","2) Materias","3) Periodos","4) Profesores","5) Estudiantes","6) Salir"],20,10)
            opc1 = menu1.menu()
            if opc1 == "1":
                carreras()
            elif opc1 == "2":
                materias()
            elif opc1 == "3":
                periodos()
            elif opc1 == "4":
                profesores()
            elif opc1 == "5":
                estudiantes()
                        
    elif opc == "2":
            borrarPantalla()
            menu2 = Menu("Menu Matriculacion",["1) Matricula","2) Salir"],20,10)
            opc2 = menu2.menu()
            if opc2 == "1":
                matriculaciones()
                pass
            elif opc2 == "2":
                pass
    elif opc == "3":
            borrarPantalla()
            menu3 = Menu("Menu Notas",["1) Notas","2) Salir"],20,10)
            opc3 = menu3.menu()
            if opc3 == "1":
                notas()
                pass

    elif opc == "4":
           borrarPantalla()
           print("Gracias por su visita....")


    else:
          print("Opcion no valida") 

input("Presione una tecla para salir")
borrarPantalla()

