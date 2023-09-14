from locust import HttpUser,task,between, SequentialTaskSet
import json

class AppUser(HttpUser):
    wait_time = between(2,5)

    @task
    def register_page(self):
        
        email_array = ["pippo@mail.com", "pluto@mail.com", "paperino@mail.com"]
        psw_array = ["pippo", "pluto", "paperino"]

        for index in range(0,3):
            register_data = {
                'username': email_array[index],
                'password': psw_array[index]
            }

            response = self.client.post("/register", data=register_data)

            if response.status_code == 200:
                print("SUCCESS 200")
