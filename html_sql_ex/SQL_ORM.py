import sqlite3

import pickle
    # https://docs.python.org/2/library/sqlite3.html
    # https://www.youtube.com/watch?v=U7nfe4adDw8


__author__ = 'user'


class Listener(object):
    def __init__(self, username, password, first_name, last_name, email):
        self.username = username
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.songs = []
        self.songs = []

    def change_password(self, password):
        self.password = password

    def __str__(self):
        return "listener:" + \
               "name:" + self.username + "\n" +\
               "password:" + self.password + "\n" +\
               "first name:" + self.first_name+ "\n" + \
               "last name: " + self.last_name + "\n" + self.email

    def update_listened(self, added):
        self.songs += added


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
        # sql= "SELECT ................ "
        res= self.current.execute(sql)




         
        self.close_DB()
        return usr
    
    def GetAccounts(self):
        pass
    def GetUsers(self):
        self.open_DB()
        usrs=[]






        self.close_DB()

        return usrs



    def get_user_balance(self,username):
        self.open_DB()

        sql="SELECT a.Balance FROM Accounts a , Users b WHERE a.Accountid=b.Accountid and b.Username='"+username+"'"
        res = self.current.execute(sql)
        for ans in res:
            balance =  ans[0]
        self.close_DB()
        return balance


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
            id = [x[0] for x in c.execute("SELECT COUNT(*) FROM ListenersInfo")][0] + 1
            print(id)
            listened = 0
            q = f"""INSERT INTO ListenersInfo
                    VALUES ({str(id)}, '{username}', '{password}', '{first_name}', '{last_name}', {listened}, '{favorite_song}')"""
            c.execute(q)
            q = f"""CREATE TABLE {username}_listened(
                                            song_name TEXT,
                                            raiting REAL)"""
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

