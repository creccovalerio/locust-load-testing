from locust import HttpUser,task,between, SequentialTaskSet
import json

class AppUser(HttpUser):
    wait_time = between(2,5)

    @task
    def upload_page(self):
        
            email_array = ["filesurfer97@gmail.com"]
            psw_array = ["filesurfer"]
            file_array = ["iris.csv"]
            #for index in range(0,3):
            response_login = self.client.post("/login", data=json.dumps({
                "email": email_array[0],
                "password": psw_array[0],
                }),auth=None,
                headers={'x-api-key':'XfvWhNRCkMa1Z8PtLECc88n4NyhvtufF905fdS7h', 'content-type': 'application/json'})
            
            token = response_login.json()['token']
            print("TOKEN: ", token)
            
            form_data = {
                "file": (file_array[0], open("/home/valerio/wekafiles/data/data/"+file_array[0], "r"), "text/csv"),
                "email": email_array[0]
            }

            # Invia una richiesta POST con formData contenente un file
            response = self.client.post('/file-upload', files=form_data)

            # Puoi fare qualcosa con la risposta se necessario
            if response.status_code == 200:
                # Esegui azioni in base alla risposta
                print("SUCCESS 200")
        