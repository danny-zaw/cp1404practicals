"""
CP1404 - Practical 7
Project Class

Estimated : 1 hour
Actual    : 3 days
"""

class Project:
    """Project class for storing project details."""
    def __init__(self, name, start_date, priority, cost_estimate, completion_percentage):
        """Initialize a project instance."""
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.completion_percentage = completion_percentage

    def __repr__(self):
        """Return a string representation of project instance."""
        return f"{self.name}, start: {self.start_date}, priority {self.priority}, estimate: ${self.cost_estimate}, completion: {self.completion_percentage}%"

    def __lt__(self, other):
        """ """
        return self.priority < other.priority

    def is_complete(self):
        """ """
        return self.completion_percentage == 100

