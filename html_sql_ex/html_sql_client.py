__author__ = 'Yossi'

import socket, SQL_ORM

import create_html
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
    print(my_account)

    return msg


def see_info():
    username = input("enter username > ")
    password = input("enter password > ")
    msg = 'SWLI' + DIVIDER + username + DIVIDER + password
    return msg


def get_listened_amount():
    username = input("enter username")
    password = input("enter password")
    msg = f"SILT{DIVIDER}{username}{DIVIDER}{password}"
    return msg


def present_data(data, pen):
    fields = data.split(DIVIDER)
    if fields[0] == "NURA":
        return "Account created successfully"
    if fields[0] == "OLIF":
        data = fields[5][3:-2].split("', ")
        songs_and_rate = []
        for x in data:
            songs_and_rate.append(x)
        print(songs_and_rate)
        pen.create_info_page(fields[1], fields[2], fields[3], fields[4], songs_and_rate)
        return "Page displayed successfully"


def manu():
    print("1. Create new account\n" + \
          "2. See an account info\n" + \
          "3. Delete an account\n" + \
          "4. Change your favorite song\n>" + \
          "5. Add a song and rating to the list of songs you've listened to\n>" + \
          "6. Get how many songs have you listened to\n>" + \
          "7. exit\n\n>")

    data = input("Enter Num> ")

    if data == "7":
        return "q"
    elif data == "1":
        msg = new_listener()
    elif data == "2":
        msg = see_info()
    elif data == "6":
        msg = get_listened_amount()
    else:
        return "ERR1"
    return msg


def main():
    cli_s = socket.socket()

    cli_s.connect(("127.0.0.1", 4000))
    pen = create_html.CreateClientPages()

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
        data = present_data(data, pen)
        print("Got>>" + data)


if __name__ == '__main__':
    main()
