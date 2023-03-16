# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import socket
clients = {}
UDP_IP = '0.0.0.0'
UDP_PORT = 9999
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0)
sock.bind((UDP_IP, UDP_PORT))
while True:
    source, address = sock.recvfrom(1024)
    message = source.decode()
    if message not in clients and address not in clients:
        clients[message] = address
        print(f'Added client {message}: {address}')
    else:
        if message not in clients and address in clients:
            print(" ERROR there is no user with name: ", message)
        else:
             if message in clients and clients[message] is not address:
                print("the message has been send to: ", message)
             else:
                destination, message = message.split(' ', 1)
                if destination in clients:
                    destination_address = clients[destination]
                    sock.sendto(message.encode(), destination_address)
                    print(f'Sent message from {message} to {destination}: {message}')
                else:
                    sock.sendto(b'No such user', address)
                    print(f'No such user: {destination}')

    print(clients)






def print_hi(name):   # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
