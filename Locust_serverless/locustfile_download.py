from locust import HttpUser,task,between
from urllib.parse import urlparse
import json



class AppUser(HttpUser):
    wait_time = between(2,5)
    
    @task
    def download_page(self):
        
            email_array = ["filesurfer97@gmail.com"]
            psw_array = ["filesurfer"]
            file_array = ["iris.arff"]
            #for index in range(0,3):
            response_login = self.client.post("/login", data=json.dumps({
                "email": email_array[0],
                "password": psw_array[0],
                }),auth=None,
                headers={'x-api-key':'XfvWhNRCkMa1Z8PtLECc88n4NyhvtufF905fdS7h', 'content-type': 'application/json'})
            
            token = response_login.json()['token']
            print("TOKEN: ", token)
            
            # Invia una richiesta POST con formData contenente un file
            response = self.client.post('/file-download', data=json.dumps({
                "filename": file_array[0],
                }),auth=None,
                headers={'x-api-key':'XfvWhNRCkMa1Z8PtLECc88n4NyhvtufF905fdS7h', 'content-type': 'application/json'})

            url = response.json()
            print("URL: " + url)
            # Puoi fare qualcosa con la risposta se necessario
            if (isValidURL(url)):
                # Esegui azioni in base alla risposta
                print("SUCCESS 200")
        

def isValidURL(url):
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except ValueError:
        return False
    