import cookielib
import urllib
import urllib2
import requests

class RegistrationRepository:

    COURSES_URL = "http://registration.boun.edu.tr/home.htm"
    LOGIN_URL = "https://registration.boun.edu.tr/scripts/loginst.asp"

    username = ""
    password = ""
    session = None

    def __init__(self):
        self.session = requests.session()

    def get_reg_page(self):
        login_data = dict(user_id=self.username, user_pass=self.password)
        session_start_result = self.session.post(self.LOGIN_URL, data=login_data)
        return session_start_result.text


