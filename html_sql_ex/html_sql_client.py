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
    username = input("enter username > ")
    msg = "SILT" + DIVIDER + username
    return msg


def present_data(data, pen):
    fields = data.split(DIVIDER)
    if fields[0] == "NURA":
        pen.new_account_confirmation()
        return "Account created successfully"
    elif fields[0] == "OLIF":
        data = fields[5][3:-2].split("', ")
        songs_and_rate = []
        for x in data:
            songs_and_rate.append(x)
        print(songs_and_rate)
        pen.create_info_page(fields[1], fields[2], fields[3], fields[4], songs_and_rate)
        return "Page displayed successfully"
    elif fields[0] == "DELT":
        pen.del_listener()
        return "Listener deleted successfully"
    elif fields[0] == "AOSL":
        pen.amount_of_songs(fields[1])
        return f"You've listened to {fields[1]} songs"
    else:
        pen.error_page()
        return "ERROR"


def del_listener():
    username = input("enter username > ")
    msg = "DELU" + DIVIDER + username
    return msg


def new_song():
    name = input("enter the song's name > ")
    rate = input("enter your rate (a number between 0 to 5, can be decimal) > ")
    msg = "ADDS" + DIVIDER + name + DIVIDER + rate
    return msg


def menu():
    print("1. Create new account\n" + \
          "2. See an account info\n" + \
          "3. Delete an account\n" + \
          "4. Add a song and rating to the list of songs you've listened to\n" + \
          "5. Get how many songs have you listened to\n" + \
          "6. Change your favorite song\n"
          "7. Exit\n\n>")

    data = input("Enter Num> ")
    msg = ''
    if data == "1":
        msg = new_listener()
    elif data == "2":
        msg = see_info()
    elif data == "3":
        msg = del_listener()
    elif data == "4":
        msg = new_song()
    elif data == "5":
        msg = get_listened_amount()
    elif data == "6":
        pass
    elif data == "7":
        return "q"
    else:
        return "ERR1"
    return msg


def main():
    cli_s = socket.socket()

    cli_s.connect(("127.0.0.1", 4000))
    pen = create_html.CreateClientPages()

    while True:
        data = menu()
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
