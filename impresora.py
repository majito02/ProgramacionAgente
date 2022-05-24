#Instrucciones
#Ingrese localizacion SALA, CUARTO, DESPACHO, en MAYUSCULAS
#Ingrese estado 0/1 donde 0 significa  imprimir y 1 no esta imprimiendo
#CONSIDERACIONES DE COSTO
# costo+1 si la impresora cambia de estado no imprimiendo a imprimiendo
# costo si la impresora cambia de localización pero esta imprimiendo
def mundo_impresora():
    #inicializar estado_objetivo: 0 indica imprimir, 1 indica no imprimir
    estado_objetivo = {'SALA': '0', 'CUARTO': '0', 'DESPACHO': '0'}
    #Inicializacion de costo
    costo = 0
    #Indicaciones de ingreso
    print("OPCIONES DE LOCALIZACIÓN: SALA - CUARTO - DESPACHO")
    print("OPCIONES DE ESTADO: 0-->esta imprimiendo  1--> no esta imprimiendo")
    #Ingreso de Primera localizacion de archivo a imprimir (Variable de importancia para detectar en que localizacion comienza)
    ingreso_localizacion_1 = input("Ingrese localizacion de archivo a imprimir: ")
    #Ingreso del estado de la primera localizacion (Variable de importancia para establecer el estado del primer lugar)
    ingreso_estado_1 = input("Ingrese estado de " + ingreso_localizacion_1+": ")
    #Ingreso de Segunda localizacion de archivo a imprimir (Variable de importancia para detectar cual es el siguiente lugar del archivo a imprimir)
    ingreso_localizacion_2 = input("Ingrese localizacion de archivo a imprimir: ")
    #Ingreso del estado de la segunda localizacion (Variable de importancia para establecer el estado del segundo lugar) 
    ingreso_estado_2 = input("Ingrese estado de " + ingreso_localizacion_2+": ")
    #Ingreso del estado de la ultima localizacion  (Variable de importancia para establecer el estado del ultimo lugar)
    ingreso_estado_3 = input("INGRESE ESTADO DE LA ULTIMA LOCALIZACION: ")
    #Impresion del estado objetivo
    print("Objetivo deseado" + str(estado_objetivo))
    #Condición si la localizacion 1 es SALA?
    if ingreso_localizacion_1 == 'SALA':
        #Imprime un mensaje que indica que la impresora de la SALA tiene un archivo 
        print("Impresora con archivo en SALA")
        #Condición del estado en SALA cuando es 1
        if ingreso_estado_1 == '1':
            #Imprime un mensaje que indica que no esta imprimiendo en la SALA
            print("Localización: SALA esta por imprimir.......")
            # estableciendo el estado objetivo que es imprimir
            estado_objetivo['SALA'] = '0'
            costo += 1 #Incrementar un costo, ya que no estaba imprimiendo y hará el esfuerzo por imprimir
            print("Imprimiendo archivo de SALA")
            #Mensaje que indica el costo actual 
            print("Costo actual: " + str(costo))
            #Condición cuando la segunda localización es CUARTO
            if ingreso_localizacion_2 == 'CUARTO':
                #Condición cuando es estado es 1 en CUARTO
                if ingreso_estado_2 == '1':
                    #Imprime un mensaje que indica que no esta imprimiendo en el CUARTO
                    print("Localización de  CUARTO no esta imprimiendo.........")
                    # estableciendo el estado objetivo que es imprimir
                    estado_objetivo['CUARTO'] = '0'
                    costo += 1 #Incrementar un costo, ya que no estaba imprimiendo y hará el esfuerzo por imprimir
                    #Mensaje que le indica al usuario que ya esta imprimiendo
                    print("Imprimiendo archivo de CUARTO")
                     #Mensaje que indica el costo actual 
                    print("Costo actual: " + str(costo))
                    #Condición cuando el estado es 1 en DESPACHO
                    if ingreso_estado_3 == '1':
                        #Imprime un mensaje que indica que no esta imprimiendo en el DESPACHO
                        print("Localización: DESPACHO no esta imprimiendo.........")
                        # estableciendo el estado objetivo que es imprimir
                        estado_objetivo['DESPACHO'] = '0'
                        costo += 1 #Incrementar un costo, ya que no estaba imprimiendo y hará el esfuerzo por imprimir
                        #Mensaje que le indica al usuario que ya esta imprimiendo
                        print("Imprimiendo archivo de DESPACHO")
                        #Mensaje que indica el costo actual 
                        print("Costo actual: " + str(costo))
                        #Condición cuando el DESPACHO tiene un estado 0
                    elif ingreso_estado_3 == '0':
                        #Se establece el estado objetivo
                        estado_objetivo['DESPACHO'] = '0'
                       #Se imprime un mensaje que indique que ya está imprimiendo,  y que no existe esfuerzo, mostrando el costo actual
                        print("Localización de DESPACHO ya esta imprimiendo....")
                        print("No hay esfuerzo. Costo Actual:" + str(costo))
                #Condición cuando el CUARTO tiene un estado 0
                elif ingreso_estado_2 == '0':
                    #Se establece el estado objetivo
                    estado_objetivo['CUARTO'] = '0'
                   #Se imprime un mensaje que indique que ya está imprimiendo,  y que no existe esfuerzo, mostrando el costo actual
                    print("Localización de CUARTO ya esta imprimiendo....")
                    print("No hay esfuerzo. Costo Actual:" + str(costo))
                    #Condición cuando el DESPACHO tiene un estado de 1
                    if ingreso_estado_3 == '1':
                        #Imprime un mensaje que indica que no esta imprimiendo en el DESPACHO
                        print("Localización de  DESPACHO no esta imprimiendo.........")
                        #Estableciendo el estado objetivo que es imprimir
                        estado_objetivo['DESPACHO'] = '0'
                        costo += 1 #Incrementar un costo, ya que no estaba imprimiendo y hará el esfuerzo por imprimir
                        #Mensaje que le indica al usuario que ya esta imprimiendo
                        print("Imprimiendo archivo de DESPACHO")
                        #Mensaje que imprime el costo actual 
                        print("Costo actual: " + str(costo))
                    #Condición cuando el estado de DESPACHO es 0
                    elif ingreso_estado_3 == '0':
                        #Se establece el estado objetivo
                        estado_objetivo['DESPACHO'] = '0'
                       #Se imprime un mensaje que indique que ya está imprimiendo,  y que no existe esfuerzo, mostrando el costo actual
                        print("Localización de DESPACHO ya esta imprimiendo....")
                        print("No hay esfuerzo. Costo Actual:" + str(costo))

            #Condición cuando la localización 2 es DESPACHO
            elif ingreso_localizacion_2 == 'DESPACHO':
                #Condición del estado de impresión cuando es 1
                if ingreso_estado_2 == '1':
                    #Imprime un mensaje que indica que no esta imprimiendo en el DESPACHO
                    print("Localización de  DESPACHO no esta imprimiendo.........")
                    #Estableciendo el estado objetivo que es imprimir
                    estado_objetivo['DESPACHO'] = '0'
                    costo += 1 #Incrementar un costo, ya que no estaba imprimiendo y hará el esfuerzo por imprimir
                    #Mensaje que le indica al usuario que ya esta imprimiendo
                    print("Imprimiendo archivo de DESPACHO")
                    #Mensaje que indica el costo actual 
                    print("Costo actual: " + str(costo))
                    #Condición cuando el estado en CUARTO es 1
                    if ingreso_estado_3 == '1':
                        #Imprime un mensaje que indica que no esta imprimiendo en el CUARTO
                        print("Localización: CUARTO no esta imprimiendo.........")
                        #Estableciendo el estado objetivo que es imprimir
                        estado_objetivo['CUARTO'] = '0'
                        costo += 1 #Incrementar un costo, ya que no estaba imprimiendo y hará el esfuerzo por imprimir
                        #Mensaje que le indica al usuario que ya esta imprimiendo
                        print("Imprimiendo archivo de CUARTO")
                        #Mensaje que imprime el costo actual
                        print("Costo actual: " + str(costo))
                    #Condición cuando el estado de Cuarto es 0
                    elif ingreso_estado_3 == '0':
                        #Se establece el estado objetivo
                        estado_objetivo['CUARTO'] = '0'
                        #Se imprime un mensaje que indique que ya está imprimiendo,  y que no existe esfuerzo, mostrando el costo actual
                        print("Localización de CUARTO ya esta imprimiendo....")
                        print("No hay esfuerzo. Costo Actual:" + str(costo))
                #Condición cuando el estado de DESPACHO es 0
                elif ingreso_estado_2 == '0':
                    #Se establece el estado objetivo
                    estado_objetivo['DESPACHO'] = '0'
                   #Se imprime un mensaje que indique que ya está imprimiendo,  y que no existe esfuerzo, mostrando el costo actual
                    print("Localización de DESPACHO ya esta imprimiendo....")
                    print("No hay esfuerzo. Costo Actual:" + str(costo))
                    #Condición cuando el estado es 1 en el CUARTO
                    if ingreso_estado_3 == '1':
                        #Imprime un mensaje que indica que no esta imprimiendo en el CUARTO
                        print("Localización de  CUARTO no esta imprimiendo.........")
                        #Estableciendo el estado objetivo que es imprimir
                        estado_objetivo['CUARTO'] = '0'
                        costo += 1 #Incrementar un costo, ya que no estaba imprimiendo y hará el esfuerzo por imprimir
                        #Mensaje que le indica al usuario que ya esta imprimiendo
                        print("Imprimiendo archivo de CUARTO")
                        #Mensaje que imprime el costo actual
                        print("Costo actual: " + str(costo))
                    #Condición cuando el estado del CUARTO es 0
                    elif ingreso_estado_3 == '0':
                        #Se establece el estado objetivo
                        estado_objetivo['CUARTO'] = '0'
                       #Se imprime un mensaje que indique que ya está imprimiendo,  y que no existe esfuerzo, mostrando el costo actual
                        print("Localización de CUARTO ya esta imprimiendo....")
                        print("No hay esfuerzo. Costo Actual:" + str(costo))
        #Condición cuando el estado es 0 en la SALA
        elif ingreso_estado_1 == '0':
            #Se establece el estado objetivo
            estado_objetivo['SALA'] = '0'
           #Se imprime un mensaje que indique que ya está imprimiendo,  y que no existe esfuerzo, mostrando el costo actual
            print("Localización: SALA ya esta imprimiendo....")
            print("No hay esfuerzo. Costo Actual:" + str(costo))
            #Condición cuando la localización es el CUARTO 
            if ingreso_localizacion_2 == 'CUARTO':
                #Condición cuando el estado de impresión es 1
                if ingreso_estado_2 == '1':
                    #Imprime un mensaje que indica que no esta imprimiendo en el CUARTO
                    print("Localización de  CUARTO no esta imprimiendo.........")
                    costo += 1 #Incrementar un costo, ya que no estaba imprimiendo y hará el esfuerzo por imprimir
                    #Estableciendo el estado objetivo que es imprimir
                    estado_objetivo['CUARTO'] = '0'
                    #Mensaje que le indica al usuario que ya esta imprimiendo
                    print("Imprimiendo archivo de SALA")
                    #Mensaje que imprime el costo actual
                    print("Costo actual: " + str(costo))
                    #Condición del estado de impresión cuando es 1 en el DESPACHO
                    if ingreso_estado_3 == '1':
                        #Imprime un mensaje que indica que no esta imprimiendo en el DESPACHO
                        print("Localización: DESPACHO no esta imprimiendo.........")
                        #Estableciendo el estado objetivo que es imprimir
                        estado_objetivo['DESPACHO'] = '0'
                        costo += 1 #Incrementar un costo, ya que no estaba imprimiendo y hará el esfuerzo por imprimir
                        #Mensaje que le indica al usuario que ya esta imprimiendo
                        print("Imprimiendo archivo de DESPACHO")
                        #Mensaje que imprime el costo actual
                        print("Costo actual: " + str(costo))
                    #Condición cuando el estado es igual a 0 en el DESPACHO
                    elif ingreso_estado_3 == '0':
                        #Se establece el estado objetivo
                        estado_objetivo['DESPACHO'] = '0'
                       #Se imprime un mensaje que indique que ya está imprimiendo,  y que no existe esfuerzo, mostrando el costo actual
                        print("Localización de DESPACHO ya esta imprimiendo....")
                        print("No hay esfuerzo. Costo Actual:" + str(costo))
                #Condición cuando el estado es 0 en el CUARTO
                elif ingreso_estado_2 == '0':
                    #Se establece el estado objetivo
                    estado_objetivo['CUARTO'] = '0'
                   #Se imprime un mensaje que indique que ya está imprimiendo,  y que no existe esfuerzo, mostrando el costo actual
                    print("Localización de CUARTO ya esta imprimiendo....")
                    print("No hay esfuerzo. Costo Actual:" + str(costo))
                    #Condición del estado de impresión cuando es 1 en el DESPACHO
                    if ingreso_estado_3 == '1':
                        #Imprime un Imprime un mensaje que indica que no esta imprimiendo en el DESPACHO
                        print("Localización de  DESPACHO no esta imprimiendo.........")
                        #Estableciendo el estado objetivo que es imprimir
                        estado_objetivo['DESPACHO'] = '0'
                        costo += 1 #Incrementar un costo, ya que no estaba imprimiendo y hará el esfuerzo por imprimir
                        #Mensaje que le indica al usuario que ya esta imprimiendo
                        print("Imprimiendo archivo de DESPACHO")
                        #Mensaje que imprime el costo actual
                        print("Costo actual: " + str(costo))
                    #Condición cuando el estado es 0 en el DESPACHO
                    elif ingreso_estado_3 == '0':
                        #Se establece el estado objetivo
                        estado_objetivo['DESPACHO'] = '0'
                       #Se imprime un mensaje que indique que ya está imprimiendo,  y que no existe esfuerzo, mostrando el costo actual
                        print("Localización de DESPACHO ya esta imprimiendo....")
                        print("No hay esfuerzo. Costo Actual:" + str(costo))
            #Condición cuando la localicación es el DESPACHO
            elif ingreso_localizacion_2 == 'DESPACHO':
                #Condición cuando el estado es 1 en el DESPACHO
                if ingreso_estado_2 == '1':
                    #Imprime un mensaje indicando que no esta imprimiendoen el DESPACHO
                    print("Localización de  DESPACHO no esta imprimiendo.........")
                    #Estableciendo el estado objetivo que es imprimir
                    estado_objetivo['DESPACHO'] = '0'
                    costo += 1 #Incrementar un costo, ya que no estaba imprimiendo y hará el esfuerzo por imprimir
                    #Mensaje que le indica al usuario que ya esta imprimiendo
                    print("Imprimiendo archivo de DESPACHO")
                    #Mensaje que imprime el costo actual
                    print("Costo actual: " + str(costo))
                    #Condición cuando el estado es 1 en el CUARTO
                    if ingreso_estado_3 == '1':
                        #Imprime un mensaje indicando que no esta imprimiendo
                        print("Localización: CUARTO no esta imprimiendo.........")
                        #Estableciendo el estado objetivo que es imprimir
                        estado_objetivo['CUARTO'] = '0'
                        costo += 1 #Incrementar un costo, ya que no estaba imprimiendo y hará el esfuerzo por imprimir
                        #Mensaje que le indica al usuario que ya esta imprimiendo
                        print("Imprimiendo archivo de CUARTO")
                        #Mensaje que imprime el costo actual
                        print("Costo actual: " + str(costo))
                    #Condición cuando el estado es 0 en el CUARTO 
                    elif ingreso_estado_3 == '0':
                        #Se establece el estado objetivo
                        estado_objetivo['CUARTO'] = '0'
                       #Se imprime un mensaje que indique que ya está imprimiendo,  y que no existe esfuerzo, mostrando el costo actual
                        print("Localización de CUARTO ya esta imprimiendo....")
                        print("No hay esfuerzo. Costo Actual:" + str(costo))
                #Condición cuando el estado es 0 en el DESPACHO
                elif ingreso_estado_2 == '0':
                    #Se establece el estado objetivo
                    estado_objetivo['DESPACHO'] = '0'
                    ##Se imprime un mensaje al usuario que indique que ya esta imprimiendo y que no existe esfuerzo, mostrando el costo actual
                    print("Localización de DESPACHO ya esta imprimiendo....")
                    print("No hay esfuerzo. Costo Actual:" + str(costo))
                    #Condición cuando el estado es 1 en el CUARTO
                    if ingreso_estado_3 == '1':
                        #Imprime un mensaje indicando que no esta imprimiendo
                        print("Localización de  CUARTO no esta imprimiendo.........")
                          #Estableciendo el estado objetivo que es imprimir
                        estado_objetivo['CUARTO'] = '0'
                        costo += 1 #Incrementar un costo, ya que no estaba imprimiendo y hará el esfuerzo por imprimir
                        #Mensaje que le indica al usuario que ya esta imprimiendo
                        print("Imprimiendo archivo de CUARTO")
                        #Mensaje que imprime el costo actual
                        print("Costo actual: " + str(costo))
                    #condición cuando el estado de CUARTO es 0
                    elif ingreso_estado_3 == '0':
                        #Se establece el estado objetivo
                        estado_objetivo['CUARTO'] = '0'
                       #Se imprime un mensaje que indique que ya está imprimiendo,  y que no existe esfuerzo, mostrando el costo actual
                        print("Localización de CUARTO ya esta imprimiendo....")
                        print("No hay esfuerzo. Costo Actual:" + str(costo))
    #Condición cuando la localizacion 1 es CUARTO
    elif ingreso_localizacion_1 == 'CUARTO':
        # Imprime un mensaje indicando que hay un archivo en la impresora del CUARTO
        print("Impresora con archivo en CUARTO")
        #Condición de estado cuando en CUARTO es 1
        if ingreso_estado_1 == '1':
            #Imprime un mensaje indicando que no esta imprimiendo
            print("Localización: CUARTO no esta imprimiendo.........")
              #Estableciendo el estado objetivo que es imprimir
            estado_objetivo['CUARTO'] = '0'
            costo += 1 #Incrementar un costo, ya que no estaba imprimiendo y hará el esfuerzo por imprimir
                    #Mensaje que le indica al usuario que ya esta imprimiendo
            print("Imprimiendo archivo de CUARTO")
            #Mensaje que imprime el costo actual
            print("Costo actual: " + str(costo))
            #Condición cuando la localización es SALA
            if ingreso_localizacion_2 == 'SALA':
                #Condición cuando el estado de SALA es 1
                if ingreso_estado_2 == '1':
                    #Imprime un mensaje indicando que no esta imprimiendo
                    print("Localización de  SALA no esta imprimiendo.........")
                      #Estableciendo el estado objetivo que es imprimir
                    estado_objetivo['SALA'] = '0'
                    costo += 1 #Incrementar un costo, ya que no estaba imprimiendo y hará el esfuerzo por imprimir
                    #Mensaje que le indica al usuario que ya esta imprimiendo
                    print("Imprimiendo archivo de SALA")
                    #Mensaje que imprime el costo actual
                    print("Costo actual: " + str(costo))
                    #Condición del estado de impresión cuando es 1 en el DESPACHO
                    if ingreso_estado_3 == '1':
                        #Imprime un mensaje indicando que no esta imprimiendo
                        print("Localización: DESPACHO no esta imprimiendo.........")
                        #Estableciendo el estado objetivo que es imprimir
                        estado_objetivo['DESPACHO'] = '0'
                        costo += 1 #Incrementar un costo, ya que no estaba imprimiendo y hará el esfuerzo por imprimir
                        #Mensaje que le indica al usuario que ya esta imprimiendo
                        print("Imprimiendo archivo de DESPACHO")
                        #Mensaje que imprime el costo actual
                        print("Costo actual: " + str(costo))
                    #Condición cuando el estado en el DESPACHO es 0
                    elif ingreso_estado_3 == '0':
                        #Se establece el estado objetivo
                        estado_objetivo['DESPACHO'] = '0'
                       #Se imprime un mensaje que indique que ya está imprimiendo,  y que no existe esfuerzo, mostrando el costo actual
                        print("Localización de DESPACHO ya esta imprimiendo....")
                        print("No hay esfuerzo. Costo Actual:" + str(costo))
                #Condición cuando el estado de la SALA es 0
                elif ingreso_estado_2 == '0':
                    #Se establece el estado objetivo
                    estado_objetivo['SALA'] = '0'
                   #Se imprime un mensaje que indique que ya está imprimiendo,  y que no existe esfuerzo, mostrando el costo actual
                    print("Localización de SALA ya esta imprimiendo....")
                    print("No hay esfuerzo. Costo Actual:" + str(costo))
                    #Condición del estado de impresión cuando es 1 en el DESPACHO
                    if ingreso_estado_3 == '1':
                          #Imprime un mensaje indicando que no esta imprimiendo
                        print("Localización de  DESPACHO no esta imprimiendo.........")
                        #Estableciendo el estado objetivo que es imprimir
                        estado_objetivo['DESPACHO'] = '0'
                        costo += 1 #Incrementar un costo, ya que no estaba imprimiendo y hará el esfuerzo por imprimir
                        #Mensaje que le indica al usuario que ya esta imprimiendo
                        print("Imprimiendo archivo de DESPACHO")
                        #Mensaje que imprime el costo actual
                        print("Costo actual: " + str(costo))
                    #Condición cuando el estado es 0 en el DESPACHO
                    elif ingreso_estado_3 == '0':
                        #Se establece el estado objetivo
                        estado_objetivo['DESPACHO'] = '0'
                       #Se imprime un mensaje que indique que ya está imprimiendo,  y que no existe esfuerzo, mostrando el costo actual
                        print("Localización de DESPACHO ya esta imprimiendo....")
                        print("No hay esfuerzo. Costo Actual:" + str(costo))
            #Condición cuando la segunda localización es el DESPACHO
            elif ingreso_localizacion_2 == 'DESPACHO':
                #Condición para establecer el estado de la impresora en el DESPACHO
                if ingreso_estado_2 == '1':
                    #Imprime un mensaje indicando que no esta imprimiendo
                    print("Localización de  DESPACHO no esta imprimiendo.........")
                      #Estableciendo el estado objetivo que es imprimir
                    estado_objetivo['DESPACHO'] = '0'
                    costo += 1 #Incrementar un costo, ya que no estaba imprimiendo y hará el esfuerzo por imprimir
                    #Mensaje que le indica al usuario que ya esta imprimiendo
                    print("Imprimiendo archivo de DESPACHO")
                    #Mensaje que imprime el costo actual
                    print("Costo actual: " + str(costo))
                    #Condición del estado de impresión cuando es 1 en la SALA
                    if ingreso_estado_3 == '1':
                        #Imprime un mensaje que indica que no esta imprimiendo
                        print("Localización: SALA no esta imprimiendo.........")
                        #Estableciendo el estado objetivo que es imprimir
                        estado_objetivo['SALA'] = '0'
                        costo += 1 #Incrementar un costo, ya que no estaba imprimiendo y hará el esfuerzo por imprimir
                        #Mensaje que le indica al usuario que ya esta imprimiendo
                        print("Imprimiendo archivo de SALA")
                        #Mensaje que imprime el costo actual
                        print("Costo actual: " + str(costo))
                    #Condición cuando el estado es 0 en SALA
                    elif ingreso_estado_3 == '0':
                        #Se establece el estado objetivo
                        estado_objetivo['SALA'] = '0'
                        #Se imprime un mensaje que indique que ya está imprimiendo,  y que no existe esfuerzo, mostrando el costo actual
                        print("Localización de SALA ya esta imprimiendo....")
                        print("No hay esfuerzo. Costo Actual:" + str(costo))
                #Condición cuando el estado es 0 en DESPACHO
                elif ingreso_estado_2 == '0':
                    #Se establece el estado objetivo
                    estado_objetivo['DESPACHO'] = '0'
                   #Se imprime un mensaje que indique que ya está imprimiendo,  y que no existe esfuerzo, mostrando el costo actual
                    print("Localización de DESPACHO ya esta imprimiendo....")
                    print("No hay esfuerzo. Costo Actual:" + str(costo))
                    #Condición del estado de impresión cuando es 1 en la SALA
                    if ingreso_estado_3 == '1':
                        #Imprime un mensaje que indica que no esta imprimiendo
                        print("Localización de  SALA no esta imprimiendo.........")
                        #Estableciendo el estado objetivo que es imprimir
                        estado_objetivo['SALA'] = '0'
                        costo += 1 #Incrementar un costo, ya que no estaba imprimiendo y hará el esfuerzo por imprimir
                        #Mensaje que le indica al usuario que ya esta imprimiendo
                        print("Imprimiendo archivo de SALA")
                        #Mensaje que imprime el costo actual
                        print("Costo actual: " + str(costo))
                    #Condición cuando el estado de la SALA es 0
                    elif ingreso_estado_3 == '0':
                        #Se establece el estado objetivo
                        estado_objetivo['SALA'] = '0'
                        #Se imprime un mensaje que indique que ya está imprimiendo,  y que no existe esfuerzo, mostrando el costo actual
                        print("Localización de SALA ya esta imprimiendo....")
                        print("No hay esfuerzo. Costo Actual:" + str(costo))
        #Condición cuando el estado del CUARTO es 0
        elif ingreso_estado_1 == '0':
            #Se establece el estado objetivo
            estado_objetivo['CUARTO'] = '0'
           #Se imprime un mensaje que indique que ya está imprimiendo,  y que no existe esfuerzo, mostrando el costo actual
            print("Localización: CUARTO ya esta imprimiendo....")
            print("No hay esfuerzo. Costo Actual:" + str(costo))
            #Condición cuando la segunda localización es SALA
            if ingreso_localizacion_2 == 'SALA':
                #Condición cuando el estado de la SALA es 1
                if ingreso_estado_2 == '1':
                    #Imprime un mensaje indicando que no esta imprimiendo
                    print("Localización de  SALA no esta imprimiendo.........")   
                    #Estableciendo el estado objetivo que es imprimir
                    estado_objetivo['SALA'] = '0'
                    costo += 1 #Incrementar un costo, ya que no estaba imprimiendo y hará el esfuerzo por imprimir
                    #Mensaje que le indica al usuario que ya esta imprimiendo
                    print("Imprimiendo archivo de SALA")
                    #Mensaje que imprime el costo actual
                    print("Costo actual: " + str(costo))
                    #Condición del estado de impresión cuando es 1 en el DESPACHO
                    if ingreso_estado_3 == '1':
                        #Imprime un mensaje indicando que no esta imprimiendo
                        print("Localización: DESPACHO no esta imprimiendo.........")
                        #Estableciendo el estado objetivo que es imprimir
                        estado_objetivo['DESPACHO'] = '0'
                        costo += 1 #Incrementar un costo, ya que no estaba imprimiendo y hará el esfuerzo por imprimir
                        #Mensaje que le indica al usuario que ya esta imprimiendo
                        print("Imprimiendo archivo de DESPACHO")
                        #Mensaje que imprime el costo actual
                        print("Costo actual: " + str(costo))
                    #Condición cuando el estado del DESPACHO es 0
                    elif ingreso_estado_3 == '0':
                        #Se establece el estado objetivo
                        estado_objetivo['DESPACHO'] = '0'
                       #Se imprime un mensaje que indique que ya está imprimiendo,  y que no existe esfuerzo, mostrando el costo actual
                        print("Localización de DESPACHO ya esta imprimiendo....")
                        print("No hay esfuerzo. Costo Actual:" + str(costo))
                #Condición cuando el estado de la SALA es 0
                elif ingreso_estado_2 == '0':
                    #Se establece el estado objetivo
                    estado_objetivo['SALA'] = '0'
                   #Se imprime un mensaje que indique que ya está imprimiendo,  y que no existe esfuerzo, mostrando el costo actual
                    print("Localización de SALA ya esta imprimiendo....")
                    print("No hay esfuerzo. Costo Actual:" + str(costo))
                    #Condición del estado de impresión cuando es 1 en el DESPACHO 
                    if ingreso_estado_3 == '1':
                        #Imprime un mensaje indicando que no esta imprimiendo
                        print("Localización de  DESPACHO no esta imprimiendo.........")
                        #Estableciendo el estado objetivo que es imprimir
                        estado_objetivo['DESPACHO'] = '0'
                        costo += 1 #Incrementar un costo, ya que no estaba imprimiendo y hará el esfuerzo por imprimir
                        #Mensaje que le indica al usuario que ya esta imprimiendo
                        print("Imprimiendo archivo de DESPACHO")
                        #Mensaje que imprime el costo actual
                        print("Costo actual: " + str(costo))
                    #Condición cuando el estado es 0 en el DESPACHO
                    elif ingreso_estado_3 == '0':
                        #Se establece el estado objetivo
                        estado_objetivo['DESPACHO'] = '0'
                       #Se imprime un mensaje que indique que ya está imprimiendo,  y que no existe esfuerzo, mostrando el costo actual
                        print("Localización de DESPACHO ya esta imprimiendo....")
                        print("No hay esfuerzo. Costo Actual:" + str(costo))
            #Condición cuando la segunda localización es el DESPACHO
            elif ingreso_localizacion_2 == 'DESPACHO':
                #Condición cuando el estado del DESPACHO es 1
                if ingreso_estado_2 == '1':
                    #Imprime un mensaje indicando que no esta imprimiendo
                    print("Localización de  DESPACHO no esta imprimiendo.........")
                    #Estableciendo el estado objetivo que es imprimir
                    estado_objetivo['DESPACHO'] = '0'
                    costo += 1 #Incrementar un costo, ya que no estaba imprimiendo y hará el esfuerzo por imprimir
                    #Mensaje que le indica al usuario que ya esta imprimiendo
                    print("Imprimiendo archivo de DESPACHO")
                    #Mensaje que imprime el costo actual
                    print("Costo actual: " + str(costo)) 
                    #Condición del estado de impresión cuando es 1 en la SALA
                    if ingreso_estado_3 == '1':
                        #Imprime un mensaje indicando que no esta imprimiendo
                        print("Localización: SALA no esta imprimiendo.........")
                        #Estableciendo el estado objetivo que es imprimir
                        estado_objetivo['SALA'] = '0'
                        costo += 1 #Incrementar un costo, ya que no estaba imprimiendo y hará el esfuerzo por imprimir
                        #Mensaje que le indica al usuario que ya esta imprimiendo
                        print("Imprimiendo archivo de SALA")
                        #Mensaje que imprime el costo actual
                        print("Costo actual: " + str(costo))
                    #Condición cuando el estado de la SALA es 0
                    elif ingreso_estado_3 == '0':
                        #Se establece el estado objetivo
                        estado_objetivo['SALA'] = '0'
                       #Se imprime un mensaje que indique que ya está imprimiendo,  y que no existe esfuerzo, mostrando el costo actual
                        print("Localización de SALA ya esta imprimiendo....")
                        print("No hay esfuerzo. Costo Actual:" + str(costo))
                #Condición cuando el estado del DESPACHO es 0
                elif ingreso_estado_2 == '0':
                    #Se establece el estado objetivo
                    estado_objetivo['DESPACHO'] = '0'
                   #Se imprime un mensaje que indique que ya está imprimiendo,  y que no existe esfuerzo, mostrando el costo actual
                    print("Localización de DESPACHO ya esta imprimiendo....")
                    print("No hay esfuerzo. Costo Actual:" + str(costo))
                    #Condición cuando el estado de SALA es 1
                    if ingreso_estado_3 == '1':
                        #Imprime un mensaje indicando que no esta imprimiendo
                        print("Localización de  SALA no esta imprimiendo.........")
                        #Estableciendo el estado objetivo que es imprimir
                        estado_objetivo['SALA'] = '0'
                        costo += 1 #Incrementar un costo, ya que no estaba imprimiendo y hará el esfuerzo por imprimir
                        #Mensaje que le indica al usuario que ya esta imprimiendo
                        print("Imprimiendo archivo de SALA")
                         #Mensaje que imprime el costo actual
                        print("Costo actual: " + str(costo))
                    #Condición cuando el estado de la SALA es 0
                    elif ingreso_estado_3 == '0':
                        #Se establece el estado objetivo
                        estado_objetivo['SALA'] = '0'
                       #Se imprime un mensaje que indique que ya está imprimiendo,  y que no existe esfuerzo, mostrando el costo actual
                        print("Localización de SALA ya esta imprimiendo....")
                        print("No hay esfuerzo. Costo Actual:" + str(costo))
    #Condición para verificar si la primera localización es el DESPACHO
    elif ingreso_localizacion_1 == 'DESPACHO':
        #Imprime un mensaje indicando la impresora va imprimir un archivo en el DESPACHO
        print("Impresora con archivo en DESPACHO")
        #Condición cuando el estado es 1 en el DESPACHO
        if ingreso_estado_1 == '1':
            #Imprime un mensaje indicando que no esta imprimiendo
            print("Localización: DESPACHO no esta imprimiendo.........")
            #Estableciendo el estado objetivo que es imprimir
            estado_objetivo['DESPACHO'] = '0'
            costo += 1 #Incrementar un costo, ya que no estaba imprimiendo y hará el esfuerzo por imprimir
                    #Mensaje que le indica al usuario que ya esta imprimiendo
            print("Imprimiendo archivo de DESPACHO")
            #Mensaje que imprime el costo actual
            print("Costo actual: " + str(costo))
            #Condición cuando la segunda localización es SALA
            if ingreso_localizacion_2 == 'SALA':
                #Condición cuando el estado de la SALA es 1
                if ingreso_estado_2 == '1':
                    #Imprime un mensaje indicando que no esta imprimiendo
                    print("Localización de  SALA no esta imprimiendo.........")
                    #Estableciendo el estado objetivo que es imprimir
                    estado_objetivo['SALA'] = '0'
                    costo += 1 #Incrementar un costo, ya que no estaba imprimiendo y hará el esfuerzo por imprimir
                    #Mensaje que le indica al usuario que ya esta imprimiendo
                    print("Imprimiendo archivo de SALA")
                    #Mensaje que imprime el costo actual
                    print("Costo actual: " + str(costo))
                    #Condición del estado de impresión cuando es 1 en el CUARTO
                    if ingreso_estado_3 == '1':
                        #Imprime un mensaje que indica que no esta imprimiendo
                        print("Localización: CUARTO no esta imprimiendo.........")
                        #Estableciendo el estado objetivo que es imprimir
                        estado_objetivo['CUARTO'] = '0'
                        costo += 1 #Incrementar un costo, ya que no estaba imprimiendo y hará el esfuerzo por imprimir
                        #Mensaje que le indica al usuario que ya esta imprimiendo
                        print("Imprimiendo archivo de CUARTO")
                        #Mensaje que imprime el costo actual
                        print("Costo actual: " + str(costo))
                    #Condición cuando el estado de CUARTO es 0
                    elif ingreso_estado_3 == '0':
                        #Se establece el estado objetivo
                        estado_objetivo['CUARTO'] = '0'
                       #Se imprime un mensaje que indique que ya está imprimiendo,  y que no existe esfuerzo, mostrando el costo actual
                        print("Localización de CUARTO ya esta imprimiendo....")
                        print("No hay esfuerzo. Costo Actual:" + str(costo))
                #Condición cuando el estado de SALA es 0
                elif ingreso_estado_2 == '0':
                    #Se establece el estado objetivo
                    estado_objetivo['SALA'] = '0'
                   #Se imprime un mensaje que indique que ya está imprimiendo,  y que no existe esfuerzo, mostrando el costo actual
                    print("Localización de SALA ya esta imprimiendo....")
                    print("No hay esfuerzo. Costo Actual:" + str(costo))
                    #Condición cuando el estado es 1 en el CUARTO
                    if ingreso_estado_3 == '1':
                        #Imprime un mensaje indicando que no esta imprimiendo
                        print("Localización de  CUARTO no esta imprimiendo.........")
                        #Estableciendo el estado objetivo que es imprimir
                        estado_objetivo['CUARTO'] = '0'
                        costo += 1 #Incrementar un costo, ya que no estaba imprimiendo y hará el esfuerzo por imprimir
                        #Mensaje que le indica al usuario que ya esta imprimiendo
                        print("Imprimiendo archivo de CUARTO")
                        #Mensaje que imprime el costo actual
                        print("Costo actual: " + str(costo))
                    #Condición cuando el estado es 0 en el CUARTO
                    elif ingreso_estado_3 == '0':
                        #Se establece el estado objetivo
                        estado_objetivo['CUARTO'] = '0'
                       #Se imprime un mensaje que indique que ya está imprimiendo,  y que no existe esfuerzo, mostrando el costo actual
                        print("Localización de CUARTO ya esta imprimiendo....")
                        print("No hay esfuerzo. Costo Actual:" + str(costo))
            #Condición cuando la segunda localización es el CUARTO
            elif ingreso_localizacion_2 == 'CUARTO':
                #Condición cuando el estado del CUARTO es 1
                if ingreso_estado_2 == '1':
                   #Imprime un mensaje que indica que no esta imprimiendo
                    print("Localización de  CUARTO no esta imprimiendo.........")
                    #Estableciendo el estado objetivo que es imprimir
                    estado_objetivo['CUARTO'] = '0'
                    costo += 1 #Incrementar un costo, ya que no estaba imprimiendo y hará el esfuerzo por imprimir
                    #Mensaje que le indica al usuario que ya esta imprimiendo
                    print("Imprimiendo archivo de CUARTO")
                    #Mensaje que imprime el costo actual
                    print("Costo actual: " + str(costo))
                    #Condición cuando el estado de la SALA es 1
                    if ingreso_estado_3 == '1':
                        #Imprime un mensaje que indica que no esta imprimiendo
                        print("Localización: SALA no esta imprimiendo.........")
                        #Estableciendo el estado objetivo que es imprimir
                        estado_objetivo['SALA'] = '0'
                        costo += 1 #Incrementar un costo, ya que no estaba imprimiendo y hará el esfuerzo por imprimir
                        #Mensaje que le indica al usuario que ya esta imprimiendo
                        print("Imprimiendo archivo de SALA")
                        #Mensaje que imprime el costo actual
                        print("Costo actual: " + str(costo))
                    #Condición cuando el estado de la SALA es 0
                    elif ingreso_estado_3 == '0':
                        #Se establece el estado objetivo
                        estado_objetivo['SALA'] = '0'
                       #Se imprime un mensaje que indique que ya está imprimiendo,  y que no existe esfuerzo, mostrando el costo actual
                        print("Localización de SALA ya esta imprimiendo....")
                        print("No hay esfuerzo. Costo Actual:" + str(costo))
                #Condición cuando el estado del CUARTO es 0
                elif ingreso_estado_2 == '0':
                    #Se establece el estado objetivo
                    estado_objetivo['CUARTO'] = '0'
                   #Se imprime un mensaje que indique que ya está imprimiendo,  y que no existe esfuerzo, mostrando el costo actual
                    print("Localización de CUARTO ya esta imprimiendo....")
                    print("No hay esfuerzo. Costo Actual:" + str(costo))
                    #Condición cuando el estado de la SALA es 1
                    if ingreso_estado_3 == '1':
                        #Imprime un mensaje indicando que no esta imprimiendo
                        print("Localización de  SALA no esta imprimiendo.........")    
                        #Estableciendo el estado objetivo que es imprimir
                        estado_objetivo['SALA'] = '0'
                        costo += 1 #Incrementar un costo, ya que no estaba imprimiendo y hará el esfuerzo por imprimir
                        #Mensaje que le indica al usuario que ya esta imprimiendo
                        print("Imprimiendo archivo de SALA")
                        #Mensaje que imprime el costo actual
                        print("Costo actual: " + str(costo))
                    #Condición cuando el estado de la SALA es 0
                    elif ingreso_estado_3 == '0':
                        #Se establece el estado objetivo
                        estado_objetivo['SALA'] = '0'
                       #Se imprime un mensaje que indique que ya está imprimiendo,  y que no existe esfuerzo, mostrando el costo actual
                        print("Localización de SALA ya esta imprimiendo....")
                        print("No hay esfuerzo. Costo Actual:" + str(costo))
        #Condición cuando el estado del DESPACHO es 0
        elif ingreso_estado_1 == '0':
            #Se establece el estado objetivo
            estado_objetivo['DESPACHO'] = '0'
           #Se imprime un mensaje que indique que ya está imprimiendo,  y que no existe esfuerzo, mostrando el costo actual
            print("Localización: DESPACHO ya esta imprimiendo....")
            print("No hay esfuerzo. Costo Actual:" + str(costo))
            #Condición cuando la segunda localización es SALA
            if ingreso_localizacion_2 == 'SALA':
                #Condición cuando el estado de la SALA es 1
                if ingreso_estado_2 == '1':
                    #Imprime un mensaje indicando que no esta imprimiendo
                    print("Localización de  SALA no esta imprimiendo.........")
                    #Estableciendo el estado objetivo que es imprimir
                    estado_objetivo['SALA'] = '0'
                    costo += 1 #Incrementar un costo, ya que no estaba imprimiendo y hará el esfuerzo por imprimir
                    #Mensaje que le indica al usuario que ya esta imprimiendo
                    print("Imprimiendo archivo de SALA")
                    #Mensaje que imprime el costo actual
                    print("Costo actual: " + str(costo))
                    #Condición cuando el estado es 1 en el CUARTO
                    if ingreso_estado_3 == '1':
                        #Imprime un mensaje indicando que no esta imprimiendo
                        print("Localización: CUARTO no esta imprimiendo.........")
                        #Estableciendo el estado objetivo que es imprimir
                        estado_objetivo['CUARTO'] = '0'
                        costo += 1 #Incrementar un costo, ya que no estaba imprimiendo y hará el esfuerzo por imprimir
                        #Mensaje que le indica al usuario que ya esta imprimiendo
                        print("Imprimiendo archivo de CUARTO")
                        #Mensaje que imprime el costo actual
                        print("Costo actual: " + str(costo))
                    #Condición cuando el estado es 0 en CUARTO
                    elif ingreso_estado_3 == '0':
                        #Se establece el estado objetivo
                        estado_objetivo['CUARTO'] = '0'
                       #Se imprime un mensaje que indique que ya está imprimiendo,  y que no existe esfuerzo, mostrando el costo actual
                        print("Localización de CUARTO ya esta imprimiendo....")
                        print("No hay esfuerzo. Costo Actual:" + str(costo))
                #Condición cuando el estado de SALA es 0
                elif ingreso_estado_2 == '0':
                    #Se establece el estado objetivo
                    estado_objetivo['SALA'] = '0'
                   #Se imprime un mensaje que indique que ya está imprimiendo,  y que no existe esfuerzo, mostrando el costo actual
                    print("Localización de SALA ya esta imprimiendo....")
                    print("No hay esfuerzo. Costo Actual:" + str(costo)) 
                    #Condición cuando el estado es 1 en el CUARTO
                    if ingreso_estado_3 == '1':
                        #Imprime un mensaje que indica que no esta imprimiendo
                        print("Localización de  CUARTO no esta imprimiendo.........")
                        #Estableciendo el estado objetivo que es imprimir
                        estado_objetivo['CUARTO'] = '0'
                        costo += 1 #Incrementar un costo, ya que no estaba imprimiendo y hará el esfuerzo por imprimir
                        #Mensaje que le indica al usuario que ya esta imprimiendo
                        print("Imprimiendo archivo de CUARTO")
                        #Mensaje que imprime el costo actual
                        print("Costo actual: " + str(costo))
                    #Condición cuando el estado de CUARTO es 0
                    elif ingreso_estado_3 == '0':
                        #Se establece el estado objetivo
                        estado_objetivo['CUARTO'] = '0'
                       #Se imprime un mensaje que indique que ya está imprimiendo,  y que no existe esfuerzo, mostrando el costo actual
                        print("Localización de DESPACHO ya esta imprimiendo....")
                        print("No hay esfuerzo. Costo Actual:" + str(costo))
            #Condición cuando la segunda localización es el CUARTO
            elif ingreso_localizacion_2 == 'CUARTO':
                #Condición cuando el estado del CUARTO es 1
                if ingreso_estado_2 == '1':
                    #Imprime un mensaje indicando que no esta imprimiendo
                    print("Localización de  CUARTO no esta imprimiendo.........")
                    #Estableciendo el estado objetivo que es imprimir
                    estado_objetivo['CUARTO'] = '0'
                    costo += 1 #Incrementar un costo, ya que no estaba imprimiendo y hará el esfuerzo por imprimir
                    #Mensaje que le indica al usuario que ya esta imprimiendo
                    print("Imprimiendo archivo de CUARTO")
                    #Mensaje que imprime el costo actual
                    print("Costo actual: " + str(costo))
                    #Condición cuando el estado de SALA es 1
                    if ingreso_estado_3 == '1':
                        #Imprime un mensaje indicando que no esta imprimiendo
                        print("Localización: SALA no esta imprimiendo.........")
                        #Estableciendo el estado objetivo que es imprimir
                        estado_objetivo['SALA'] = '0'
                        costo += 1 #Incrementar un costo, ya que no estaba imprimiendo y hará el esfuerzo por imprimir
                        #Mensaje que le indica al usuario que ya esta imprimiendo
                        print("Imprimiendo archivo de SALA")
                        #Mensaje que imprime el costo actual
                        print("Costo actual: " + str(costo))
                    #Condición cuando el estado de SALA es 0
                    elif ingreso_estado_3 == '0':
                        #Se establece el estado objetivo
                        estado_objetivo['SALA'] = '0'
                       #Se imprime un mensaje que indique que ya está imprimiendo,  y que no existe esfuerzo, mostrando el costo actual
                        print("Localización de SALA ya esta imprimiendo....")
                        print("No hay esfuerzo. Costo Actual:" + str(costo))
                #Condición cuando el estado del cuarto es 0
                elif ingreso_estado_2 == '0':
                    #Se establece el estado objetivo
                    estado_objetivo['CUARTO'] = '0'
                   #Se imprime un mensaje que indique que ya está imprimiendo,  y que no existe esfuerzo, mostrando el costo actual
                    print("Localización de CUARTO ya esta imprimiendo....")
                    print("No hay esfuerzo. Costo Actual:" + str(costo))
                    #Condición cuando la el estado de SALA es 1
                    if ingreso_estado_3 == '1':
                        #Imprime un mensaje indicando que no esta imprimiendo
                        print("Localización de  SALA no esta imprimiendo.........")
                        #Estableciendo el estado objetivo que es imprimir
                        estado_objetivo['SALA'] = '0'
                        costo += 1 #Incrementar un costo, ya que no estaba imprimiendo y hará el esfuerzo por imprimir
                        #Mensaje que le indica al usuario que ya esta imprimiendo
                        print("Imprimiendo archivo de SALA")
                        #Mensaje que imprime el costo actual
                        print("Costo actual: " + str(costo))
                    #Condiciión cuando el estado de SALA es 0
                    elif ingreso_estado_3 == '0':
                        #Se establece el estado objetivo
                        estado_objetivo['SALA'] = '0'
                       #Se imprime un mensaje que indique que ya está imprimiendo,  y que no existe esfuerzo, mostrando el costo actual
                        print("Localización de SALA ya esta imprimiendo....")
                        print("No hay esfuerzo. Costo Actual:" + str(costo))
    #Impresiones finales con el estado objetivo que es 0 que significa que imprime y la medición de rendimiento de acuerdo al costo
    print("ESTADO OBJETIVO: ")
    print(estado_objetivo)
    print("Medición de rendimiento: "+str(costo))
# Permite correr el entorno
mundo_impresora()
