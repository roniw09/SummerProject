import webbrowser


class CreateClientPages:

    def create_info_page(self, username, password, first_name, last_name, songs_and_rate):
        with open('page.html', 'w') as current_page:
            html_template = f"""<html>
                    <head>
                        <title>Info</title>
                    </head>
                    <body style="font-family: assistant">
                        <h2>Welcome {first_name} {last_name}, here's you're info:</h2>
    
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
