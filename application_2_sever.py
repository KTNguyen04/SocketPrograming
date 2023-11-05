import requests
import socket
from datetime import datetime
from weather import get_response
SEVER_NAME = '127.0.0.1'
WELCOME_PORT = 6789
WELCOME_ADDR = SEVER_NAME, WELCOME_PORT


def get_weather():
    raw_weather = get_response()
    temp = raw_weather['main']['temp'] - 272.15
    weather = raw_weather['weather'][0]['main']
    place = raw_weather['name']
    return f'{place} \n Temperature: {temp}\xb0C \n Weather: {weather}'


def tcp_sever_soc(send_processing, processing, recv_processing, at_sever_processing):
    welcome_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    welcome_socket.bind(WELCOME_ADDR)
    welcome_socket.listen(1)
    print('Sever is ready to connect')
    while True:
        working_socket, client_addr = welcome_socket.accept()
        print("Listening from ", client_addr)
        try:
            while True:
                recv_data = recv_processing(working_socket)
                if recv_data.lower() == 'exception':
                    working_socket.close()
                    break
                at_sever_processing(recv_data)

                treated_data = processing(recv_data)
                send_processing(working_socket, treated_data)
            # message = input("Sever: "
               # working_socket.send(bytes(recv_data.upper(), 'utf8'))
        except KeyboardInterrupt:
            print("Close connection")
            working_socket.close()
            break
            # print("Close connection")
        finally:
            working_socket.close()
            print("Close connection")

    welcome_socket.close()


def send_(socket_obj, message):
    send_message(socket_obj, message)


def recv_(socket_obj):
    recv = get_message(socket_obj)
    recv = recv.decode('utf8')
    return recv


def handle_data(data):
    if data.lower() == 'hello':
        return 'Hello, how are you?'
    elif data.lower() == 'what is the time':
        return datetime.now().strftime('%H:%M:%S %d/%m/%Y')
    elif data.lower() == 'what is the weather like':
        return get_weather()
    else:
        return 'Not understand'


def at_sever_proc(data):
    print("Client: ", data)


def get_message(socket_obj):
    return socket_obj.recv(1024)


def send_message(socket_obj, message):
    socket_obj.sendall(bytes(str(message), 'utf8'))


def main():
    tcp_sever_soc(send_, handle_data, recv_, at_sever_proc)


"""run"""
if __name__ == "__main__":
    main()
