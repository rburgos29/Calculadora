import socket

ip = '127.0.0.1'
puerto = 8092

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    cliente.connect((ip, puerto))
    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    print('Bienvenido a la calculadora!')
    print("elige una opción : pulsa 0 para terminar,1 para sumar o 2 para multiplicar")
    print("introduce la opcion seguido de los dos numeros , todo serparado por un espacio, sino dará error")
    c_abierta = True
    while c_abierta:

        msg1 = input(":")
        msg1 = str.encode(msg1)
        cliente.send(msg1)

        resultado = cliente.recv(1000).decode('utf-8')
        if resultado == 'Cerrando calculadora...':
            print(resultado)
            cliente.close()
        else:
            print('El resutado es: ', resultado)

except KeyboardInterrupt:
    cliente.close()
    print('Cerrando la calculadora...')
