class User:
    def __init__(self, username, user_type):
        self.username = username
        self.user_type = user_type

class Student(User):
    def __init__(self, username):
        super().__init__(username, "student")
        self.requests = []

    def submit_request(self, request):
        self.requests.append(request)

class Teacher(User):
    def __init__(self, username):
        super().__init__(username, "teacher")
        self.received_requests = []

    def receive_request(self, request):
        self.received_requests.append(request)

    def get_requests(self):
        return self.received_requests
