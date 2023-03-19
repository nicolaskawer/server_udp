# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
# this function get the dictionary and the vale and return the key of the value
import socket
def get_key_by_value(my_dict, value):
    for key, val in my_dict.items():
        if val == value:
            return key
    return None

clients = {}
UDP_IP = '0.0.0.0'
UDP_PORT = 9999
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0)
sock.bind((UDP_IP, UDP_PORT))
while True:
    source, address = sock.recvfrom(1024)
    message = source.decode()
    if " " in message:
        destination, message = message.split(' ', 1)
        name_of_client = get_key_by_value(clients, address)
        # go to the function and see if there are a client in the dictionary
        if name_of_client is None:
            sock.sendto(b'U cant send a message! Enter your name first', address)
        else:
            if destination in clients:
                destination_address = clients[destination]
                sock.sendto(b'U got message from ' + name_of_client.encode() + b' as:' + message.encode(), destination_address)
                print(f'Sent message from {name_of_client} to {destination}: {message}')
            else:
                sock.sendto(b'No such user', address)
                print(f'{name_of_client} is trying to send to a non-existent user: {destination}')
    else:
        if message not in clients and address not in clients:
            clients[message] = address
            print(f'Added client {message}: {address}')


sock.close()



def print_hi(name):   # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
