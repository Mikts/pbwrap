"""A simple pastebin api wrapper."""

import requests
from ppaw import ppaw_formatter as ppaw_form
from ppaw.helpers.constants import API_OPTIONS


class Pastebin(object):

    def __init__(self, api_dev_key):
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
        """Return user details"""
        data = {'api_dev_key': self.api_dev_key,
                'api_user_key': self.api_user_key}

        r = requests.post('https://pastebin.com/api/api_post.php', data)

        return ppaw_form.user_from_xml(r.text)

    def get_trending(self):
        """Return a dictionary of paste objects with the most trending pastes."""
        data = {
            'api_dev_key': self.api_dev_key,
            'api_option': API_OPTIONS['TREND']}

        r = requests.post('https://pastebin.com/api/api_post.php', data)

        return ppaw_form.paste_list_from_xml(r.text)

    @staticmethod
    def get_archive():
        """Return archive paste list.Archive contains 25 most recent pastes."""
        r = requests.get('https://pastebin.com/archive')

        return ppaw_form.archive_url_format(r.text)

    def get_raw_paste(self, paste_id):
        """Return raw text of given paste_id."""
        r = requests.get('https://pastebin.com/raw/' + paste_id)
        return r.text

    def create_new_paste(
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

    def get_user_pastes(self, api_results_limit=None):
        """Return a list of user pastes."""
        data = {'api_dev_key': self.api_dev_key,
                'api_user_key': self.api_user_key,
                'api_results_limit': api_results_limit,
                'api_option': API_OPTIONS['USER_PASTE']}

        # Filter data and remove dictionary None keys.
        filtered_data = {k: v for k, v in data.items() if v is not None}

        r = requests.post('https://pastebin.com/api/api_post.php', filtered_data)

        if r.text:
            return ppaw_form.paste_list_from_xml(r.text)

        return 'No pastes in this account'

    def delete_user_paste(self, api_paste_key):
        """Deletes a paste created by the user."""
        data = {'api_dev_key': self.api_dev_key,
                'api_user_key': self.api_user_key,
                'api_paste_key': api_paste_key,
                'api_option': API_OPTIONS['DELETE_PASTE']}

        r = requests.post('https://pastebin.com/api/api_post.php', data)

        return r.text
