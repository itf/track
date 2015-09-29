from parse_rest.connection import register
from parse_rest.datatypes import Object
from parse_rest.user import User
import json
APPLICATION_ID = "bLxJPXQ34sup0hAmY8DEdELkxgWQgLgQT47dCxnf"
REST_API_KEY = "03fSuGga6CnI4Xod0Uf7LPTcrDbNmTJwST7jvV2z"
register(APPLICATION_ID, REST_API_KEY)

class sampleTimeTable(Object):
    pass

class mit_submit_utils:
    SUBMIT_FILE = "last-submit"
    @staticmethod
    def get_table(tableId):
        sampleTimeTable.Query.get("tableId")
    @staticmethod
    def get_user(username, password):
        return User.login(str(username), str(password))
    @staticmethod
    def get_table_id_from_user(user):
        pass

    @classmethod
    def save_last_submit(cls,value):
            _file_name = mit_submit_utils.SUBMIT_FILE
            with open(_file_name, 'w') as _file:
                json.dump(value, _file,
                          sort_keys=False)
    @classmethod
    #throw exception
    def get_last_submit(cls):
        _file_name = mit_submit_utils.SUBMIT_FILE
        with open(_file_name) as _file:
            _struct = json.load(_file)
        user_pass = _struct;
        return user_pass
    @classmethod
    def clear(cls):
        save_last_submit(cls,[0,0])

