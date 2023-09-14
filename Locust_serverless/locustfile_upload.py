from locust import HttpUser,task,between, SequentialTaskSet
import json

class AppUser(HttpUser):
    wait_time = between(2,5)

    @task
    def upload_page(self):
        
        email_array = ["vacrecco97@gmail.com", "ludovix9070@gmail.com", "filesurfer97@gmail.com"]
        psw_array = ["valerio", "ludovico", "filesurfer"]
        file_array = ["iris.csv", "vote.csv", "glass.csv"]
        for index in range(0,3):
            response_login = self.client.post("/login", data=json.dumps({
                "email": email_array[index],
                "password": psw_array[index],
                }),auth=None,
                headers={'x-api-key':'CqIRvghfaQlNhPna9d7P9q39aRmEwMT87auwBmF0', 'content-type': 'application/json'})
            
            token = response_login.json()['token']
            print("TOKEN: ", token)
            
            form_data = {
                "file": (file_array[index], open("/home/valerio/wekafiles/data/data/"+file_array[index], "r"), "text/csv"),
                "email": email_array[index]
            }

            # Invia una richiesta POST con formData contenente un file
            response = self.client.post('/file-upload', files=form_data)

            # Puoi fare qualcosa con la risposta se necessario
            if response.status_code == 200:
                # Esegui azioni in base alla risposta
                print("SUCCESS 200")
        