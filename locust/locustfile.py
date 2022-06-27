from locust import HttpUser, task, between

fof_request = "/?source=id_23&event_name=filledOutForm&event_status=status&payout=1000000"
other_request = "/?source=id_29&event_name=unknown&event_status=status&payout=100"
unknown_source_request = "/?source=id_2&event_name=unknown&event_status=status&payout=100"

class AppSendingEvent(HttpUser):
    wait_time = between(1, 5)

    @task(5)
    def send_filled_out_form(self):
        self.client.get(fof_request)

    @task(2)
    def send_other_event(self):
        self.client.get(other_request)

    @task(1)
    def send_unknown_source(self):
        self.client.get(unknown_source_request)