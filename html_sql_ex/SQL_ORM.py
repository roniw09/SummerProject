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
               "username:" + self.username + "\n" +\
               "password:" + self.password + "\n" +\
               "first name:" + self.first_name+ "\n" + \
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
        self.current = None   # will store the DB connection cursor

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

    def commit(self):
        self.conn.commit()

    def getUserList(self):
        self.open_DB()
        user_table = [m[0] for m in self.current.execute("SELECT username FROM ListenersInfo")]
        print(user_table)
        return user_table



    #All read SQL

    def GetUser(self,username):
        self.open_DB()

        usr=None
        sql = f"""SELECT * FROM ListenersInfo 
                  WHERE username = '{username}'"""

        res = [m for m in self.current.execute(sql)][0]
        info = []
        for x in res:
            info.append(x)



         
        self.close_DB()
        return info
    
    def get_single_listener_info(self, username, password):
        with sqlite3.connect("Listeners.db") as db:
            c = db.cursor()
            sql = f"""SELECT * 
                      FROM ListenersInfo 
                      WHERE username = '{username}' AND password = '{password}'"""
            info = c.execute(sql).fetchone()
            username = info[1]
            password = info[2]
            first_name = info[3]
            last_name = info[4]

            sql = f"SELECT * FROM {username}_listened"
            res = c.execute(sql).fetchall()
            return [username, password, first_name, last_name, res]


    def get_amount_of_listened_songs(self,username):
        self.open_DB()
        sql = "SELECT listened FROM ListenersInfo WHERE and username='"+username+"'"
        res = [x[0] for x in self.current.execute(sql)][0]
        self.close_DB()
        return res

    def get_amount_of_users(self):
        self.open_DB()
        id = [x[0] for x in self.current.execute("SELECT COUNT(*) FROM ListenersInfo")][0]
        self.close_DB()
        return id


    #__________________________________________________________________________________________________________________
    #__________________________________________________________________________________________________________________
    #______end of read start write ____________________________________________________________________________________
    #__________________________________________________________________________________________________________________
    #__________________________________________________________________________________________________________________
    #__________________________________________________________________________________________________________________




    #All write SQL

    def new_listener(self,username,password,first_name,last_name, favorite_song):
        with sqlite3.connect("Listeners.db") as db:
            c = db.cursor()
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


    def update_user(self,user):
        self.open_DB()



        self.close_DB()
        return True


    def update_account(self,account):
        pass



    def delete_user(self,username):
        pass

    def delete_account(self,accountID):
        pass

