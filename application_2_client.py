import socket
SEVER_NAME = '127.0.0.1'
SEVER_PORT = 6789
SEVER_ADDR = SEVER_NAME, SEVER_PORT


def tcp_client_soc(input_request, send_processing, recv_processing, at_client_processing):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(SEVER_ADDR)
    try:
        print("Ctrl + C to stop\n")
        while True:
            message = input_request()
            send_processing(client_socket, message)
            respond = recv_processing(client_socket)
            at_client_processing(respond)
           # print("Sever: ", respond)
    except KeyboardInterrupt:
        # print("Close connection")
        client_socket.sendall(bytes("Exception", 'utf8'))
    finally:
        print("Close connection")
        client_socket.close()


def send_(socket_obj, message):
    # client_socket.sendall(bytes(message, 'utf8'))
    send_message(socket_obj, message)


def recv_(socket_obj):
    respond = get_message(socket_obj)
    return respond.decode('utf8')

    # client_socket.close()d


def at_client_(data):

    print("Sever: ", data)


def user_input():
    return input("Client: ")


def get_message(socket_obj):
    return socket_obj.recv(1024)


def send_message(socket_obj, message):
    socket_obj.sendall(bytes(message, 'utf8'))


"""run"""


def main():
    tcp_client_soc(user_input, send_, recv_, at_client_)


if __name__ == "__main__":
    main()
