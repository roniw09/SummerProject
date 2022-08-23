__author__ = 'Roni Weiss'

import socket
import SQL_ORM

import queue, threading, time, random
from tcp_by_size import send_with_size, recv_by_size

DEBUG = True
exit_all = False
user_list = []
DIVIDER = '~'


def handl_client(sock, tid, db):
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
                # 'Connection reset by peer'
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
    check what client ask and fill to send with the answer
    """
    to_send = "ERR1"
    fields = data.split(DIVIDER)
    action = fields[0]


    if DEBUG:
        print("Got client request " + action + " -- " + str(fields))

    if action == 'NUSR':
        msg = db.new_listener(fields[1], fields[2], fields[3], fields[4], fields[5])
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
        to_send = "AOSL" + DIVIDER + amount

    return to_send


def main():
    global exit_all, user_list

    exit_all = False
    db = SQL_ORM.ListenersORM()

    s = socket.socket()

    s.bind(("0.0.0.0", 4000))

    s.listen(4)
    print("after listen")

    threads = []
    i = 1
    while i < 5:
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
