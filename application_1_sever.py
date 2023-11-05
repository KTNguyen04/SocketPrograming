import socket
SEVER_NAME = '127.0.0.1'
WELCOME_PORT = 6789
WELCOME_ADDR = SEVER_NAME, WELCOME_PORT


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

                modified_data = processing(recv_data)
                send_processing(working_socket, modified_data)
            # message = input("Sever: ")
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


def modify_data(data):
    result = computing(data)
    return " = " + str(result)


def at_sever_proc(data):
    print("Client: ", data)


def computing(data):
    return eval(data)
    # client_socket.close()d


def get_message(socket_obj):
    return socket_obj.recv(1024)


def send_message(socket_obj, message):
    socket_obj.sendall(bytes(str(message), 'utf8'))


def main():
    tcp_sever_soc(send_, modify_data, recv_, at_sever_proc)


"""run"""
if __name__ == "__main__":
    main()
