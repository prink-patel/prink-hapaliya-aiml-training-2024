import os
from dotenv import load_dotenv


class GetLoginData:
    def __init__(self):
        load_dotenv()

        self.email_id = os.environ.get("email_id")
        self.password = os.environ.get("password")

    #check if credentials are correct or not
    def check_credentials(self, email_id, password):
        if self.email_id == email_id and self.password == password:
            return True
        else:
            return False
    # check if email id is correct or not
    def check_email_id(self, email_id):
        if self.email_id != email_id:
            return True
        else:
            return False
    # check if password is correct or not
    def check_password(self, password):
        if self.password != password:
            return True
        else:
            return False
