import sqlite3


class ListenersORM():

    def __init__(self):
        """
        initialize class
        """
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
        """
        close database connection
        """
        self.conn.close()

    def check_if_exsist(self, username):
        """
        checks if a listener exist
        :param username: the listener's username
        """
        with sqlite3.connect("Listeners.db") as db:
            c = db.cursor()
            sql = f"SELECT COUNT(username) FROM ListenersInfo WHERE username = '{username}'"
            res = c.execute(sql).fetchone()[0]
            print(res)
            if res == 0:
                return False
            return True

    def get_single_listener_info(self, username, password):
        """
        returns a listener information
        :param username: the listener's username
        :param password: the listener's username
        """
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

    def new_listener(self, username, password, first_name, last_name, favorite_song):
        """
        adds a listener to database
        :param username: the listener's username
        :param password: the listener's username
        :param first_name: the listener's first name
        :param last_name: the listener's last name
        :param favorite_song: the listener's favorite song
        """
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
                                            rating INTEGER)"""
            c.execute(q)
            q = f"""INSERT INTO {username}_listened
                    VALUES ('{favorite_song}', 5)"""
            c.execute(q)
            return "OK"

    def delete_listener(self, username):
        """
        deletes a listener from database
        :param username: the listener's username
        """
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
        """
            returns how many songs a listener listened to
            :param username: the listener's username
        """
        with sqlite3.connect("Listeners.db") as db:
            c = db.cursor()
            exist = self.check_if_exsist(username)
            if not exist:
                return "ERR2"
            sql = f"SELECT COUNT(song_name) FROM {username}_listened"
            res = c.execute(sql).fetchone()[0]
            return res

    def add_new_song(self, username, song_name, rate):
        """
            adds a new song to listener's data
            :param username: the listener's username
            :param song_name: the song's name
            :param rate: the listener's rate
        """
        with sqlite3.connect("Listeners.db") as db:
            c = db.cursor()
            exist = self.check_if_exsist(username)
            if not exist:
                return "ERR2"
            q = f"""INSERT INTO {username}_listened
                    VALUES ('{song_name}', {rate})"""
            c.execute(q)
            new_amount = self.get_listened(username) + 1
            q = f"""UPDATE ListenersInfo
                    SET num_of_listened = {new_amount}
                    WHERE username = '{username}';"""
            c.execute(q)
            return "NSWA"
