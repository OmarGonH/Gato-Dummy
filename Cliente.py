import socket

HOST = input("Ingresa la ip del servidor") # Hostname o  dirección IP del servidor
print("---------------Dificultad---------------- ")
modo_juego=input("1.Principiente\n2.Avanzado\nSelecciona una opción:")


PORT = 65432  # Puerto del servidor
buffer_size = 1024

#Creacion de la conexion
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as TCPClientSocket:
    #Ligamos puerto e IP
    TCPClientSocket.connect((HOST, PORT))
    print("Seleccionando modo de juego...")
    #Enviamos la dificultad seleccionada para el juego
    TCPClientSocket.sendall(bytes(str(modo_juego), 'utf-8'))
    #Recibimos el tablero
    tablero = str(TCPClientSocket.recv(buffer_size).decode())
    print(tablero)

    
    while True:
        tiro = input("Selecciona el numero de casilla en el tablero donde deseas tirar:")
        #Enviamos nuestra seleccion 
        tiro = str(tiro)
        TCPClientSocket.sendall(bytes(tiro, 'utf-8'))

        print("Esperando tiro...")
        #Esperamos una respuesta del servidor
        tablero = TCPClientSocket.recv(buffer_size).decode()
        print(tablero)
        if tablero.startswith(("FELICIDADES, HA GANADO EL CLIENTE", "MALA SUERTE, HA GANADO EL SERVIDOR", "ESTO ES UN EMPATE")):
            break
    tiempoejecucion = TCPClientSocket.recv(buffer_size).decode()
    print(tiempoejecucion)