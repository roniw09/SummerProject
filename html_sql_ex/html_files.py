# to open/create a new html file in the write mode
import codecs

# import module
import webbrowser, sqlite3

f = open('GFG.html', 'w')

# the html code which will go in the file GFG.html
html_template = """<html>
<head>
<title>Title</title>
</head>
<body>
<h2>Welcome To GFG</h2>

<p>Default code has been loaded into the Editor.</p>

</body>
</html>
"""

# writing the code into the file
f.write(html_template)

# close the file
f.close()


# open html file
# webbrowser.open('GFG.html')

def insert_new_user(c, username, password, first_name, last_name, favorite_song):
    id = [x[0] for x in c.execute("SELECT COUNT(*) FROM ListenersInfo")][0] + 1
    listened = 0
    q = f"""INSERT INTO ListenersInfo
            VALUES ({str(id)}, '{username}', '{password}', '{first_name}', '{last_name}', {listened}, '{favorite_song}')"""
    c.execute(q)


with sqlite3.connect("Listeners.db") as db:
    m = db.cursor()
    m.execute("DELETE FROM ListenersInfo")
    # table_list = [a[0] for a in
    #               m.execute("SELECT COUNT(*) FROM ListenersInfo WHERE username = 'abc123' AND password = 'abc123'")]
    # insert_new_user(m, 'li', 'df34', 'lili', 'evans', 'sos')
    # print(table_list[0])
