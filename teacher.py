from user import User

class Teacher(User):
    def __init__(self, username, password):
        super().__init__(username, password, "teacher")
        self.requests_received = []  # list of requests received from students

    def receive_request(self, request):
        self.requests_received.append(request)