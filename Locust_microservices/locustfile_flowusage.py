from locust import HttpUser,task,between, SequentialTaskSet
import json

class AppUser(HttpUser):
    wait_time = between(2,5)

    @task
    def flowusage_page(self):
        
        email_array = ["vacrecco97@gmail.com", "ludovix9070@gmail.com", "filesurfer97@gmail.com"]
        psw_array = ["valerio", "ludovico", "filesurfer"]
        file_array = ["iris.csv", "vote.csv", "glass.csv"]
        fidARFF_array = ["65036675f7aa72ac85778577", "65036694d865bdeed05c3dcb", "650366b3f7aa72ac85778579"]
        for index in range(0,3):
            
            login_data = {
                'username': email_array[index],
                'password': psw_array[index]
            }

            response = self.client.post("/login", data=login_data)

            token = response.cookies
            print("TOKEN: ", token)
            
            form_data = {
                "file-upload-csv": (file_array[index], open("/home/valerio/wekafiles/data/data/"+file_array[index], "r"), "text/csv"),
            }

            # Invia una richiesta POST con formData contenente un file
            response = self.client.post('/upload_csv', files=form_data)

            # Puoi fare qualcosa con la risposta se necessario
            if response.status_code == 200:
                # Esegui azioni in base alla risposta
                print("UPLOAD SUCCESS 200")
            

            # Invia una richiesta POST con formData contenente un file
            response_download = self.client.get('/download_arff?fidARFF=' + fidARFF_array[index])
            if(response_download.status_code == 200):
                print("DOWNLOAD SUCCESS 200")

            response = self.client.get("/logout")
            if response.status_code == 200:
                # Esegui azioni in base alla risposta
                print("LOGOUT SUCCESS 200")