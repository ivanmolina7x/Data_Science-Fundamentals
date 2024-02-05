class UserAuthentication:
    def __init__(self, className) :
        self._className = className

    def ValidateUser(self, uname, pwd):
        return self._className.ValidateUser(self, uname, pwd)

class FakeServiceAuthentication(UserAuthentication):
    def ValidateUser(self, uname, pwd):
        if(uname == 'guest' and pwd == 'guest'):
            return True
        else:
            return False

import sqlite3
from sqlite3 import Error
class DBServiceAuthentication(UserAuthentication):
    def ValidateUser(self, uname, pwd ):
        try:
            con = sqlite3.connect('sqldb.db')
            sql = f"select count(*) from Users where Username='{uname}' and Password='{pwd}'"
            cursor = con.cursor()
            cursor.execute(sql)
            result = cursor.fetchone()
            if result[0] > 0 :
                return True
            else:
                return False
        except Error:
            print(Error)
        finally:
            con.close()

#ua = UserAuthentication(FakeServiceAuthentication)

import json
import sys
import types

def str_to_class(classname):
    return getattr(sys.modules[__name__], classname)

with open('service.json') as f:
    data = json.load(f)

service = str_to_class(data['name'])

ua = UserAuthentication(service)

uname = input('Enter Username :')
pwd = input('Enter Password :')

result = ua.ValidateUser(uname, pwd)

print(f'Result : {result}')