class ToDo:
    def __init__(self, title, description):
        self.title = title
        self.description = description


    # Returns title an description of the 'to do' to the list
    def __str__(self):
        return f"{self.title}\n    {self.description}"