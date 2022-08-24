__author__ = 'Roni Weiss'

import socket
import SQL_ORM

import threading
from tcp_by_size import send_with_size, recv_by_size

DEBUG = True
exit_all = False
user_list = []
DIVIDER = '~'


def handl_client(sock, tid, db):
    """
    handles client requests
    :param sock: client's socket
    :param tid: client's number
    :param db: connection to the data base
    """
    global exit_all

    print("New Client num " + str(tid))

    while not exit_all:
        try:
            data = recv_by_size(sock)
            if data == "":
                print("Error: Seens Client DC")
                break
            if 'EXIT' in data:
                break

            to_send = do_action(data, db)
            send_with_size(sock, to_send)

        except socket.error as err:
            if err.errno == 10054:
                print("Error %d Client is Gone. %s reset by peer." % (err.errno, str(sock)))
                break
            else:
                print("%d General Sock Error Client %s disconnected" % (err.errno, str(sock)))
                break

        except Exception as err:
            print("General Error:", err)
            break
    sock.close()


def do_action(data, db):
    """
    check what client ask and fill to send with the answer.
    :param data: what the client wants to do
    :param db: connection to data base
    """
    to_send = "ERR1"
    fields = data.split(DIVIDER)
    action = fields[0]


    if DEBUG:
        print("Got client request " + action + " -- " + str(fields))

    if action == 'NUSR':
        user = SQL_ORM.Listener(fields[1], fields[2], fields[3], fields[4], fields[5])
        song = SQL_ORM.Song(fields[5], fields[6], fields[7], fields[1])
        msg = db.new_listener(user, song)
        if msg == "OK":
            to_send = 'NURA'
        else:
            to_send = "ERR2"
    elif action == 'SWLI':
        print(fields[1], fields[2])
        info = db.get_single_listener_info(fields[1], fields[2])
        if info == "err2":
            return 'ERR2'
        to_send = "OLIF" + DIVIDER
        for x in range(len(info) - 1):
            to_send += info[x] + DIVIDER
        to_send += str(info[-1])
    elif action == "DELU":
        to_send = db.delete_listener(fields[1])
    elif action == "SILT":
        amount = db.get_listened(fields[1])
        if amount == "ERR2":
            return amount
        to_send = "AOSL" + DIVIDER + str(amount)
    elif action == "ADNS":
        song = SQL_ORM.Song(fields[2], fields[3], fields[4], fields[1])
        print(song)
        if not fields[5].isnumeric():
            return "ERR2"
        to_send = db.add_new_song(song, int(fields[5]))
    elif action == "GALD":
        to_send = "AIDB" + DIVIDER + db.get_all_info()
        if not to_send:
            return "ERR1"
    return to_send


def main():
    """
    main server loop
    """
    global exit_all, user_list

    exit_all = False
    db = SQL_ORM.ListenersORM()

    s = socket.socket()

    s.bind(("0.0.0.0", 4000))

    s.listen(4)
    print("after listen")

    threads = []
    i = 1
    while i < 6:
        cli_s, addr = s.accept()
        t = threading.Thread(target=handl_client, args=(cli_s, i, db))
        t.start()
        i += 1
        threads.append(t)

    exit_all = True
    for t in threads:
        t.join()

    s.close()


if __name__ == '__main__':
    main()
