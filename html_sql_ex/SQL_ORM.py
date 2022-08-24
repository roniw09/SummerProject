import sqlite3


class Listener(object):
    def __init__(self, username, password, first_name, last_name, favorite_song):
        self.username = username
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
        self.favorite_song = favorite_song

    def get_username(self):
        return self.username

    def get_password(self):
        return self.password

    def get_first_name(self):
        return self.first_name

    def get_last_name(self):
        return self.last_name

    def __str__(self):
        return f"{self.username}, {self.password}, {self.first_name}, {self.last_name}, {self.favorite_song}"


class Song(object):
    def __init__(self, name, artist, release_year, who_added):
        self.name = name
        self.artist = artist
        self.release_year = release_year
        self.who_added = who_added

    def get_name(self):
        return self.name

    def get_artist(self):
        return self.artist

    def get_release_year(self):
        return self.release_year

    def get_who_added(self):
        return self.who_added

    def __str__(self):
        return f"{self.name}, {self.artist}, {self.release_year}, {self.who_added}"


class ListenersORM:

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
            username = info[0]
            password = info[1]
            first_name = info[2]
            last_name = info[3]

            sql = f"""SELECT * FROM Songs
                      WHERE username = '{username}'"""
            res = c.execute(sql).fetchall()
            print(res)
            list = ''
            for x in range(len(res)):
                for i in range(1, len(res[x])):
                    list += str(res[x][i]) + "|"
            return [username, password, first_name, last_name, list]

    def new_listener(self, user, song):
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
            twice = self.check_if_exsist(user.get_username())
            if twice:
                return "ERR2"
            listened = 1
            print("here")
            q = f"""INSERT INTO ListenersInfo
                    VALUES ('{user.get_username()}', '{user.get_password()}', '{user.get_first_name()}', '{user.get_last_name()}',
                            {listened}, '{song.get_name()}')"""
            c.execute(q)
            print("here2")
            q = f"""INSERT INTO Songs
                    VALUES ('{user.get_username()}', '{song.get_name()}', '{song.get_artist()}', 
                           '{song.get_release_year()}',  5)"""
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
            sql = f"""DELETE FROM Songs
                      WHERE username = '{username}'"""
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
            sql = f"SELECT COUNT(name) FROM Songs WHERE username = '{username}'"
            res = c.execute(sql).fetchone()[0]
            return res

    def add_new_song(self, song, rate):
        """
            adds a new song to listener's data
            :param song: the song we want to add
            :param rate: the listener's rate
        """
        with sqlite3.connect("Listeners.db") as db:
            c = db.cursor()
            exist = self.check_if_exsist(song.get_who_added())
            if not exist:
                return "ERR2"
            q = f"""INSERT INTO Songs
                    VALUES ('{song.get_who_added()}', '{song.get_name()}', '{song.get_artist()}', 
                                        '{song.get_release_year()}', {rate})"""
            c.execute(q)
            new_amount = self.get_listened(song.get_who_added()) + 1
            q = f"""UPDATE ListenersInfo
                    SET num_of_listened = {new_amount}
                    WHERE username = '{song.get_who_added()}';"""
            c.execute(q)
            return "NSWA"
