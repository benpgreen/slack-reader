import requests

from .responses import User, Channel
from .tools import get_request_url


class SlackReader:

    def __init__(self, API_KEY):
        self.api_key = API_KEY

    def get_users(self, active_only=True):

        url = get_request_url('users.list', self.api_key)
        response = requests.get(url)
        response = response.json()
        if not response['ok']:
            raise RuntimeError("Problem connecting to slack.")
        user_list = []
        for user in response['members']:
            if not user['deleted'] or not active_only:
                user_list.append(User(self.api_key, user))
        self.users = user_list

    def get_channels(self):

        url = get_request_url('channels.list', self.api_key)
        response = requests.get(url)
        response = response.json()
        if not response['ok']:
            raise RuntimeError("Problem connecting to slack.")
        channel_list = []
        for channel in response['channels']:
            if channel['is_channel']:
                channel_list.append(Channel(self.api_key, channel))
        self.channels = channel_list
