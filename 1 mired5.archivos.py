
#Recordemos que en este módulo están todos las funciones adicionales que hemos creado.
import coursera1 as Red
#El modulo 'os' nos permitirá consultar si un archivo existe.
import os
Red.mostrar_bienvenida()
nombre = Red.obtener_nombre()
print("Hola ", nombre, ", bienvenido a Mi Red")

#Verificamos si el archivo existe
if Red.existe_archivo(nombre+".user"):
    #Esto lo hacemos si ya habÃ­a un usuario con ese nombre
    print("Leyendo datos de usuario", nombre, "desde archivo.")
    (nombre, edad, estatura_m, estatura_cm, sexo, pais, amigos, estado, muro) = Red.leer_usuario(nombre)

else:
    #En caso que el usuario no exista, consultamos por sus datos tal como lo hacÃ­amos antes
    print()
    edad = Red.obtener_edad()
    (estatura_m, estatura_cm) = Red.obtener_estatura()
    sexo = Red.obtener_sexo()
    pais = Red.obtener_pais()
    amigos = Red.obtener_lista_amigos()
    estado = ""
    muro =[]

#En ambos casos, al llegar aquí=­ ya conocemos los datos del usuario
print("Muy bien. Estos son los datos de tu perfil.")
Red.mostrar_perfil(nombre, edad, estatura_m, estatura_cm, sexo, pais, amigos)
Red.mostrar_mensaje(nombre, estado)

#Ahora podemos mostrar el menu y consultar las opciones
opcion = 1
while opcion != 0:
    opcion = Red.opcion_menu()
    if opcion == 1:
        estado = Red.obtener_mensaje()
        Red.publicar_mensaje(nombre, amigos, estado, muro)

    elif opcion == 2:
        Red.mostrar_muro(muro)

    elif opcion == 3:
        Red.mostrar_perfil(nombre, edad, estatura_m, estatura_cm, sexo, pais, amigos)

    elif opcion == 4:
        edad = Red.obtener_edad()
        (estatura_m, estatura_cm) = Red.obtener_estatura()
        sexo = Red.obtener_sexo()
        pais = Red.obtener_pais()
        amigos = Red.obtener_lista_amigos()
        Red.mostrar_perfil(nombre, edad, estatura_m, estatura_cm, sexo, pais, amigos)
    
    elif opcion == 5:
        nombre2 = Red.obtener_nombre()
        if Red.existe_archivo(nombre2+".user"):
        #Esto lo hacemos si ya habÃ­a un usuario con ese nombre
            Red.escritura_archivo(nombre,edad,estatura_m,estatura_cm,sexo,pais,amigos,estado,muro)
            print("Leyendo datos de usuario", nombre2, "desde archivo.")
            (nombre, edad, estatura_m, estatura_cm, sexo, pais, amigos, estado, muro) = Red.leer_usuario(nombre2)
        else:
            print("No se puede encontrar un archivo con el nombre ", nombre,".user")
            print("Puedes Salir y crearlo si tenes ganas")
    elif opcion ==6:
        nuev_amigo = input("Agrega el nombre de tu nuevo amigo, incluiremos de uno por vez:     ")
        nuev_amigo = nuev_amigo.strip()
        nuev_amigo = nuev_amigo.capitalize()
        amigos.append(nuev_amigo)
    elif opcion ==7:
        #aca leeremos los estados de nuestro amigos
        for i in amigos:
            #ver si archivo existe
            if Red.existe_archivo(i+".user") == False:
                print(i," no forma parte de esta Red, ojalá pronto se cope")
            else:
                with open(i+'.user', 'r') as f:
                    contador = -1
                    last_line = f.readlines()[contador]
                    last_line = last_line.strip()
                    while last_line == "":
                        contador = contador - 1
                        with open(i+'.user', 'r') as f:
                            last_line = f.readlines()[contador]
                            last_line = last_line.strip()
                    f.close
                print(i, " dice: ",last_line)

    elif opcion == 0:
        print("Has decidido salir. Guardando perfil en ",nombre+".user")
        Red.escritura_archivo(nombre,edad,estatura_m,estatura_cm,sexo,pais,amigos,estado, muro)



print("Gracias por usar Mi Red. ¡Hasta pronto!")
