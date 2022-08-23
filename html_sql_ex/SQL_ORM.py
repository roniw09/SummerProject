import sqlite3

import pickle
# https://docs.python.org/2/library/sqlite3.html
# https://www.youtube.com/watch?v=U7nfe4adDw8
import webbrowser


class Listener(object):
    def __init__(self, username, password, first_name, last_name, favorite_song):
        self.username = username
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
        self.favorite_song = favorite_song
        self.listened = 0

    def change_password(self, password):
        self.password = password

    def __str__(self):
        return "listener:\n" \
               "username:" + self.username + "\n" + \
               "password:" + self.password + "\n" + \
               "first name:" + self.first_name + "\n" + \
               "last name: " + self.last_name + "\n" + \
               "favorite song: " + self.favorite_song

    def update_listened(self, added):
        self.listened += added

    def get_username(self):
        return self.username

    def get_password(self):
        return self.password

    def get_first_name(self):
        return self.first_name

    def get_last_name(self):
        return self.last_name

    def get_favorite_song(self):
        return self.favorite_song


class ListenersORM():

    def __init__(self):
        self.conn = None  # will store the DB connection
        self.current = None  # will store the DB connection cursor

    def open_DB(self):
        """
        will open DB file and put value in:
        self.conn (need DB file name)
        and self.cursor
        """
        self.conn = sqlite3.connect("Listeners.db")
        self.current = self.conn.cursor()

    def close_DB(self):
        self.conn.close()


    def check_if_exsist(self, username):
        with sqlite3.connect("Listeners.db") as db:
            c = db.cursor()
            sql = f"SELECT COUNT(username) FROM ListenersInfo WHERE username = '{username}'"
            res = c.execute(sql).fetchone()[0]
            print(res)
            if res == 0:
                return False
            return True


    def get_single_listener_info(self, username, password):
        with sqlite3.connect("Listeners.db") as db:
            c = db.cursor()
            sql = f"""SELECT * 
                      FROM ListenersInfo 
                      WHERE username = '{username}' AND password = '{password}'"""
            info = c.execute(sql).fetchone()
            if not info:
                return 'err2'
            username = info[1]
            password = info[2]
            first_name = info[3]
            last_name = info[4]

            sql = f"SELECT * FROM {username}_listened"
            res = c.execute(sql).fetchall()
            return [username, password, first_name, last_name, res]

    def get_amount_of_users(self):
        self.open_DB()
        id = [x[0] for x in self.current.execute("SELECT COUNT(*) FROM ListenersInfo")][0]
        self.close_DB()
        return id

    def new_listener(self, username, password, first_name, last_name, favorite_song):
        with sqlite3.connect("Listeners.db") as db:
            c = db.cursor()
            twice = self.check_if_exsist(username)
            print(twice)
            if twice:
                return "ERR2"
            id = self.get_amount_of_users() + 1
            print(id)
            listened = 0
            q = f"""INSERT INTO ListenersInfo
                    VALUES ({str(id)}, '{username}', '{password}', '{first_name}', '{last_name}', {listened}, '{favorite_song}')"""
            c.execute(q)
            q = f"""CREATE TABLE {username}_listened(
                                            song_name TEXT,
                                            raiting REAL)"""
            c.execute(q)
            q = f"""INSERT INTO {username}_listened
                    VALUES ('{favorite_song}', 5)"""
            c.execute(q)
            return "OK"

    def delete_listener(self, username):
        with sqlite3.connect("Listeners.db") as db:
            c = db.cursor()
            exist = self.check_if_exsist(username)
            if not exist:
                return "ERR2"
            sql = f"DELETE FROM ListenersInfo WHERE username = '{username}'"
            c.execute(sql)
            sql = f"DROP TABLE {username}_listened"
            c.execute(sql)
            return "DELT"

    def get_listened(self, username):
        with sqlite3.connect("Listeners.db") as db:
            c = db.cursor()
            exist = self.check_if_exsist(username)
            if not exist:
                return "ERR2"
            sql = f"SELECT COUNT(song_name) FROM {username}_listened"
            res = c.execute(sql).fetchone()[0]
            return str(res)