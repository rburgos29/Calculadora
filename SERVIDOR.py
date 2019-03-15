import socket
ip = '127.0.0.1'
puerto = 8092
respuestas = 2

servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    servidor.bind((ip, puerto))
    servidor.listen(respuestas)
    print('Esperando conexion en {ip},{puerto}'.format(ip = ip, puerto = puerto))
    (cliente, direccion) = servidor.accept()
    print('Se ha conectado alguien')
    c_abierta = True
    while c_abierta:
        opcion=cliente.recv(1000).decode('utf-8')
        opcion=opcion.split(" ")
        if opcion[0]=="0":
            msg = ('Cerrando calculadora...')
            msg = str.encode(msg)

            cliente.send(msg)

        elif opcion[0]== "1":
            msg=int(opcion[1]) + int(opcion[2])
            msg=str(msg)
            msg = str.encode(msg)
            cliente.send(msg)
        elif opcion[0]=="2":
            msg= int(opcion[1]) * int(opcion[2])
            msg=str(msg)
            msg = str.encode(msg)
            cliente.send(msg)
        else:
            print("introduzca una opcion valida ")
            c_abierta = False





except KeyboardInterrupt:
    cliente.close()
    print('Cerrando la calculadora...')
