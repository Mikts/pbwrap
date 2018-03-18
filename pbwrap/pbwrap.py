"""A simple pastebin api wrapper."""

import requests
import os
import pbwrap.formatter as formatter
from pbwrap.constants import API_OPTIONS


class Pastebin(object):

    def __init__(self, api_dev_key=None):
        """Instantiate a Pastebin Object.
           Attributes : api_dev_key(Find it here https://pastebin.com/api after you login)
                        api_user_key(obtained after authenticating with get_user_id)
           Most functions require at least an api_dev_key parameter.
           Functions for manipulating your pastes through the API require an api_user_key.
        """
        self.api_dev_key = api_dev_key
        self.api_user_key = None

    def get_user_id(self, username, password):
        """Return a string with the api user key."""
        data = {'api_dev_key': self.api_dev_key,
                'api_user_name': username,
                'api_user_password': password}

        r = requests.post('https://pastebin.com/api/api_login.php', data)

        self.api_user_key = r.text
        return self.api_user_key

    def get_user_details(self):
        """Return user details in a dictionary.
           Can only be user after authenticating with get_user_id(username, password).
        """
        data = {'api_dev_key': self.api_dev_key,
                'api_user_key': self.api_user_key}

        r = requests.post('https://pastebin.com/api/api_post.php', data)

        return formatter.user_from_xml(r.text)

    def get_trending(self):
        """Return a list of paste objects created from the most trending pastes"""
        data = {
            'api_dev_key': self.api_dev_key,
            'api_option': API_OPTIONS['TREND']}

        r = requests.post('https://pastebin.com/api/api_post.php', data)

        return formatter.paste_list_from_xml(r.text)

    @staticmethod
    def get_archive():
        """Return archive paste link list.Archive contains 25 most recent pastes."""
        r = requests.get('https://pastebin.com/archive')

        return formatter.archive_url_format(r.text)

    def get_raw_paste(self, paste_id):
        """Return raw text of given paste_id."""
        r = requests.get('https://pastebin.com/raw/' + paste_id)
        return r.text

    def create_paste(
            self,
            api_paste_code,
            api_paste_private=0,
            api_paste_name=None,
            api_paste_expire_date=None,
            api_paste_format=None):
        """Create a new paste if succesfull return it's url."""
        data = {'api_dev_key': self.api_dev_key,
                'api_user_key': self.api_user_key,
                'api_paste_code': api_paste_code,
                'api_paste_private': api_paste_private,
                'api_paste_name': api_paste_name,
                'api_paste_expire_date': api_paste_expire_date,
                'api_paste_format': api_paste_format,
                'api_option': API_OPTIONS['PASTE']}

        # Filter data and remove dictionary None keys.
        filtered_data = {k: v for k, v in data.items() if v is not None}

        r = requests.post('https://pastebin.com/api/api_post.php', filtered_data)

        return r.text

    def create_paste_from_file(
            self,
            filepath,
            api_paste_private=0,
            api_paste_name=None,
            api_paste_expire_date=None,
            api_paste_format=None):
            """Create a new paste from file if succesfull return it's url."""
            if os.path.exists(filepath):
                api_paste_code = open(filepath).read()
                return create_paste(api_paste_code, api_paste_private,
                                    api_paste_name, api_paste_expire_date, api_paste_format)

            print('File not found')
            return None

    def get_user_pastes(self, api_results_limit=None):
        """Return a list of Pastes created from user pastes."""
        data = {'api_dev_key': self.api_dev_key,
                'api_user_key': self.api_user_key,
                'api_results_limit': api_results_limit,
                'api_option': API_OPTIONS['USER_PASTE']}

        # Filter data and remove dictionary None keys.
        filtered_data = {k: v for k, v in data.items() if v is not None}

        r = requests.post('https://pastebin.com/api/api_post.php', filtered_data)

        if r.text:
            return formatter.paste_list_from_xml(r.text)

        return 'No pastes in this account'

    def get_user_raw_paste(self, api_paste_key):
        """Return the raw data of a user paste(even private pastes!) as string."""
        data = {'api_dev_key': self.api_dev_key,
                'api_user_key': self.api_user_key,
                'api_paste_key': api_paste_key,
                'api_option': API_OPTIONS['USER_RAW_PASTE']}

        r = requests.post('https://pastebin.com/api/api_post.php', data)

        return r.text

    def delete_user_paste(self, api_paste_key):
        """Deletes a paste created by the user."""
        data = {'api_dev_key': self.api_dev_key,
                'api_user_key': self.api_user_key,
                'api_paste_key': api_paste_key,
                'api_option': API_OPTIONS['DELETE_PASTE']}

        r = requests.post('https://pastebin.com/api/api_post.php', data)

        return r.text
