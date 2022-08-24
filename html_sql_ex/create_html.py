import webbrowser

HEADER = "<!DOCTYPE html>"


class CreateClientPages:

    def clear_page(self):
        """
        clear last page
        """
        with open('page.html', 'w') as current_page:
            current_page.truncate(0)

    def create_info_page(self, username, password, first_name, last_name, songs_and_rate):
        """
        create the info page
        :param username: the listener's username
        :param password: the listener's username
        :param first_name: the listener's first name
        :param last_name: the listener's last name
        :param favorite_song: the listener's favorite song
        :param songs_and_rate: list of the songs a listener listened to
        """
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
        """
        confirm a new listener was created
        """
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

    def error_page(self):
        """
        present there was an error
        """
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

    def del_listener(self):
        """
        confirm a new listener was deleted
        """
        self.clear_page()
        with open('page.html', 'w') as current_page:
            html_template = HEADER + """<html>
                <style>
                    body{background-color:#add8e6; font-family: assistant;}
                </style>
                <head>
                    <title>Deleted</title>
                    <link rel="icon" href="properties/icon.png"></link>
                </head>
                <body>
                    <h1>Deleted wanted account</h1>
                    <img src="properties/delete.gif">
                </body>
            </html>"""

            current_page.write(html_template)

        webbrowser.open('page.html')

    def amount_of_songs(self, amount):
        """
        presents how many songs a listener listened to
        """
        self.clear_page()
        with open('page.html', 'w') as current_page:
            html_template = HEADER + """<html>
                <style>
                    body{background-color:#add8e6; font-family: assistant;}
                </style>
                <head>
                    <title>Songs Amount</title>
                    <link rel="icon" href="properties/icon.png"></link>
                </head>"""
            html_template += f"""
                <body>
                    <h2>You've listened to...</h2>
                    <h1>{amount} songs!!</h1>
                    <img src="properties/amount.gif">
                </body>
            </html>"""

            current_page.write(html_template)

        webbrowser.open('page.html')

    def new_song_added(self):
        """
        confirm a new song was added
        """
        self.clear_page()
        with open('page.html', 'w') as current_page:
            html_template = HEADER + """<html>
                        <style>
                            body{background-color:#add8e6; font-family: assistant;}
                        </style>
                        <head>
                            <title>New Song</title>
                            <link rel="icon" href="properties/icon.png"></link>
                        </head>
                        <body>
                            <h1>You've listened to a new song!</h1>
                            <h2>Good Job!!</h2>
                            <img src="properties/amount.gif">
                        </body>
                    </html>"""

            current_page.write(html_template)

        webbrowser.open('page.html')
