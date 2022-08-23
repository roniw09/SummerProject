import webbrowser

HEADER = "<!DOCTYPE html>"
class CreateClientPages:

    def clear_page(self):
        with open('page.html', 'w') as current_page:
            current_page.truncate(0)

    def create_info_page(self, username, password, first_name, last_name, songs_and_rate):
        self.clear_page()
        with open('page.html', 'w') as current_page:
            html_template = HEADER + """
            <html>
                <style>
                    body{background-color:#add8e6; font-family: assistant;}
                </style>
                <head>
                    <title>Info</title>
                    <link rel="icon" href="properties/icon2.png"></link>
                </head>"""
            html_template += f"""<body style="font-family: assistant">
                    <h2>Welcome {first_name} {last_name}, here's your info:</h2>

                    <p>
                        username: {username}<br>
                        password: {password}<br>
                    </p>
                    
                    <h4>Your Songs:</h4>
                    <table border="2" style="width:50%; align-content: center; text-align: center">
                        <tr>
                            <th>song</th>
                            <th>rate</th>
                        </tr>"""

            table_content = ""
            for x in range(0, len(songs_and_rate), 2):
                table_content += f"""<tr>
                                        <td>{songs_and_rate[x]}</td>
                                        <td>{songs_and_rate[x + 1]}</td>
                                     </tr>
                                  """
            html_template += table_content + """</body>
                    </html>
                    """

            current_page.write(html_template)

        webbrowser.open('page.html')

    def new_account_confirmation(self):
        self.clear_page()
        with open('page.html', 'w') as current_page:
            html_template = HEADER + """<html>
                <style>
                    body{background-color:#add8e6; font-family: assistant;}
                </style>
                <head>
                    <title>Register</title>
                    <link rel="icon" href="properties/icon.png"></link>
                </head>
                <body>
                    <h1>The account is registered!</h1>
                    <h3>Welcome to Listeners project!</h3>
                    <img src="properties/TightGreatCaimanlizard-size_restricted.gif">
                </body>
            </html>
                    """

            current_page.write(html_template)

        webbrowser.open('page.html')

    def del_listener(self):
        self.clear_page()
        with open('page.html', 'w') as current_page:
            html_template = HEADER + """<html>
                <style>
                    body{background-color:#add8e6; font-family: assistant;}
                </style>
                <head>
                    <title>Error</title>
                    <link rel="icon" href="properties/icon.png"></link>
                </head>
                <body>
                    <h1>Somthing went wrong!</h1>
                    <img src="properties/error.gif">
                </body>
            </html> """

            current_page.write(html_template)

        webbrowser.open('page.html')

    def error_page(self):
        self.clear_page()
        with open('page.html', 'w') as current_page:
            html_template = HEADER + """<html>
                <style>
                    body{background-color:#add8e6; font-family: assistant;}
                </style>
                <head>
                    <title>Error</title>
                    <link rel="icon" href="properties/icon.png"></link>
                </head>
                <body">
                    <h1>Deleted wanted account</h1>
                    <img src="properties/delete.gif">
                </body>
            </html>"""

            current_page.write(html_template)

        webbrowser.open('page.html')