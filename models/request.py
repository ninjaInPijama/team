class StudentRequest:
    def __init__(self, student_name, topics_difficulty, message):
        self.student_name = student_name
        self.topics_difficulty = topics_difficulty
        self.message = message

    def get_summary(self):
        return {
            "green": sum(1 for v in self.topics_difficulty.values() if v == "green"),
            "yellow": sum(1 for v in self.topics_difficulty.values() if v == "yellow"),
            "red": sum(1 for v in self.topics_difficulty.values() if v == "red")
        }

    def get_details(self):
        return {
            "student": self.student_name,
            "topics": self.topics_difficulty,
            "message": self.message
        }
