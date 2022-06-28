from locust import HttpUser, task, between
import requests

class WebsiteTestUser(HttpUser):
    wait_time = between(0.1, 0.9)
    def on_start(self):
        self.client.verify = False
    def on_stop(self):
        pass

    @task(1)
    def hello_world(self):
        requests.packages.urllib3.disable_warnings()
        self.client.post('/getOpenersAPIzl89zqiNpYpfa6Pw19V4',json={"cid":"123"})