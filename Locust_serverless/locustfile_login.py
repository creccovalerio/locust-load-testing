from locust import HttpUser,task,between, SequentialTaskSet
import json

class AppUser(HttpUser):
    wait_time = between(2,5)

    @task
    def login_page(self):
        email_array = ["vacrecco97@gmail.com", "ludovix9070@gmail.com", "filesurfer97@gmail.com"]
        psw_array = ["valerio", "ludovico", "filesurfer"]
        
        for index in range(0,3):
            response = self.client.post("/login", data=json.dumps({
                            "email": email_array[index],
                            "password": psw_array[index],
                            }),auth=None,
                            headers={'x-api-key':'CqIRvghfaQlNhPna9d7P9q39aRmEwMT87auwBmF0', 'content-type': 'application/json'})

            token = response.json()['token']
            print("TOKEN: ", token)

            if(response.status_code == 200):
                print("SUCCESS 200")