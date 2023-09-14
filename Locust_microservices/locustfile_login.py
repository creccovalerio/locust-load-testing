from locust import HttpUser,task,between
import datetime

class AppUser(HttpUser):
    wait_time = between(2,5)

    @task
    def login_page(self):
        email_array = ["vacrecco97@gmail.com", "ludovix9070@gmail.com", "filesurfer97@gmail.com"]
        psw_array = ["valerio", "ludovico", "filesurfer"]
        
        for index in range(0,3):
            login_data = {
                'username': email_array[index],
                'password': psw_array[index]
            }

            response = self.client.post("/login", data=login_data)

            token = response.cookies
            print("TOKEN: ", token)

            if response.status_code == 200:
                print("SUCCESS 200")

            response = self.client.get("/logout")
            if response.status_code == 200:
                # Esegui azioni in base alla risposta
                print("LOGOUT SUCCESS 200")

        