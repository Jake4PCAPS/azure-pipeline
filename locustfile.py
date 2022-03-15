from locust import HttpUser, task

class PredictionTest(HttpUser):
    @task
    def prediction_test(self):
        self.client.get("/")