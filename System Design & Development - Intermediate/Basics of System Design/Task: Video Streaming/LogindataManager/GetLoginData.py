import os
from dotenv import load_dotenv


class GetLoginData:
    def __init__(self):
        load_dotenv()

        self.email_id = os.environ.get("email_id")
        self.password = os.environ.get("password")
        print(self.email_id, self.password)

    def check_credentials(self, email_id, password):
        if self.email_id == email_id and self.password == password:
            print(email_id, password)
            return True
        else:
            return False

    def check_email_id(self, email_id):
        if self.email_id != email_id:
            return True
        else:
            return False

    def check_password(self, password):
        if self.password != password:
            return True
        else:
            return False
