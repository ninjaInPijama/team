class Request:
    def __init__(self, student_username, topics_difficulty, message):
        self.student_username = student_username
        self.topics_difficulty = topics_difficulty  # dict: {"Math": "red", "Science": "yellow"}
        self.message = message