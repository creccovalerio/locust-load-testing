from locust import HttpUser,task,between
from urllib.parse import urlparse
import json



class AppUser(HttpUser):
    wait_time = between(2,5)
    
    @task
    def download_page(self):
        
        email_array = ["vacrecco97@gmail.com", "ludovix9070@gmail.com", "filesurfer97@gmail.com"]
        psw_array = ["valerio", "ludovico", "filesurfer"]
        file_array = ["iris.arff", "vote.arff", "glass.arff"]
        for index in range(0,3):
            response_login = self.client.post("/login", data=json.dumps({
                "email": email_array[index],
                "password": psw_array[index],
                }),auth=None,
                headers={'x-api-key':'CqIRvghfaQlNhPna9d7P9q39aRmEwMT87auwBmF0', 'content-type': 'application/json'})
            
            token = response_login.json()['token']
            print("TOKEN: ", token)
            
            # Invia una richiesta POST con formData contenente un file
            response = self.client.post('/file-download', data=json.dumps({
                "filename": file_array[index],
                }),auth=None,
                headers={'x-api-key':'CqIRvghfaQlNhPna9d7P9q39aRmEwMT87auwBmF0', 'content-type': 'application/json'})

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
    