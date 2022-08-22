__author__ = 'Yossi'

import socket, SQL_ORM
from tcp_by_size import send_with_size, recv_by_size

DIVIDER = '~'
my_account = None


def new_listener():
    global my_account
    info = []
    msg = 'NUSR' + DIVIDER
    info.append(str(input("Enter username > ")))
    info.append(str(input("Enter password > ")))
    info.append(str(input("Enter first name > ")))
    info.append(str(input("Enter last name > ")))
    info.append(str(input("Enter favorite song > ")))
    print(info)

    for x in range(len(info) - 1):
        msg += info[x] + DIVIDER
    msg += info[-1]

    print(msg, type(msg))

    my_account = SQL_ORM.Listener(info[0], info[1], info[2], info[3], info[4])

    return msg


def manu():
    print("1. Create new account\n" + \
          "2. Log in with an existing account\n" + \
          "3. Delete account\n" + \
          "4. Get your favorite song\n>" + \
          "5. Add a song and rating to the list of songs you've listened to\n>" + \
          "6. Get how many songs have you listened to\n>" + \
          "9. exit\n\n>")

    data = input("Enter Num> ")

    if data == "9":
        return "q"
    elif data == "1":
        msg = new_listener()
        return msg
    else:
        return "ERR1"


def main():
    cli_s = socket.socket()

    cli_s.connect(("127.0.0.1", 4000))

    while True:
        data = manu()
        print(data, type(data))

        if data == "q":
            send_with_size(cli_s, "EXIT")
            break
        send_with_size(cli_s, data)

        data = recv_by_size(cli_s)
        if data == "":
            print("seems server DC")
            break
        print("Got>>" + data)


if __name__ == '__main__':
    main()
