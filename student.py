from user import User
from request import Request

class Student(User):
    def __init__(self, username, password):
        super().__init__(username, password, "student")
        self.requests = []  # list of requests sent to teachers

    def send_request(self, teacher, topics_difficulty, message):
        request = Request(self.username, topics_difficulty, message)
        self.requests.append(request)
        teacher.receive_request(request)