class Project:
    """Create a project class"""

    def __init__(self, name='', start_date='', priority=0, cost_estimate=0.0, completion_percentage=0):
        """Initialize Project object."""
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.completion_percentage = completion_percentage

    def __str__(self):
        """Return a string representation."""
        return (f"{self.name}, start: {self.start_date}, priority {self.priority}, "
                f"estimate: ${self.cost_estimate:.2f}, completion: {self.completion_percentage}%")

    def __lt__(self, other):
        """Add a comparison method (sorted by priority)"""
        return self.priority < other.priority

    def is_completed(self):
        """Check if project is fully done."""
        return self.completion_percentage == 100

    def update_percentage(self, percentage):
        """Update the completion percentage of project."""
        self.completion_percentage = percentage

    def update_priority(self, priority):
        """Update the priority of project."""
        self.priority = priority