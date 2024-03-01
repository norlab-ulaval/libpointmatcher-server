class User:
    username = ""
    email = ""
    password = ""
    
    def __init__(self, username=None, email=None, password=None):
        self.username = username
        self.email = email
        self.password = password
