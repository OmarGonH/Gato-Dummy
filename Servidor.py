import socket
import random
import time

#calcualr tiempo
inicio = ''
final = ''
#Fichas de juego 
ficha_C='X'
ficha_S='O'

#Creacion del tablero
def tablero(opcion):

    if opcion=='1':
        prinTablero=''
        columnasS='       |        |        '+'\n'
        filas='------------------------'+'\n'
        columnasN1='1  '+str(matriz[0])+'   |2  '+str(matriz[1])+'    |3  '+str(matriz[2])+'        \n'
        columnasN2='4  '+str(matriz[3])+'   |5  '+str(matriz[4])+'    |6  '+str(matriz[5])+'        \n'
        columnasN3='7  '+str(matriz[6])+'   |8  '+str(matriz[7])+'    |9  '+str(matriz[8])+'        \n'

        prinTablero+=columnasS
        prinTablero+=columnasN1
        prinTablero+=columnasS
        prinTablero+=filas
        prinTablero+=columnasS
        prinTablero+=columnasN2
        prinTablero+=columnasS
        prinTablero+=filas
        prinTablero+=columnasS
        prinTablero+=columnasN3
        prinTablero+=columnasS
        return prinTablero
        
    elif opcion=='2': 
        prinTablero=''
        columnasS='       |        |        |        |        '+'\n'
        prinTablero+=columnasS
        columnasN1='1  '+str(matriz[0])+'   |2  '+str(matriz[1])+'    |3  '+str(matriz[2])+'    |4  '+str(matriz[3])+'    |5  '+str(matriz[4])+'\n'
        columnasN2='6  '+str(matriz[5])+'   |7  '+str(matriz[6])+'    |8  '+str(matriz[7])+'    |9  '+str(matriz[8])+'    |10  '+str(matriz[9])+'\n'
        columnasN3='11  '+str(matriz[10])+'  |12  '+str(matriz[11])+'   |13  '+str(matriz[12])+'   |14  '+str(matriz[13])+'   |15  '+str(matriz[14])+'\n'
        columnasN4='16  '+str(matriz[15])+'  |17  '+str(matriz[16])+'   |18  '+str(matriz[17])+'   |19  '+str(matriz[18])+'   |20  '+str(matriz[19])+'\n'
        columnasN5='21  '+str(matriz[20])+'  |22  '+str(matriz[21])+'   |23  '+str(matriz[22])+'   |24  '+str(matriz[23])+'   |25  '+str(matriz[24])+'\n'
        prinTablero+=columnasN1
        filas='-------------------------------------------'+'\n'
        prinTablero+=columnasS
        prinTablero+=filas
        prinTablero+=columnasS
        prinTablero+=columnasN2
        prinTablero+=columnasS
        prinTablero+=filas
        prinTablero+=columnasS
        prinTablero+=columnasN3
        prinTablero+=columnasS
        prinTablero+=filas
        prinTablero+=columnasS
        prinTablero+=columnasN4
        prinTablero+=columnasS
        prinTablero+=filas
        prinTablero+=columnasS
        prinTablero+=columnasN5
        prinTablero+=columnasS
        return prinTablero
        

#Definir final de partida
def empate(matriz,modo):
    if modo=='1':
        empate=True
        i=0
        while (empate==True and i<9):
            if matriz[i]==" ":
                empate=False
            i+=1
        return empate 
    elif modo=='2':
        empate=True
        i=0
        while (empate==True and i<25):
            if matriz[i]==" ":
                empate=False
            i+=1
        return empate 

def victoria(matriz,modo):
    if modo=='1':
        if(matriz[0]==matriz[1]==matriz[2]!=" " or matriz[3]==matriz[4]==matriz[5]!=" " or matriz[6]==matriz[7]==matriz[8]!=" " or
        matriz[0]==matriz[3]==matriz[6]!=" " or matriz[1]==matriz[4]==matriz[7]!=" " or matriz[2]==matriz[5]==matriz[8]!=" "):
            return True
        else:
            return False
    elif modo=='2':
        if(matriz[0]==matriz[1]==matriz[2]==matriz[3]==matriz[4]!=" "or 
           matriz[5]==matriz[6]==matriz[7]==matriz[8]==matriz[9]!=" "or 
           matriz[10]==matriz[11]==matriz[12]==matriz[13]==matriz[14]!=" " or
           matriz[15]==matriz[16]==matriz[17]==matriz[18]==matriz[19]!=" " or
           matriz[20]==matriz[21]==matriz[22]==matriz[23]==matriz[24]!=" " or
           matriz[0]==matriz[5]==matriz[10]==matriz[15]==matriz[20]!=" " or
           matriz[1]==matriz[6]==matriz[11]==matriz[16]==matriz[21]!=" " or
           matriz[2]==matriz[7]==matriz[12]==matriz[17]==matriz[22]!=" " or
           matriz[3]==matriz[8]==matriz[13]==matriz[18]==matriz[13]!=" " or
           matriz[4]==matriz[9]==matriz[14]==matriz[19]==matriz[24]!=" " ):
            return True
        else:
            return False

#Definir movimientos
def movimientos_cliente(modo,tiro):
        if modo=='1':
            posiciones=[0,1,2,3,4,5,6,7,8]
            casilla=int(tiro)
            if (casilla-1) not in posiciones:
                print("No existe esa casilla")
                print("Comience nuevo juego")
            else:
                if matriz[casilla-1]==" ":
                    matriz[casilla-1]= ficha_C

              

        elif modo=='2':
            posiciones=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24]
            casilla=int(tiro)
            if (casilla-1) not in posiciones:
                print("No existe esa casilla")
                print("COmience nuevo juego")
            else:
                if matriz[casilla-1]==" ":
                    matriz[casilla-1]= ficha_C

                

def movimientos_servidor(modo):
        if modo=='1':
            posiciones=[0,1,2,3,4,5,6,7,8]
            casilla=9
            parar=False

            for i in posiciones:
                copia=list(matriz)
                if copia[i]==" ":
                    copia[i]==ficha_S
                    if victoria(copia,modo_juego)==True:
                        casilla=i

            if casilla==9:
                for j in posiciones:
                    if copia[j]==" ":
                        copia[j]==ficha_C
                    if victoria(copia,modo_juego)==True:
                        casilla=j
                        
            if casilla==9:
                while(not parar):
                    casilla=random.randint(0,8)
                    if matriz[casilla]==" ":
                        parar=True
            matriz[casilla]=ficha_S

        elif modo=='2':
            posiciones=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24]
            casilla=25
            parar=False

            for i in posiciones:
                copia=list(matriz)
                if copia[i]==" ":
                    copia[i]==ficha_S
                    if victoria(copia,modo_juego)==True:
                        casilla=i

            if casilla==25:
                for j in posiciones:
                    if copia[j]==" ":
                        copia[j]==ficha_C
                    if victoria(copia,modo_juego)==True:
                        casilla=j
                        
            if casilla==25:
                while(not parar):
                    casilla=random.randint(0,24)
                    if matriz[casilla]==" ":
                        parar=True
            matriz[casilla]=ficha_S

#Revisar ganador
def revisar_ganador(contador,casilla):
        ganador=contador
        if victoria(matriz,modo_juego):
            if ganador%2==0:
                return [True,"FELICIDADES, HA GANADO EL CLIENTE \n"]
            
            else:
                return [True,"MALA SUERTE, HA GANADO EL SERVIDOR \n"]

        elif empate(matriz,modo_juego):
            return [True,"ESTO ES UN EMPATE \n"]

        elif ganador%2==0:
            movimientos_servidor(modo_juego)
            return [False,"Tiro del servidor: \n"]

        elif ganador%2!=0:
            movimientos_cliente(modo_juego,casilla)
            return [False,"Tiro del cliente: \n"]
        

HOST = "192.168.56.1"  # Direccion de la interfaz de loopback estándar (localhost)
PORT = 65432  # Puerto que usa el cliente  (los puertos sin provilegios son > 1023)
buffer_size = 1024
#Creacion del socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as TCPServerSocket:
    #Enviamos la IP y el puerto
    TCPServerSocket.bind((HOST, PORT))
    #Servidor a la escucha
    TCPServerSocket.listen()
    print("El servidor TCP está disponible y en espera de solicitudes")
    #Regresa la conexion y direccion del cliente->aceptando la conexion, aqui creamos el canal de conexion
    client_conn, client_addr = TCPServerSocket.accept()
    #Se abre la conexion
    with client_conn:
        def final(condicion):       
            if condicion:
                return True
            return False
        print("Conectado a", client_addr)
        #Recibimos el  modo de juego
        modo_juego  = str(client_conn.recv(buffer_size).decode())
        #Se genera el tablero
        if modo_juego=='1':
            matriz=[" "]*9
        elif modo_juego=='2':
            matriz=[" "]*25
        partida=False
        ganador=1
       
        #Validamos el modo de juego
        if modo_juego == '1' or modo_juego=='2':
            mitablero=tablero(modo_juego)
            print(mitablero)
             #Enviamos en tablero al cliente
            client_conn.sendall(bytes(mitablero, 'utf-8'))
            #Comienza el tiempo de la ejecucion
            inicio = time.time()
            while not partida:
                #ganador=ganador+1
                
                #Esperando recibir el tiro del cliente
                print("Esperando tiro del cliente... ")
                #Guardamos la casilla que eligio
                tiro  = client_conn.recv(buffer_size).decode()
                print(tiro)
                tirocliente=revisar_ganador(ganador,tiro)
                ganador+=1
                #tiro_servidor=revisar_ganador(ganador,tiro)
                tiroserver=revisar_ganador(ganador,tiro)
                
                #Se realiza el tiro y se guarda el tablero nuevo
                mitablero= tiroserver[1] + tablero(modo_juego)
                #Se envia de nuevo el tablero y el estatus de la partida
                partida=final(tiroserver[0])
                print("Enviando tablero a: ", client_addr)
                client_conn.sendall(bytes(mitablero, 'utf-8'))
            
            final = time.time()
            tiempoejecucion = final - inicio
            enviartiempo = f"El juego tuvo una duración de {round(tiempoejecucion, 2)}s"
            client_conn.sendall(bytes(enviartiempo, 'utf-8'))

        else:
            print("Modo de juego no valido")

