from locust import HttpUser,task,between, SequentialTaskSet
import json

class AppUser(HttpUser):
    wait_time = between(2,5)

    @task
    def register_page(self):
        email_array = ["dea97@mail.com", "enrico97@mail.com", "pier97@mail.com"]
        psw_array = ["alessandro", "enrico", "pier"]
        for index in range(0,3):
            self.client.post("/register", data=json.dumps({
            "email": email_array[index],
            "password": psw_array[index],
            }),auth=None,
            headers={'x-api-key':'XfvWhNRCkMa1Z8PtLECc88n4NyhvtufF905fdS7h', 'content-type': 'application/json'})
