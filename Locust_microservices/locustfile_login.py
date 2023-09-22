from locust import HttpUser,task,between

class AppUser(HttpUser):
    wait_time = between(2,5)

    @task
    def login_page(self):
        email_array = ["vacrecco97@gmail.com"]
        psw_array = ["valerio"]
        
        #for index in range(0,3):
        login_data = {
            'username': email_array[0],
            'password': psw_array[0]
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

        