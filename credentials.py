import os
import json


class Credentials:
    @staticmethod
    def get_credentials():
        with open('account_credentials.json', 'rb') as account_credentials:
            dict_account_credentials = json.load(account_credentials)

            return dict_account_credentials