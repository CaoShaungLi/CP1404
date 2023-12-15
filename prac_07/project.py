"""Project class program"""


class Project:
    """Represent information of project"""

    def __init__(self, project, start_date, priority, cost_estimate, completion_percentage):
        """Initialise a project instance"""
        self.project = project
        self.start_date = start_date
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.completion_percentage = completion_percentage

    def __str__(self):
        """Return string about project"""
        return f"{self.project}, start: {self.start_date}, priority {self.priority}, estimate: {self.cost_estimate}" \
               f" completion: {self.completion_percentage}%"

    def __lt__(self, other):
        return self.completion_percentage < other.completion_percentage
