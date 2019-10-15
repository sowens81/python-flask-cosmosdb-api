class User():

    userLevel = "basic"

    def __init__(self,firstName,lastName,emailAddress):
        self.firstName = firstName
        self.lastName = lastName
        self.emailAddress = emailAddress
        self.userLevel = self.userLevel
    
    def __str__(self):
        return "User"
