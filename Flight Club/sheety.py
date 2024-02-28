import requests

class User:

    def add_new_row(self, f_name, l_name, email):
        url = 'YOUR_SHEETY_ENDPOINT'
        header = {
            "Content-Type": "application/json"
        }

        body = {
            "user": {
                "firstName": f_name,
                "lastName": l_name,
                "email": email
            }
        }

        response = requests.post(url, json=body, headers=header)
        print(response.text)

