# to open/create a new html file in the write mode
import codecs

# import module
import webbrowser, sqlite3, SQL_ORM, create_html

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

    # table_list = [a[0] for a in
    #               m.execute("SELECT COUNT(*) FROM ListenersInfo WHERE username = 'abc123' AND password = 'abc123'")]
    # insert_new_user(m, 'li', 'df34', 'lili', 'evans', 'sos')
    # print(table_list[0])

with sqlite3.connect('Listeners.db') as db:
    k = db.cursor()
    username = input()
    password = input()
    sql = f"SELECT * FROM ListenersInfo WHERE username = '{username}' AND password = '{password}'"
    info = k.execute(sql).fetchone()
    print(str(info))
    username = info[1]
    password = info[2]
    first_name = info[3]
    last_name = info[4]
    sql = "SELECT * FROM dustyBun_listened"
    res = k.execute(sql).fetchall()
    print(res)
    pen = create_html.CreateClientPages()
    pen.create_info_page(first_name, last_name, username, password, res)
